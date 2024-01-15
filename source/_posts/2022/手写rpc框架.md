---
title: 手写rpc框架
tags:
  - 搭建博客
  - 前端
date: 2022-01-11 18:24:21
abbrlink: 82rio
---

https://blog.csdn.net/qq_41373246/article/details/100009385

https://dalin.blog.csdn.net/article/details/107805105?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=2



点赞功能
https://blog.csdn.net/weixin_45862170/article/details/116139362


tcp_keepalive_time默认是2个小时，也就是TCP空闲连接可以存活2个小时，在close_wait状态下，可以把这个时间调小，减少处于close_wait连接的数量

net.ipv4.tcp_syncookies = 1 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；
net.ipv4.tcp_tw_reuse = 1 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；
net.ipv4.tcp_tw_recycle = 1 表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭。
net.ipv4.tcp_fin_timeout 修改系默认的 TIMEOUT 时间


负载均衡

一致性hash

限流


分布式id   
uuid 通用唯一标识符（16个字符 空间占用多）
数据库主键自增 （数据泄露）
redis自增（使用内存，并发性能高  数据丢失 数据泄露）
雪花算法（缺点 时钟回拨）
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113125324010.jpg)

分布式锁
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113125552953.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113130304988.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113130426864.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113130828119.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113131153868.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113134747315.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113134949450.jpg)
分布式事务
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113135200606.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113135449787.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113140055297.jpg)

can commit
pre commit
do commit
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113140311740.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113140528783.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113141033971.jpg)
TCC
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113141139416.jpg)

TCC空回滚
幂等
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113153500701.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113155301763.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113160017090.jpg)

悬挂
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113153854100.jpg)
可靠消息服务
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113154637453.jpg)
最大努力通知
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113155136943.jpg)
zab协议

自动装配  starter

springmvc 9大内置组件

消息队列

submit和execute区别
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113152226073.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113153203975.jpg)

client(动态代理类)先动态生成一个对象，表示一个client对象。然后这个client对象调用接口的方法A，方法A一般就是我们需要的服务，然后通过某种机制，方法A的真正调用会发生在server端，server将调用完方法A后，会得到相应的结果，将结果返回给client。那么client和server的一次交互就完成了。整个过程下来，client端申请调用，而server端真正执行调用，最后server端将调用产生的结果返回给client。这样有什么好处呢？客户端一般就是申请服务，如计算服务，而真正的计算的过程会交由服务端进行（理论上服务端的计算资源可以无限大——如集群模式）。典型的hadoop的底层通信框架RPC原理就是如此。

服务端反射调用服务实现者

客户端动态代理（InvocationHandler中向服务端发送函数名和参数列表）
其中涉及序列化和反序列化 网络通信

zookeeper做注册中心  负载均衡

Nacos服务分级存储模型
NacosRule负载均衡
命名空间隔离环境
临时实例宕机时，会从nacos的服务列表中剔除，而非临时实例则不会

Nacos集群默认采用AP方式，当集群中存在非临时实例时，采用CP模式；Eureka采用AP方式

建议将一些关键参数，需要运行时调整的参数放到nacos配置中心，一般都是自定义配置

流控效果



