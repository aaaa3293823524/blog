---
title: Netty学习
tags:
  - 搭建博客
  - 前端
date: 2021-11-27 23:08:55
abbrlink: 81dqk
---
NioEventLoopGroup   DefaultEventLoopGroup

服务器端
Chnnel 连接数据通道
ServerBootStrap 启动器 负责组装netty组件 启动服务器
bosseventloop  可连接事件
   workereventloop()    可读事件
   selecter监听io事件 +线程

   ServerSocketChannel实现

   childHandler 决定worker能执行哪些操作
   添加其他Handler    连接建立后执行

   StringDecoder  ByteBuf转换为字符串
   自定义Handler   ChannelInboundHandlerAdapter

   bind() 端口

   accept事件
   read事件
客户端：
StringEncoder   字符串编码为ByteBuf

connect()
.sync()   阻塞方法直到连接建立
.channel()   代表连接对象
.writeAndFlush()   发送数据

经过pipeline加工  流水线

handler处理工序   inbound   outbound  入站 出站

pipeline发布事件传播给handler

事件循环对象
eventloop处理数据的工人      （io时 工人和channel有绑定为了线程安全）   可执行io操作也可进行任务处理 每个工人有任务队列
普通任务  定时任务   底层单线程线程池
继承ScheduledExecutorService     OrderedEventExecutor

按照pipeline顺序 按照handler规划处理数据

事件循环组   register方法
创建事件循环组   获取下一个事件循环对象   执行普通任务    异步处理   
 定时任务  scheduleAtFixedRate  延时  分隔时间
 ![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220112131421341.jpg)
 处理io事件
boss  只负责 serversocketchannel accept事件  
 worker只负责 socketchannel 读写
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220112135510494.jpg)
 ctx.fireChannelRead()  让消息传递给下一个handler

eventloop切换线程（handler执行过程中换人）


ChannelFuture对象    sync() 同步处理结果  阻塞住当前线程  直到nio线程连接建立完毕
addListener （回调对象）    异步处理结果     ChannelFutureListener

connect方法  异步非阻塞  main发起调用  真正执行connect是nio线程

channel.close()   异步操作            关闭之后的操作
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220112141051586.jpg)
获取ClosedFuture对象    channel.closeFuture()   同步处理关闭  sync()
异步处理关闭    ChannelFutureListener

多线程   异步   响应时间增加  吞吐量提高  单位时间内处理请求速度
合理任务拆分

Netty  Future接口继承 jdk中Future    

Promise继承    Netty  Future接口

jdk中Future 同步等待任务结束    cancel 取消  isDone  任务是否完成，不区分是否失败    get获取任务结果，阻塞等待
Netty  Future    同步  异步   都要等任务结束    await不抛异常   isSuccess判断任务是否成功     sync抛异常
Promise    脱离任务独立存在    作为线程间传递结果的容器   setSuccess   setFailure 

Future  Promise  和异步方法配套使用  用来处理结果

DefaultPromise   主动创建promise  结果容器

handler处理channel上的事件   
入站处理器   channelinboundhandlerAdapter子类  读取客户端数据 写回结果
出站处理器   channeloutboundhandlerAdapter子类   对写回结果进行加工     从tail逆序
pipeline.addLast()       head   tail    双向链表

eventloopgroup  shutdownGracefully

embedded-channel   用来测试的channel

bytebuf创建   对字节数据的封装 ByteBufAllocator.DEFAULT.buffer()   容量可动态变化

writeBytes()   getBytes()
直接内存   读写效率高   directBuffer  适合配合池化   Netty默认直接内存
堆内存   分配效率高   heapBuffer

池化     重用ByteBuf  内存分配算法提升分配效率
非池化
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220112145839169.jpg)

组成
容量  最大容量    最开始读写指针都在0位置
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220112150912508.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220112151206445.jpg)
写入
网络编程   大端 writeInt()（先写高位  再写低位 网络编程一般大端）   小端   writeIntLE()
CharSequence

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220112151437892.jpg)
读取    readByte()   1次读取1个字节
读取int整数5   先标记    markReaderIndex()
重复读取  reset

内存释放   retain +1 release  -1    
unpooledheapbytebuf   jvm内存   GC回收
unpooledDirectbytebuf   需特殊方法回收内存
pooledbytebuf  更复杂规则回收

引用计数   ByteBuf实现ReferenceCounted接口   计数为0内存回收

谁是最后使用者  谁负责release

头尾释放源码

slice  零拷贝体现之一    减少数据复制   切片   单独读写指针   setByte()
 
duplicate   零拷贝体现之一   截取原始ByteBuf所有内容    单独读写指针

copy  深拷贝

channelActive 连接建立成功后触发

双向通信   java socket全双工  读线程  写线程

粘包半包   服务器接收缓冲区小  半包   确认应答  滑动窗口
Nagle算法   会造成粘包         接收方ByteBuf设置过大

MSS限制   超过切片   半包    MTU

TCP流式协议，消息无边界

解决   短连接    childOption 调整netty缓冲区（ByteBuf）   效率低 能解决粘包  不能解决半包

固定长度解码器    空间浪费

分隔符确定边界   LineBasedFrameDecoder    \n   \r\n    换行符   设定最大长度   行解码器      效率比较低
DelimiterBased

LTC解码器   LengthFieldFrameDecoder   告诉内容有多长    回车13  换行10  消息不够紧凑

协议设计与解析  redis协议  http协议

netty提供了协议   HttpServerCodec()  编解码器结合  请求解码  响应编码   HttpRequest   HttpContent   SimpleChannelInboundHandler
DefaultFullHttpResponse

自定义协议   
魔数 第一时间判断是否是有效数据包
版本号   支持协议升级
序列化算法   消息正文  json  protobuf  hession   jdk
指令类型
请求序号  双工通信  提供异步能力
正文长度



netty进阶

netty优化   扩展序列化算法

高性能序列化协议protobuf

Netty心跳机制

直接内存与Netty零拷贝


Socket与文件描述符

Socket与Tcp协议、Http协议的关系



Netty之Http协议开发

Netty之WebSocket协议开发


