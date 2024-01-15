---
title: Prometheus监控搭建
tags:
  - 搭建博客
  - 前端
date: 2023-11-14 22:14:50
abbrlink: 8nid2
---
zabbix

exporter  配置采集的数据库信息

回想一下Skywalking是怎么做的，SkyWalking有客户端和服务端，需要在目标服务上安装探针（agent），探针采集目标服务的指标数据，上报给服务端OAP服务，这个对目标有一定的侵入性，不过可以接受。Prometheus不需要探针，可以借助push gateway来实现push效果

TSDB
brew install prometheus

/opt/homebrew/Cellar/prometheus/2.47.2

/opt/homebrew/etc/prometheus.yml
```
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
    - targets: ["localhost:9090"]
```


./prometheus --config.file=/usr/local/etc/prometheus.yml

brew services start prometheus


localhost:8080/metrics


brew install grafana

/opt/homebrew/Cellar/grafana/10.1.1

grafana-server --config=/usr/local/etc/grafana/grafana.ini --homepath /usr/local/share/grafana --packaging=brew cfg:default.paths.logs=/usr/local/var/log/grafana cfg:default.paths.data=/usr/local/var/lib/grafana cfg:default.paths.plugins=/usr/local/var/lib/grafana/plugins




如需修改默认端口，可修改/opt/homebrew/etc/grafana/grafana.ini 这个文件)，默认用户名/密码，都是admin，使用前必须更改密码


brew services start grafana


https://grafana.com/grafana/dashboards/7362-mysql-overview/

https://prometheus.io/download/#mysqld_exporter


Apollo  -Dserver.port 
8070
8080
8090

nacos配置中心

远程热部署原理

CompletableFuture
runAsync
thenCompose CompletionStage
AllOf
AnyOf
get
getNow
whenComplete   BiConsumer 接收2个参数 返回值，异常 回调
exceptionally
complete   超时设置结果
cancel

StampedLock
不可变的累加器对象设计

Disruptor

gfs mapreduce bigtable

平衡二叉树
memtable  sstable 压缩，合并
tiering leveling

分布式文件系统
大规模，可扩展，适配大文件
文件分为一个个chunk来存储，64MB  大chunk
节省网络开销
减少chunk数量

分割存储   分散存储在多台服务器上
大文件存储（几个GB）
chunkserver

自动扩缩容
文件位置等信息  元数据

文件名  chunk编号
文件到chunk映射

master  控制流经过master 数据流不经过master

client会缓存master中元数据

GFS高可用设计
master高可用
primary master   同步WAL(write ahead log)
shadow master
记录日志

Chuby
chunk高可用
chunk副本

GFS读写流程
改写和追加
存储与计算解耦


得物异地多活
https://www.cnblogs.com/crazymakercircle/p/17227789.html


安卓模拟器
https://blog.csdn.net/iYNing/article/details/129314021

apollo ReleaseMessage

skywalking支持grpc,dubbo
pinpoint 收集数据比较多 性能比较差
zipkin
CAT 有侵入性 报表丰富

RocketBot 服务 端点 实例
skywalking常用插件
配置覆盖
系统配置
探针配置
系统环境变量配置
覆盖优先级 探针配置>系统配置>系统环境变量配置>配置文件值
Trace工具包  追踪id
过滤指定端点 skywalking.trace.ignore_path
告警   webhook接口
指标对比
OpenTracing