---
title: java的IO学习
tags:
  - 搭建博客
  - 前端
date: 2021-12-04 22:52:09
abbrlink: 81li4
---
通信
![](https://s2.loli.net/2021/12/04/JAT2dajlZfVNOvb.png)

![](https://s2.loli.net/2021/12/04/1o3RkCYTGP7AmyU.png)

![](https://s2.loli.net/2021/12/04/d4zgojXVJNrxbsn.png)

![](https://s2.loli.net/2021/12/04/3ZyxsvAGkb8h6aU.png)


java.io
BIO多发多收   任意类型文件上传    端口转发

java.nio
NIO   面向缓冲区  基于通道

直接与非直接缓冲区    直接内存

NIO三大核心


Selector



linux 5种io模型
阻塞式I/O模型(也就是BIO，Blocking IO) 如果当前内核中数据没有准备好，那么会让出CPU时间片，一直阻塞等待，不会进行其他操作。直到内核中的数据准备好

非阻塞时I/O模型  当该数据未到达的时候，进程会不断询问内核，直到内核准备好数据。 

I/O多路复用模型
基础版的I/O复用模型
select和poll

epoll 基于事件 水平触发  边缘触发

信息驱动式I/O模型  内核准备好数据后，会给用户态发送一个信号

异步I/O模型   内核准备好数据后  在数据从内核态拷贝到用户空间之后，内核才通知用户态进程来处理数据