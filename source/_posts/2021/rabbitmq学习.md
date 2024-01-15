---
title: rabbitmq学习
tags:
  - 搭建博客
  - 前端
date: 2021-12-01 22:22:02
abbrlink: 81i5a
---
应用解耦   提升容错性和可维护性
异步提速   提升吞吐量
削峰填谷   提高系统稳定性

可用性降低
复杂度提高   以前同步远程调用  现在MQ异步调用，怎么保证消息不重复  不丢失  顺序正确
一致性问题

容许短暂不一致性

开发语言   erlang
协议    AMQP   高级消息队列协议（网络协议   应用层协议开放标准）

吞吐量   万级                      RocketMQ
消息延迟   延迟最低                Kafka

并发能力强  社区活跃

publisher exchange（路由分发）  routes  queue   consumer

Broker（RabbitMQ  Server）    visual host 逻辑分区
 Binding

建立tcp连接

JMS  java  message server java消息服务应用程序接口  api

15672  5672   25672  集群

生产者

创建连接工厂   ConnectionFactory
设置参数
创建连接 Connection
创建Channel
创建队列   queueDeclare  
发送消息    basicPublish   exchange  简单模式交换机默认
routingkey  路由名称
props  配置信息
body  发送消息数据   字节数组

释放资源
channel.close()
connection.close()

消费者     监听队列
Consumer           DefaultConsumer          收到消息自动执行方法
basicConsume        callback回调对象

不关闭资源

工作模式   6种
简单      一个生产者一个消费者
工作队列     多个消费者竞争   任务较多     提高任务处理速度

发布订阅    一个消息可被多个消费者消费
exchange常见3种    只负责转发  不负责存储
fanout  广播   扇形   发送消息到每一个队列
direct 定向      routing key   路由key
topics 通配符    路由模式      *一个单词     #0或多个
headers    参数匹配 

创建交换机   exchangeDeclare

绑定队列和交换机
channel.queueBind()

Routing
Topics 表达式形式 *恰好1个单词    #0个或多个单词
RPC

springboot与rabbitmq整合  依赖  yml文件  ip  端口   username  password
写配置类   交换机   队列    队列和交换机绑定关系 Binding
ExchangeBuilder    QueueBuilder     BindingBuilder
bind()   to()  with()  
无参数 noargs() 
有参数  and()
生产者    RabbitTemplate
convertAndSend()

消费者
定义监听类    监听队列   @RabbitListener注解

高级特性
消息可靠投递   
confirm   确认模式
开启   setConfirmCallBack

return    退回模式
Consumer Ack


消费端限流


TTL    消息设置过期时间

死信队列     过期消息再利用
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215001530502.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215002016026.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215001833578.jpg)
延迟队列
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215002814702.jpg)

日志与监控


消息追踪
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215003003367.jpg)

应用问题

消息可靠性保障
消息补偿
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215003635892.jpg)

消息幂等性
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215004033802.jpg)
乐观锁
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211215004244719.jpg)

集群搭建
镜像队列

haproxy

采用 RabbitMQ 实战异步写日志与异步发邮件    rabbitmq异步评论通知

场景一：异步记录用户操作日志

消息模型：DirectExchange+RoutingKey 消息模型
消息：用户登录的实体信息，包括用户名，登录事件，来源的IP，所属日志模块等信息
发送接收：在登录的 Controller 中实现发送，在某个 listener 中实现接收并将监听消费到的消息入数据表；实时发送接收



编译插件有什么用
@Qualifier

死信交换机