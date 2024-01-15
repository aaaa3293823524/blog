---
title: MyCat学习
tags:
  - 搭建博客
  - 前端
date: 2023-10-29 22:22:44
abbrlink: 8n0la
---
Cobar 基于Java开发  伪装成mysql server

代码重构
bio->nio
group by,order by,limit聚合功能支持

mariadb


TDDL

https://blog.csdn.net/weixin_57128596/article/details/125490529

https://blog.51cto.com/ITEvan/6460007


批量获取，然后存在在内存里面，需要用到的时候，直接从内存里面拿就舒服了！这也就是我们说的 基于数据库的号段模式来生成分布式 ID

数据库的号段模式也是目前比较主流的一种分布式 ID 生成方式。像滴滴开源的Tinyidopen in new window 就是基于这种方式来做的。不过，TinyId 使用了双号段缓存、增加多 db 支持等方式来进一步优化。

Leaf 提供了 号段模式 和 Snowflake(雪花算法) 这两种模式来生成分布式 ID。并且，它支持双号段，还解决了雪花 ID 系统时钟回拨问题。不过，时钟问题的解决需要弱依赖于 Zookeeper



https://zhuanlan.zhihu.com/p/622454317
https://blog.csdn.net/Y_hanxiong/article/details/128063621



泛化调用
https://blog.csdn.net/m0_53157173/article/details/130516238


schema.xml                 作用：定义逻辑库，表、分片节点等内容
server.xml                    作用：定义用户以及系统设置，如端口等.
rule.xml                        作用：定义分片规则。（如果不用分片，无需配置）





客户端向服务器请求资源时，为了减少网络带宽，提高响应时间，服务器一般不会一次将所有资完整的回传给客户端。比如在请求一个网页时，首先会回传该网页的文本内容，当客户端浏览器在解析文本的过程中发现有图片存在的时候，会再次向服务器端发起对该图片资源的请求，服务器将存储的图片资源再发送给客户端。在这个过程中，如果该服务器上只包含网页的文本内容，而没有存储相关的图片资源，而是将图片资源链接到了其他站点的服务器上去了，这就形成了盗链问题。


参数 返回值 没有具体pojo对象 map集合对象装配对象
referenceConfig
GenericService 接口处理所有服务请求
网关服务
测试平台


数据扩容  双写方案平滑迁移




Mycat只能做到分库不分表，和单库分表，不能做到一个库有0-4，另一个库有5-9
dataNode
使用方式添加subTables="t_order$1-2,t_order3"。
目前分表1.6以后开始支持 并且dataNode在分表条件下只能配置一个，分表条件下不支持各种条件的join语句。


subtables rule

maven.test.skip=true




lucene
词典：fst  在内存 压缩率高
倒排表  链表

分段  段不变性 只可读不可写  常驻内存

更新 删除+新增 。de l sdels

中小段合并

tf,length 文档的权重
idf  词的权重

向量空间模型
概率模型
BM25

https://blog.csdn.net/pp3736245/article/details/125503822

ES中倒排索引的压缩算法主要有FOR算法(Frame Of Reference)和RBM算法(RoaringBitMap)
https://www.jb51.net/article/282260.htm


Term Index不需要存所有term，只是一个前缀数，再结合FST压缩技术，存放到内存中。通过TermIndex定位到TermDictionary在磁盘上的block后，在顺序查找磁盘，降低随机读磁盘的次数

FST结构  trie树，合并公共后缀
https://zhuanlan.zhihu.com/p/457746699?utm_id=0


压缩方法有基于磁盘的FOR和基于内存的RoaringBitmap等
联合索引查询 skiplist bitset

如果查询的filter缓存到了内存中（以bitset的形式），那么合并就是两个bitset的AND。
如果查询的filter没有缓存，那么就用skip list的方式去遍历两个on disk的posting list
https://blog.csdn.net/baichoufei90/article/details/111303223

趋势递增
通用唯一识别码

分布式id leaf分析
https://www.jianshu.com/p/55dd21895f39
https://cloud.tencent.com/developer/article/2302654

bizType


DefaultUidGenerator、CachedUidGenerator
tail指针 cursor指针
ringbuffer

Leaf-segment  双buffer
Leaf-snowflake

弱依赖ZooKeeper
除了每次会去ZK拿数据以外，也会在本机文件系统上缓存一个workerID文件。当ZooKeeper出现问题，恰好机器出现问题需要重启时，能保证服务能够正常启动。这样做到了对三方组件的弱依赖。一定程度上提高了SLA。

