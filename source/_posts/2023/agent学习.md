---
title: agent学习
tags:
  - 搭建博客
  - 前端
date: 2023-11-12 01:30:19
abbrlink: 8nf6i
---
java探针

arthas-agent启动的逻辑比较简单，使用Java Agent原理在应用启动前或者应用运行时将Instrumentation作为参数传递给ArthasBootstrap类的getInstance方法，通过自定义的加载器ArthasClassloader加载ArthasBootstrap类，利用反射的方式调用ArthasBootstrap类的getInstance方法。

https://zhuanlan.zhihu.com/p/617498975

https://zhuanlan.zhihu.com/p/476317425

Java agent本质上可以理解为一个插件，该插件就是一个精心提供的jar包。只是启动方式和普通Jar包有所不同，对于普通的Jar包，通过指定类的main函数进行启动。但是Java Agent并不能单独启动，必须依附在一个Java应用程序运行，在面向切面编程方面应用比较广泛。

可以在加载java文件之前做拦截把字节码做修改
可以在运行期将已经加载的类的字节码做变更
比如我们用到过的Jcoco，Arthas, chaosblade等，都是使用Java agent技术来实现的。

jvm 参数形式： 调用 premain 方法
attach 方式： 调用 agentmain 方法


java Instrument

自Jdk5开始，就引入了 Java Instrumentation，它可以通过 addTransformer 方法设置一个 ClassFileTransformer，可以在这个 
ClassFileTransformer 实现类的转换

jdk5提供的Instrumentation 是静态的，基本思路就是在java程序启动前去加载一个代理（javaagent），这个javaagent是一个jar，然后需要编写
一个premain() 方法，然后记录在MANIFEST.MF中，在运行main()方法前，会先运行premain()方法里的逻辑
整个代理的过程基本是：先将代理类打成一个jar，然后在主程序中加上 -javaagent 的参数，参数的值是代理jar的全路径
https://blog.csdn.net/qq_30468551/article/details/121023416


ClassVisitor
Classwriter
ClassReader

jaeger
zipkin
skyWalking
openTelemetry
上报java应用数据
https://www.alibabacloud.com/help/zh/arms/tracing-analysis/use-skywalking-to-report-java-application-data

InfluxDB  时间序列数据库
指标名+标签

应用监控所有实例某个指标做聚合计算，如某个接口的请求量，一次聚合涉及指标数量高达十几万个，高基数查询，InfluxDB不支持，选择clickhouse存储指标数据
分布式列式数据库 sql语言 丰富的数据处理函数 可以完成很多指标处理 P95 完备集群方案
clikhouse不支持自动删除过时数据，而且增加新tag要修改表结构

分布式应用监控系统CAT

公共日志服务平台CLog

灾备 故障演练  验证业务容灾和恢复能力

单元化部署   解决跨区域多活一种主要思路，需要投入额外的硬件资源

保证复制实时性
库级并行复制
组提交并行复制
基于writeset并行复制

双向复制解决循环复制  GTID uuid标记数据来源

压测流量构造方式
流量回放  流量构造
Jmeter LoadRunner

隔离环境  生产环境

全链路压测  数据隔离 影子库
清理脏数据
通过不断失败来验证失败  混沌工程

AIops  智能运维

故障定级



监控主从延迟 pt-heartbeat

Galera 协议

缓存命中率  缓存回收策略


Apollo  3个jar包 依赖mysql  需要2个数据库
configService
adminService
portal   控制台  用户名apollo 密码admin


userId entityType entityId  entityUserId
 
uv hyperloglog
dau bitmap

添加评论 过滤敏感词 存入mysql 更新帖子评论数量 异步同步es redis帖子分数

点赞  set   数量size 事务 点赞状态isMember
关注  用户关注实体 zset  实体拥有的粉丝 zset 事务  zcard数量

关注列表
分页查询评论
评论个数
查询某个用户的评论/回复数量


置顶加精删除
帖子热度计算

updateStatus 0正常 1精华 2拉黑
updateType 0普通 1置顶

评论盖楼  回复帖子楼层加1


----------------------
centos安装es6
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.tar.gz

groupadd elsearch           
useradd elsearch -g elsearch -p elasticsearch
chown -R elsearch:elsearch  elasticsearch-6.3.0
su elsearch

端口映射
ssh -L 9000:172.16.117.100:9000 root@172.16.117.100


解决es内部netty冲突

@EnableScheduling

https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter/2.3.4.RELEASE




本地缓存load  reload区别  async区别


npm uninstall vue-cli -g
npm install -g @vue/cli@3.6.0
