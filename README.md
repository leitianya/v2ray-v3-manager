
~~~
mkdir v2ray-agent  &&  cd v2ray-agent
curl https://raw.githubusercontent.com/alliswell2day/v2ray-v3-manager/v2ray_api/install.sh -o install.sh && chmod +x install.sh && bash install.sh
~~~



~~~

docker pull alliswell2day/v2ray:api_alpine



### standard install

**install v2ray：**


bash <(curl -L -s https://install.direct/go.sh)




CentOS：


yum install -y https://centos7.iuscommunity.org/ius-release.rpm
yum update
yum install -y git python36u python36u-libs python36u-devel python36u-pip gcc
python3.6 -V



git clone -b v2ray_api https://github.com/alliswell2day/v2ray-v3-manager.git
cd v2ray-v3-manager
cp config/config_example.yml config/config.yml
cp config/config.json /etc/v2ray/config.json
pip3.6 install -r requirements.txt



**edit**

edit: config.yml， docker SET TO false SET sspanel_url、key、node_id 。
edit /etc/v2ray/config.json  config.yml  api_port, edit : config.json LINE 12。

**RUN：**


screen -S v2ray
python3.6 run.py --config-file=config/config.yml
~~~


