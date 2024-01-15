---
title: docker学习
tags:
  - 搭建博客
  - 前端
date: 2023-10-28 20:52:22
abbrlink: 8mzes
---

docker下载

docker配置

镜像
容器
容器卷

dockerFile

父镜像

端口映射

私有仓库

docker命令


客户端连接


和虚拟机区别

共享宿主机内核

uname -m  看系统架构
docker pull mysql --platform arm64

docker run -p 3306:3306 --name mysql -v ./data/mysql/conf/my.cnf:/etc/my.cnf -v ./data/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest

https://blog.csdn.net/Chen_chenjiasheng/article/details/126946296



docker run -e ES_JAVA_OPTS="-Xms256m -Xmx256m" -e "discovery.type=single-node" -d -p 9200:9200 -p 9300:9300 --name elasticsearch e082d8ac7e5e


docker run --name kibana -e ELASTICSEARCH_HOSTS=http://host.docker.internal:9200 -p 5601:5601 -d kibana:7.16.2



docker nginx部署
https://www.zhuawaba.com/post/84


docker-compose up -d


文件上传七牛云
https://blog.csdn.net/daeiqiu/article/details/128672957



volume

add
from
maintainer
env

run
cmd
entrypoint

