---
title: Netty框架学习
tags:
  - 搭建博客
  - 前端
date: 2020-12-22 17:31:45
abbrlink: 7qvp7
---
多线程和网络编程    Reactor模式   通信  java内存模型  并发编程
同步 （需要1个额外线程询问是否完成）
阻塞  客户端：IO线程=1：1    
非阻塞  客户端：IO线程=M：1  
BIO(同步阻塞I/O)

AIO(异步非阻塞I/O)

NIO（New I/O）

Selector   多路复用
ByteBuffer  SocketChannel ServerSocketChannel
Hadoop RPC框架avro使用Netty作为底层通信框架

Netty入门

TCP 粘包/拆包问题解决之道

分隔符和定长解码器应用

**搭建Netty开发环境**
>[Netty官网](https://netty.io/)

读半包问题

Netty编解码功能

java序列化   Java对象   字节数组   Serializable接口

HTTP协议   UDP协议   WebSocket协议   文件传输

字典树