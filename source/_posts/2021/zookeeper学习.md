---
title: zookeeper学习
tags:
  - 搭建博客
  - 前端
date: 2021-12-01 22:29:17
abbrlink: 81i5h
---
分布式应用程序协调服务
配置管理
分布式锁
集群管理（注册中心）

leader选举  paxos算法
leader follower observer

zoo.cfg
dataDir
server.1=             心跳端口  选举端口
server.2=
server.3=

myid
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222101228620.jpg)
序列化
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222101626751.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222101820370.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222102002325.jpg)

zkCli.sh -server ip

create -s(序列化) -e（临时）   默认非序列化 持久节点
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222105012641.jpg)
delete
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222110331140.jpg) 
quota 日志警告
history redo
watcher
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222111307328.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222111559015.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222111745964.jpg)
集群选举
FastLeaderElection
全新集群   主要看服务器id
非全新集群
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222113628702.jpg)
数据发布与订阅
命名服务  分布式锁
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222113905103.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222114129395.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222114607154.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222114627759.jpg)
序列化

不同节点线程访问
redis分布式锁
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222115713701.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222115942913.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222120348281.jpg)
