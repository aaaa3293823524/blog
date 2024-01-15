---
title: springsecurity学习
tags:
  - 搭建博客
  - 前端
date: 2023-11-22 00:40:55
abbrlink: 8nq94
---

springSecurity不是基于一些filter来实现的嘛，但是@ControllerAdvice只能拦截到控制器的异常，filter中的异常时拦截不到的，所以还是建议用springSecurity内部的异常处理的机制，springSecurity会抛出两大类异常，一个是AuthenticationException（认证的异常）,一个是AccessDeniedException（权限不足的异常），处理的方法时写两个类，一个继承AccessDeniedHandler接口，一个继承AuthenticationEntryPoint接口，然后在springSecurity的配置类configure(HttpSecurity httpSecurity)中配置刚刚写的这两个类，httpSecurity.exceptionHandling().accessDeniedHandler({实现了AccessDeniedHandler接口的类}).authenticationEntryPoint({实现了AuthenticationEntryPoint接口的类})








gradle各版本下载

https://www.nowcoder.com/discuss/458013033286189056


一个线程oom,其他线程还能运行吗

Elasticsearch源码解析与优化实战


https://code84.com/55990.html


-Des.path.home=/Users/zhangxuefeng/Downloads/eshome
-Des.path.conf=/Users/zhangxuefeng/Downloads/eshome/config
-Xms1g
-Xmx1g
-Dlog4j2.disable.jmx=true
-Djava.security.policy=/Users/zhangxuefeng/Downloads/eshome/config/elasticsearch.yml


https://blog.csdn.net/qq_33890670/article/details/108510923


架构驿站


![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-25_17-42-47.png)



https://gitee.com/xieqk/Bilibili_Spider_by_UserID



ConcurrenSkipListMap

写稀疏索引 内存映射   MappedByteBuffer
写log   fileChannel

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-26_14-30-52.png)



chrome://net-internals/#sockets

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-27_23-59-07.png)


![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_00-52-37.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_11-12-15.png)


idea类图 ctrl alt shift u
https://www.cnblogs.com/imsoft/p/6972612.html

idea recent files
ctrl+e  
idea 子类实现方法
ctrl alt b
idea 变量引用
ctrl alt f7

ctrl+f12，快速查看Java类中的结构



![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_14-23-40.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_15-29-44.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_15-42-19.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_15-45-33.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_15-46-35.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_16-02-08.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_16-06-11.png)


![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_16-18-43.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-28_20-17-58.png)



https://blog.csdn.net/weixin_42687829/article/details/86751174

查询出口IP地址
curl cip.cc


-Drocketmq.namesrv.addr=127.0.0.1
export NAMESRV_ADDR=127.0.0.1:9876


![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-29_19-26-24.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-29_19-18-22.png)

netty设计模式
单例模式  https://blog.csdn.net/weixin_43004044/article/details/131611315
ReadTimeoutException
MqttEncoder
策略模式
chooser
装饰者模式
WrappedByteBuf及子类
观察者模式
channelFuture promise
addListenner
迭代器模式
CompositeByteBuf 零拷贝

责任链模式
pipeline

netty高并发性能调优
单机百万连接调优     突破局部文件句柄限制  突破全局文件句柄限制
netty应用级别性能调优

ulimit -n 一个进程能打开最大文件数
/etc/security/limits.conf
vagrant
![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-29_21-41-36.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-29_21-48-18.png)


![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-29_23-12-30.png)


全链路异步


https://www.jianshu.com/p/97654045a68e

https://archive.apache.org/dist/hadoop/common/

macos编译Hadoop
https://blog.csdn.net/sinat_41679123/article/details/89449259



RocketMQ实战与原理解析

Elasticsearch实战与原理解析


电子书
https://github.com/qingpiaodeyanshen/pdf


dubbo3新特性
https://mikechen.cc/25713.html


jdk spi约定
![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-30_12-18-27.png)
ServiceLoader

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-30_12-23-46.png)

extensionLoader objectFactory

ExtensionFactory  Protocal
ServiceConfig
@Adaptive注解   
loadFile


# 动态编译
javassistCompiler
jdkCompiler
javassist字节码编辑工具

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-11-30_22-15-56.png)
# 服务发布
暴露本地服务
暴露远程服务
启动netty
打开zk
到zk注册
监听zk
![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-01_00-03-14.png)

exporterMap InJvmExpoter DubboExpoter(key带端口)

exchanger信息交换层
Transpoter网络传输层
![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-01_01-32-38.png)

NettyTranspoter
NettyServer
HeaderExchangeServer  内部有心跳定时器,采用线程池,如果断开就心跳重连
# 服务引用

urlInvokerMap
# 集群容错
![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-01_21-37-23.png)
Directory 目录服务 RegistryDirectory(静态目录服务.Invoker固定)  RegistryDirectory(注册目录服务,Invoker集合数据来源于zk注册中心)
methodInvokerMap(数据的来源,同时也是notify的重要操作对象)

router路由规则
灰度发布
启动路由规则触发哪些动作
a.什么时候加入ConditionRouter
b.ConditionRouter怎么过滤的
路由规则实现类
ConditionRouter  条件路由  后台管理的路由配置都是条件路由
ScriptRouter 脚本路由
MockInvokersSelector
Cluster集群
FailoverCluster.join 
![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-01_22-25-31.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-01_22-26-47.png)

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-01_22-28-34.png)

服务降级
容错 fail:return null
屏蔽 force:return null
MockClusterInvoke

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-01_23-11-10.png)
# 网络通信




netty时间轮(HashedWheelTimer)源码分析

MappedFile
https://blog.csdn.net/Wengzhengcun/article/details/131223994


writeAndFlush