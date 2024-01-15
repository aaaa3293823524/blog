---
title: 手写tomcat
tags:
  - 搭建博客
  - 前端
date: 2023-11-08 19:45:15
abbrlink: 8nbkx
---

royal tsx
三台虚拟机
172.16.117.100
172.16.117.101
172.16.117.102

cd /opt/software/SimpleTomcat/out/production/SimpleTomcat/

java com.example.NIOTomcat

sudo systemctl stop firewalld
关闭防火墙

将编译好的项目通过ftp传入虚拟机通过java命令运行程序

nginx配置tomcat地址 实现轮询负载均衡
```
http {
    upstream tomcat_proxy {
      server 172.16.117.100:8889 weight=1;
      server 172.16.117.101:8889 weight=1;
      server 172.16.117.102:8889 weight=1;
    }

    server {
        listen       8890;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            #root   html;
            #index  index.html index.htm;
	    proxy_pass http://tomcat_proxy/testServlet;
        }
    }
}
```


http://localhost:8890


https://mirrors.cloud.tencent.com/apache/