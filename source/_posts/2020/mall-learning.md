---
title: mall-learning
tags:
  - 搭建博客
  - 前端
date: 2020-11-25 13:17:10
abbrlink: 7q1i5
---
mall-learning

spring-security  登录认证   JWT
Swagger-UI
整合SpringTask实现定时任务   （Quartz）
elasticsearch 实现商品搜索

Cron表达式

只需要在配置类中添加一个@EnableScheduling注解即可开启SpringTask的定时任务能力。

Elasticsearch 是一个分布式、可扩展、实时的搜索与数据分析引擎。 它能从项目一开始就赋予你的数据以搜索、分析和探索的能力，可用于实现全文搜索和实时数据统计。

Spring Data Elasticsearch是Spring提供的一种以Spring Data风格来操作数据存储的方式，它可以避免编写大量的样板代码。

mall整合Mongodb实现文档操作

安装Robo 3T(Robomongo)MongoDB可视化工具

mall整合RabbitMQ实现延迟消息

官方手册

Lombok插件   交换机  队列

mall整合OSS实现文件上传    服务端签名后前端直传的相关说明

对象存储    

CORS全称Cross-Origin Resource Sharing，意为跨域资源共享。当一个资源去访问另一个不同域名或者同域名不同端口的资源时，就会发出跨域请求。如果此时另一个资源不允许其进行跨域资源访问，那么访问的那个资源就会遇到跨域问题。


springboot处理校验逻辑两种方式
Hibernate Validator   Vuex

Elasticsearch  DSL语句
Logstash，用于收集日志

RabbitMQ消息模型
![ss](/images/RabbitMQ.jpg)
![dwt2函数](/images/图像融合.jpg)

SpringCloud为开发人员提供了快速构建分布式系统架构的工具，例如配置管理，服务发现，断路器，智能路由，微代理，控制总线，一次性令牌，全局锁定，领导选举，分布式会话，集群状态等。

Spring Boot Admin

Spring Cloud Alibaba：Nacos 作为注册中心和配置中心使用

Spring Boot Admin不仅可以监控单体应用，还可以和Spring Cloud的注册中心相结合来监控微服务应用。

Spring Cloud Security：Oauth2使用入门

单点登录（Single Sign On）指的是当有多个系统需要登录时，用户只需登录一个系统，就可以访问其他需要登录的系统而无需登录。

随着微服务的流行，服务和服务之间的稳定性变得越来越重要。 Sentinel 以流量为切入点，从流量控制、熔断降级、系统负载保护等多个维度保护服务的稳定性。

使用Seata彻底解决Spring Cloud中的分布式事务问题！

Spring Cloud Gateway：新一代API网关服务

Spring Cloud Consul：服务治理与配置中心

Zuul  网关

自动化部署（Jenkins）

Spring Cloud OpenFeign：基于Ribbon和Hystrix的声明式服务调用

Feign是声明式的服务调用工具  Hystrix服务容错 

Ribbon提供负载均衡

Spring Cloud Eureka：服务注册与发现

DockerFile
使用Docker Compose部署SpringBoot应用
写网络结构消融实验部分和conclusion,experiments分析   画图 整合

服务治理
服务注册中心（单节点  高可用） 服务提供者  服务消费者

@EnableEurekaServer

消息代理（RabbitMQ RocketMQ Kafka ActiveMQ）

RESTful API 设计指南
http://www.ruanyifeng.com/blog/2014/05/restful_api.html

缓存的出现加快了数据查询的速度，同时增加了维护成本，建议使用在高频读低频写的数据上。
使用不当可能会出现数据不一致的问题，请谨慎使用。

maven的项目继承依赖

ZooKeeper的安装模式分为三种，分别为：单机模式（stand-alone）、集群模式和集群伪分布模式。

Dubbo是：

一款分布式服务框架
高性能和透明化的RPC远程服务调用方案
SOA服务治理方案

Dubbo提供的注册中心有如下几种类型可供选择：

Multicast注册中心
Zookeeper注册中心
Redis注册中心
Simple注册中心

多提供者多消费者情况   dubbo-admin安装和使用
Dubbo：搭建管理控制台(dubbo-admin)

开源的Dubbo的服务管理控制台是阿里巴巴内部裁剪版本，
开源部分主要包含：路由规则/动态配置/服务降级/访问控制/权重调整/负载均衡等管理功能。

git init 
git add
git commit -m "first commit"
git remote add origin github网址
git push -u origin master