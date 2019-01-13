import logging

from Munager.MuAPI import MuAPI
from Munager.V2Manager import V2Manager
import json
from copy import deepcopy
import traceback
import socket
from configloader import load_config
class Munager(object):

    def __init__(self):
        self.config =load_config()

        # set logger
        self.logger = logging.getLogger()
        # mix
        self.mu_api = MuAPI()

        self.manager = V2Manager()

        self.first_time_start = True

    def update_manager(self):

        new_node_info = self.mu_api.get_node_info()
        if new_node_info:
            self.logger.info("Old Node infos: {}".format(self.manager.next_node_info))
            self.logger.info("New Node infos: {}".format(new_node_info))
            if json.dumps(self.manager.next_node_info,sort_keys=True,indent=2) != json.dumps(new_node_info,sort_keys=True,indent=2):
                self.manager.next_node_info=new_node_info
                self.manager.update_server()
            # get from MuAPI and ss-manager
            users = self.mu_api.get_users('email', self.manager.next_node_info)
            current_user = self.manager.get_users()
            self.logger.info('get MuAPI and ss-manager succeed, now begin to check ports.')

            # remove user by prefixed_id
            for prefixed_id in current_user:
                if prefixed_id not in users or not users.get(prefixed_id).available:
                    self.manager.remove(prefixed_id)
                    self.logger.info('need to remove client: {}.'.format(prefixed_id))

            # add prefixed_id
            for prefixed_id, user in users.items():
                if user.available and prefixed_id not in current_user:
                    if self.manager.add(user):
                        self.logger.info('need to add user email {}.'.format(prefixed_id))

                if user.available and prefixed_id in current_user:
                    if user != current_user.get(prefixed_id):
                        if self.manager.remove(prefixed_id) and self.manager.add(user):
                            self.logger.info('need to reset user {} due to method or password changed.'.format(prefixed_id))

            # check finish
            self.logger.info('check ports finished.')
            self.logger.info("if update {}".format(self.manager.if_user_change))
            if self.manager.if_user_change:
                self.manager.if_user_change = False
                self.manager.update_users()
                self.manager.current_node_info = self.manager.next_node_info
        else:
            # self.manager.next_node_info or new_node_info 此时 current不为空
            # 选择直接初始化全部用户
            # start remove inbounds
            self.logger.info("initial system")
            self.manager.remove_inbounds()
            self.manager.users_to_be_removed=deepcopy(self.manager.users)
            self.manager.users_to_be_add ={}
            self.manager.update_users()
            self.manager.current_node_info = None
            self.manager.next_node_info = None
            self.first_time_start = True



    def upload_throughput(self):
        current_user = self.manager.get_users()
        online_amount = 0
        data = []
        for prefixed, user in current_user.items():
            laset_traffic_upload,laset_traffic_download,user_id= self.manager.get_last_traffic(user)
            current_upload,current_download = self.manager.client.get_user_traffic_uplink(user.email),\
                                            self.manager.client.get_user_traffic_downlink(user.email)
            if current_download is None:
                current_download = 0
            else:
                current_download = int(current_download)
            if current_upload is None:
                current_upload = 0
            else:
                current_upload = int(current_upload)

            if current_download+current_upload < laset_traffic_upload+laset_traffic_download:
                online_amount += 1
                self.logger.warning('error throughput, try fix.')
                self.manager.set_current_traffic(user, upload=current_upload,download=current_download)
            elif current_download+current_upload > laset_traffic_upload+laset_traffic_download:
                online_amount += 1
                upload_dif = current_upload - laset_traffic_upload
                download_dif = current_download - laset_traffic_download
                data.append({'u': upload_dif, 'd': download_dif, 'user_id': user_id})

        if self.mu_api.upload_throughput(data):
            self.logger.info("Successfully upload {} users traffics".format(len(data)))
        else:
            self.logger.info('update trafic faileds')

        # update online users count
        if self.mu_api.post_online_user(online_amount):
            self.logger.info('upload online user count: {}.'.format(online_amount))
        else:
            self.logger.warning('failed to upload online user count.')

        self.mu_api.upload_systemload()

    @staticmethod
    def del_servers():
        global db_instance
        db_instance.logger.info("initial system")
        db_instance.manager.remove_inbounds()
        db_instance.manager.users_to_be_removed = deepcopy(db_instance.manager.users)
        db_instance.manager.users_to_be_add = {}
        db_instance.manager.update_users()
        db_instance.manager.current_node_info = None
        db_instance.manager.next_node_info = None
        db_instance.first_time_start = True

    @staticmethod
    def thread_db(obj):
        global db_instance
        timeout = 60
        socket.setdefaulttimeout(timeout)
        db_instance = obj()
        try:
            import resource
            logging.info(
                'current process RLIMIT_NOFILE resource: soft %d hard %d' %
                resource.getrlimit(
                    resource.RLIMIT_NOFILE))
        except:
            pass
        try:
            while True:
                try:
                    ping = db_instance.mu_api.webapi.getApi('func/ping')
                    if ping is None:
                        logging.error(
                            'something wrong with your http api, please check your config and website status and try again later.')
                    else:
                        db_instance.update_manager()
                        db_instance.upload_throughput()
                except Exception as e:
                    trace = traceback.format_exc()
                    logging.error(trace)
                    # logging.warn('db thread except:%s' % e)
                if db_instance.event.wait(timeout) or not db_instance.is_all_thread_alive():
                    break
                if db_instance.has_stopped:
                    break
        except KeyboardInterrupt as e:
            pass
        db_instance.del_servers()
        db_instance = None

    @staticmethod
    def thread_db_stop():
        global db_instance
        db_instance.has_stopped = True
        db_instance.event.set()

