
~~~
mkdir v2ray-agent  &&  cd v2ray-agent
curl https://raw.githubusercontent.com/alliswell2day/v2ray-v3-manager/v2ray_api/install.sh -o install.sh && chmod +x install.sh && bash install.sh
~~~

### Docker + docker-compose 

**install Docker：**
~~~
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
~~~

**install docker-compose：**

~~~
sudo curl -L https://github.com/docker/compose/releases/download/1.17.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
~~~



**uninstall docker-compose：**

~~~
sudo rm /usr/local/bin/docker-compose
~~~


####  v2ray + Caddy : tls (ws)

edit Caddyfile

~~~
{$V2RAY_DOMAIN}
{
  root /srv/www
  log ./caddy.log
  proxy {$V2RAY_PATH} localhost:10550 {
    websocket
    header_upstream -Origin
  }
  gzip
  tls {$V2RAY_EMAIL} {
    protocols tls1.0 tls1.2
    # remove comment if u want to use cloudflare ddns
    # dns cloudflare
  }
}
~~~

edit: docker-compose.yml 

~~~
version: '2'

services:
 v2ray:
    image: rico93/v2ray_v3:api_alpine
    restart: always
    network_mode: "host"
    environment:
      sspanel_url: "https://xxxx"
      key: "xxxx"
      docker: "true"
      speedtest: 6
      node_id: 10
    logging:
      options:
        max-size: "10m"
        max-file: "3"

 caddy:
    image: rico93/v2ray_v3:caddy
    restart: always
    environment:
      - ACME_AGREE=true
#      if u want to use cloudflare ddns service
#      - CLOUDFLARE_EMAIL=xxxxxx@out.look.com
#      - CLOUDFLARE_API_KEY=xxxxxxx
      - V2RAY_DOMAIN=xxxx.com
      - V2RAY_PATH=/v2ray
      - V2RAY_EMAIL=xxxx@outlook.com
    network_mode: "host"
    volumes:
      - ./.caddy:/root/.caddy
      - ./Caddyfile:/etc/Caddyfile
~~~

**run：**

~~~
docker-compose up (ADD -d TO RUN IN BACKGROUND）
~~~



edit:  docker-compose.yml 

~~~
version: '2'

services:
 v2ray:
    image: rico93/v2ray_v3:api_alpine
    restart: always
    network_mode: "host"
    environment:
      sspanel_url: "https://xxxx"
      key: "xxxx"
      docker: "true"
      speedtest: 6
      node_id: 10
    logging:
      options:
        max-size: "10m"
        max-file: "3"
~~~

**RUN：**

~~~
docker-compose up (ADD -d TO RUN IN BACKGROUND）
~~~

### Docker 

Pull the image（Ubuntu  500M、alpine 200M）


~~~
docker pull alliswell2day/v2ray:api_alpine

// or 

docker pull alliswell2day/v2ray:api_ubuntu

//run

docker run -d --network=host --name v2ray_v3_api -e node_id=1 -e key=ixidnf -e sspanel_url=https://xx -e docker=true --log-opt max-size=50m --log-opt max-file=3 --restart=always alliswell2day/v2ray:api_alpine
~~~


### standard install

**install v2ray：**

~~~
bash <(curl -L -s https://install.direct/go.sh)
~~~



CentOS：

~~~
yum install -y https://centos7.iuscommunity.org/ius-release.rpm
yum update
yum install -y git python36u python36u-libs python36u-devel python36u-pip gcc
python3.6 -V
~~~

~~~
git clone -b v2ray_api https://github.com/alliswell2day/v2ray-v3-manager.git
cd v2ray-v3-manager
cp config/config_example.yml config/config.yml
cp config/config.json /etc/v2ray/config.json
pip3.6 install -r requirements.txt
~~~

**edit**

edit: config.yml， docker SET TO false SET sspanel_url、key、node_id 。
edit /etc/v2ray/config.json  config.yml  api_port, edit : config.json LINE 12。

**RUN：**

~~~
screen -S v2ray
python3.6 run.py --config-file=config/config.yml
~~~


