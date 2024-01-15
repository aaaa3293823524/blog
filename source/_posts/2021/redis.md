---
title: redis
tags:
  - 搭建博客
  - 前端
date: 2021-11-05 22:14:18
abbrlink: 80p92
---

redis设计与实现


G1垃圾回收器的原理：
8.binlog有哪些
9.ip协议的划分

关于项目：
数据库的设计
session机制的时间设置，会不会过期

哈希表扩展与收缩 rehash


压缩列表  ziplist

大部分情况跳跃表和平衡树效率差不多 但实现简单
zskiplistnode
zskiplist 节点数量 头节点   尾节点
层  前进指针    跨度
后退指针
节点按分值从小到大排序
节点成员对象

多个跳跃表节点组成一个跳跃表

压缩列表是列表键和哈希键底层实现
小整数  短字符串
节约内存  特殊编码 连续内存块 顺序形数据结构
包含任意多个节点 每个节点可保存一个字节数组或一个整数值
zlbytes zltail  zllen

previous_entry_length  记录前1个节点长度
1字节或5字节

尾部向前遍历

encoding   记录节点content属性保存数据类型和长度
00   01 10 字节数组
11  整数

redisServer
服务器中数据库  db数组
初始化服务器  dbnum决定应创建多少个数据库

切换数据库  select

redisClient db属性记录客户端当前目标数据库 指针

数据库键空间  dict字典保存所有键值对 字典称为键空间

watch命令监视某个键  脏 修改

ttl   setex  expire  expireat    persist
pttl
expires字典保存数据库所有键过期时间
键是指针指向某个数据的键
值是过期时间

定时删除   定时器  cpu不友好
惰性删除    内存不友好
定期删除   难点是时长和频率
实现

RDB持久化
bgsave  save  实现
生成rdb文件    压缩二进制文件
载入rdb文件
启动redis时 开启rdb功能会载入rdb文件   分主从
rdb保存键值对  aof保存写命令
rdb文件结构
AOF持久化
实现  命令追加  文件写入  文件同步
aof文件重写实现

去除冗余浪费空间的命令 读取服务器当前数据库状态实现
优先aof
bgrewriteaof
aof写入
aof重写

aof缓冲区
aof重写缓冲区
aof后台重写

持久化可以手动执行也可以根据服务器配置定期执行

事件
客户端
服务器
复制
Sentinel  高可用   sentinels字典   监视  主观下线  客观下线
命令连接  订阅连接
每秒10次发送INFO命令   
ping   指定时长连续发送无效回复认为主观下线
集群
分布式数据库方案 通过分片进行数据共享  提供复制和故障转移功能
cluster meet  连接节点   握手
集群数据结构
clusterNode 保存节点当前状态 
重新分片  redis-trib 将属于某个槽的所有键值对从一个节点转移至另一个节点
事务

单线程实现简单  基于内存操作 瓶颈是内存和网络带宽
单线程指的是处理客户端发送的请求命令的文件处理器模块是单线程，其他模块不一定是单线程的

优点：
锁  上下文切换

Redis采用单线程的劣势:
1.无法充分发挥多核机器的优势，不过可以通过在机器上启动多个Redis实例来利用资源。（但是启动多个Redis实例可能会导致在进行AOF重写时，竞争IO资源，导致磁盘写入压力过大，所以可以使用脚本来触发实例的AOF重写，让所有实例的 AOF 串行执行。）

SDS会使用空间预分配和惰性空间释放


非阻塞：  不断询问

I/O复用指的是多个I/O连接复用一个进程

epoll是对select和poll的升级版，解决了很多问题，是线程安全的，而且可以通知进程是哪个Socket连接有I/O事件,不需要进行全部连接进行遍历，提高了查找效率。

epoll和select/poll最大区别是

(1)epoll内部使用了mmap共享了用户和内核的部分空间，避免了数据的来回拷贝。 (2)epoll基于事件驱动，epoll_wait只返回发生的事件避免了像select和poll对事件的整个轮寻操作（时间复杂度为O(N)），epoll时间复杂度为O（1）。


发送信号


epoll水平触发和边缘触发的区别？


select/poll  epoll



redis数据结构   字符串  hash list  set zset

在Redis中，字符串有两种存储方式，int编码，embstr编码和raw编码。


在Redis中，字符串有两种存储方式，int编码，embstr编码和raw编码。


hash   ziplist或者hashtable

ziplist     (字符串长度较短且元素个数较少)
元素保存的字符串长度较短且元素个数较少时(小于64字节，个数小于512)，出于节约内存的考虑，hash表会使用ziplist作为的底层实现，ziplist是一块连续的内存，里面每一个节点保存了对应的key和value，然后每个节点很紧凑地存储在一起，优点是没有冗余空间，缺点插入新元素需要调用realloc扩展内存。（可能会进行内存重分配，将内容拷贝过去，也可能在原有地址上扩展）。

hashtable
元素比较多时就会使用hashtable编码来作为底层实现，这个时候RedisObject的ptr指针会指向一个dict结构，dict结构中的ht数组保存了ht[0]和ht[1]两个元素，通常使用ht[0]保存键值对，ht[1]只在渐进式rehash时使用。hashtable是通过链地址法来解决冲突的，table数组存储的是链表的头结点（添加新元素，首先根据键计算出hash值，然后与数组长度取模之后得到数组下标，将元素添加到数组下标对应的链表中去）。


>Java中的列表数据进行缓存时一般是序列化成JSON，以字符串的形式存储在Redis上，而不是使用Redis中的List来进行存储


quicklist   双向链表 链表节点是ziplist

set   元素少  整数数组  元素多 hashtable


zset元素较少用ziplist   元素较多时用skiplist+dict

skiplist+dict
当元素较多时，使用skiplist+dict来实现。 skiplist存储元素的值和Score，并且将所有元素按照分值有序排列。便于以O(logN)的时间复杂度插入，删除，更新，及根据Score进行范围性查找。

dict存储元素的值和Score的映射关系，便于以O(1)的时间复杂度查找元素对应的分值。



>跳跃表理解   (多级索引)

就是单链表的查找的时间复杂度为O(N)，为了提高查询效率，可增加一些索引节点，让查询时间复杂度降低为O(logN)。（只有底层单链表会保存节点数据，上层的节点之后保存几个索引项和分数，也就是向左指向前一个节点的索引，向右指向后一个节点的索引，向下指向上一级的索引。）

时间复杂度的推理过程可以认为，从每一级索引中两个节点中选一个节点作为下一级索引的节点，让下一级索引的节点数量为本级索引节点数量的一半。假设原始链表的长度为n，第一级索引节点个数为n/2,第二级为n/4，一直到最高层。


要原因是因为作为一种动态的数据结构，其删除和添加的节点是不可预测的，而跳跃表又不能像平衡二叉树那样，可以通过染色或者旋转来维持平衡，如果严格按照两个节点之间建立一个索引，在删除和添加节点时，需要更新的索引太多了。所以在这种情况下，就需要一种概率随机化的方式来自动均衡跳跃表的多级索引，通过这种方式虽然不能完全保证跳跃表的均匀性，但总体上可以使得跳跃表趋于平衡，从而能够达到较高的综合性能。


时间复杂度

所以每一层最多遍历的节点数是<=3,这是由于每一层索引节点数是上一层的节点数的一半来得到的，每两个节点的区间，在上一层中都是两个区间，就是第三层的 1  5区间对应上一层的1  3 区间和3  5 区间。
所以时间复杂度=总层数*每层遍历节点数=3logN,去掉常数后是log(N)
空间复杂度 1/(1-p)



从内存占用上来说，skiplist比平衡树更灵活一些。一般来说，平衡树每个节点包含2个指针（分别指向左右子树），而skiplist每个节点包含的指针数目平均为1/(1-p)，具体取决于参数p的大小。如果像Redis里的实现一样，取p=1/4，那么平均每个节点包含1.33个指针，比平衡树更有优势。



每一次IO读取的数据我们称之为一页(page)
具体一页有多大数据跟操作系统有关，一般为4k或8k，innodb中一页是16K。)


>因为每个节点有多层前进指针，首先取第一个节点的最上层的前进指针level[i]，比较指针level[i]跳转到的节点的score与查找的score的大小

如果大于，那么说明要查找的score就处于当前节点与当前的level[i]跳转的节点之间，不能跳转，直接下降一级，取level[i-1]的指针进行判断。如果level[i-1]是最下面的一层，也就是单链表的指针，那么就直接向后进行遍历查找，直到找到这个score或者第一个大于这个score的值(也就是范围查找的左边界)。

如果小于，说明说明要查找的score就处于当前节点与当前的level[i]跳转的节点的后面，跳转后，取跳转后的节点进行这个判断。



![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210213345813.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210213646261.jpg)

## 持久化
RDB   写时复制  共享内存    备份  快速重启
save阻塞

bgsave非阻塞

flushall

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210220946752.jpg)

AOF
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210221246117.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210222737692.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210223018718.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210223236925.jpg)
redis-check-aof --fix  修复aof文件

发布订阅  主从复制  哨兵模式
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210224120960.jpg)

单个主机单点故障

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210224659439.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210224857834.jpg)
slaveof no one

哨兵模式原理
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210225029138.jpg)

哨兵故障
多哨兵模式   奇数节点
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210225310267.jpg)
主观下线
客观下线
选哨兵领导

队列offset

选offset大的 比较新
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211210225850095.jpg)

全量复制
部分复制

集群cluster
