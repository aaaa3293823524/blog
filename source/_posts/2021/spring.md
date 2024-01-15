---
title: spring
tags:
  - 搭建博客
  - 前端
date: 2021-11-05 22:00:15
abbrlink: 80p8o
---
基于注解组件扫描
Spring组件扫描和自动织入
spring技术内幕  java nio

bean生命周期等

设计思路，项目架构

java 过滤器  拦截器

多种环境中配置和使用事务处理的能力 提供通用支持
ioc容器强大配置能力 声明事务

aop  事务属性配置和读取 事务对象抽象
事务处理器    数据源事务处理支持
事务管理  并发  数据一致性
事务处理拦截器
编程实现
事务处理器实现


springboot启动过程
构造SpringApplication实例 调用SpringApplication的静态方法run()
调用构造器方法创建出一个SpringApplication实例，在构造器中会确定当前web应用类型，是reactive web类型，还是servlet web类型，还是none类型。以及设置监听器等等，完成一些初始化操作。(监听器就是来监听SpringApplication启动过程的，在开始启动，创建上下文，启动失败等生命周期事件时都会调用监听器相关的方法)

执行实例的run()方法，首先会创建一个StopWatch计时器，来统计run()方法的启动耗时，在日志里面会显示启动时间，那个时间就是在这里统计的。然后处理环境参数，就是java -jar ***.jar启动命令中带的那些jvm参数。

创建applicationContext

执行prepareContext()方法
会调用prepareContext()方法来为应用上下文做一些准备工作，会将运行时的参数封装成bean，注册到beanFactory中去，以及使用load方法加载启动类


执行refreshContext()方法
动容器，也就是会为beanFactory做很多配置，注册BeanPostProcessors，设置类加载器等等。在这一步也会解析启动类中@SpringBootApplication这个组合注解。

afterRefresh()方法
这个方法里面会把容器里面所有ApplicationRunner自定义子类和CommandLineRunner自定义子类的Bean全部取出来，执行它们的run()方法。(就是有时候如果需要在应用启动后执行一些我们自定义的初始化操作，可以通过自定义一个类，继承ApplicationRunner类来实现。)

之后会调用listeners.started()方法，通知所有Listener，application已经启动完成了，以及调用listeners.running()方法通知所有Listener，application已经运行了。

C和A是无法同时做到。所以一般对于数据一致性要求特别高的业务，例如支付，交易相关的业务，就是会优先保证一致性C和分区容错性P，就是保证数据一致性，例如让所有子节点都收到更新后才算提交成功，就像MySQL主从同步中的全同步模式一样。普通的业务是优先保证可用性A和分区容错性P，比如在MySQL主从同步时，默认就是异步的方式，我们执行一条更新SQL，只需要主节点更新成功就行就对事务进行提交，不需要等待从节点更新数据成功，主节点会异步把SQL发送给从节点。


客户端向zookeeper从节点发送读请求，节点会直接从数据库中找到这个节点的数据然后返回。

客户端向zookeeper从节点发送写请求，节点会将znode路径和数据转发到leader节点，leader会将写请求转换为proposal提案，并且分配一个事务ID zxid，将这个proposal放到每个节点的队列（主节点会给每个从节点分配一个专用队列）中去，然后会根据先进先出的策略，将消息发送给从节点，从节点接收到后会将事务写入到磁盘中去，然后返回ACK响应给主节点，当主节点接收到半数以上的从节点的ACK响应后，主节点会认为这个事务提交成功，完成这个事务提交，同时给所有从节点发送commit消息，从节点接收到消息后，会将这条事务提交。

由此看来zookeeper没法保证客户端读取的都是最新的数据，

所有节点都有两个属性，SID：节点ID，zoo.cfg中配置的myid，ZXID：节点当前的最大事务ID 选举的目的就是选目前所有节点中拥有最大ZXID的节点作为Leader，如果拥有的ZXID相同，就选取SID最大的节点作为Leader。
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220115125322064.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220115135654620.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220115205539702.jpg)