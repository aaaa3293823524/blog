---
title: nginx学习
tags:
  - 搭建博客
  - 前端
date: 2023-10-28 20:20:53
abbrlink: 8mzdw
---

高并发 轻量级  web服务器  
反向代理  负载均衡

～  
～*
=
@

http模块
events模块
server location

gzip模块

指令
listen
include
server_name
error_page
index
root

sendfile

gzip
gzip types
gzip_comp_level
gzip_buffers
gzip_disable
gzip_http_version
gzip_min_length
gzip_proxid
gzip-static


expires

add_header

valid_referers

pcre库
rewrite  url重写
set
if
break
return 
rewrite
rewrite_log

域名跳转
域名镜像
独立域名
防盗链   valid_referers $invalid_refer

rewrite常用全局变量

¥http_user_agent

ngx_http_proxy_module 模块
proxy_pass
proxy_set_header
proxy_redirect


proxy_cache

upstream

ssl

动静分离

keepalived

ngx_lua

openrestry


nginx第三方模块



nginx -t
nginx -s reload


后面加斜杠
后面不加斜杠  nginx会做301重定向
server_name_in_direct

$server_port
$host
$1 $2


make&&make intall


nginx负载均衡状态
max_fails fail_timeout
down
backup


nginx用户认证模块


lua nginx扩展模块
local 局部变量
.. 字符串连接
#字符串长度

数值型for循环

泛型for循环
for i,v in ipairs(x) do
    循环体
end



try_files


HttpRedis 
HttpRedis2Module
lua-resty-redis库


lua-resty-mysql
lua-cjson

init_by_lua_block{

}
content_by_lua_block{
  
}


tcp_nopush
tcp_nodelay


brew install nginx
brew services start nginx
/opt/homebrew/etc/nginx/nginx.conf



{
  # 设置Nginx并发处理的worker数量，可以为具体数值，也可以设置为auto
  # 通常建议为节点CPU的核数
  worker_processes auto;
  …
  events {
    # Nginx处理的最大连接数（这里可以进行数据库流控），默认为1024
    # 需根据业务实际运行情况进行调整。
    worker_connections  1024;
  }
  http {
    …
    # 负载均衡默认采用轮询方法
    upstream tomcat_proxy {
      server 172.16.117.100:8889 weight=1;
      server 172.16.117.101:8889 weight=1;
      server 172.16.117.102:8889 weight=1;
    }
    server {
      # 可按IP:Port形式指定Nginx监听地址和端口，默认是在所有地址监听
      # 8086是openGemini ts-sql组件默认的服务监听端口，这里可以修改为其他
      listen 8890;
      # location 后面的斜线‘/’不能少
      location / {
        # 这里的openGemini（可修改）与upstream 后面配置的名称（openGemini）
        # 需保持一致，否则无法转发
        proxy_pass http://tomcat_proxy；
      }
    }
  }
}


ConcurrentLinkedQueue

WebMvcConfigurer


http://localhost:8889/testServlet
http://192.168.0.3:8889/testServlet

java com.example.NIOTomcat

ln -s 软链接

if指令
map指令