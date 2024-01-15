---
title: Dubbo学习
tags:
  - 搭建博客
  - 前端
date: 2021-12-01 22:29:59
abbrlink: 81i5h
---
RPC框架
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222123629105.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222124538588.jpg)

推荐使用zookeeper做注册中心
@Service
@Reference 远程注入
配置项目名称
配置注册中心地址

dubbo高级特性
dubbo-admin管理平台
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211222134056697.jpg)

序列化
地址缓存
超时
重试
多版本
负载均衡
集群容错
服务降级

从系统结构简易程序：springcloud的系统结构更简单、“注册+springmvc=springcloud”，而dubbo各种复杂的Url，protocol，register，invocation，dubbofilter，dubboSPI，dubbo序列化..........炫技的成分更多一些

从性能：dubbo的网络消耗小于springcloud，但是在国内95%的公司内，网络消耗不是什么太大问题，如果真的成了问题，通过压缩、二进制、高速缓存、分段降级等方法，很容易解

dubbo的神坑是jar包依赖，开发阶段难度极大

dubbo的改进是通过dubbofilter



从整个大的平台架构来讲，dubbo框架只是专注于服务之间的治理，如果我们需要使用配置中心、分布式跟踪这些内容都需要自己去集成，这样无形中使用dubbo的难度就会增加。Spring Cloud几乎考虑了服务治理的方方面面，更有Spring Boot这个大将的支持，开发起来非常的便利和简单。

