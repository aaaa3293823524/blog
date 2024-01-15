---
title: Hadoop环境搭建
tags:
  - 大数据
 
date: 2019-05-25 15:21:40
abbrlink: 792hl
---
三大发行版：apache


三种运行模式
单机
伪分布式
分布式


结构化数据 半结构化数据 非结构化数据
HDFS存储
HDFS以流式数据访问模式来存储超大文件
HDFS块设置
要足够大 将寻址时间减少 数据传输时间占比更大
也不能太大 map任务并行速度会慢

数据容错和可用性
FileSystem类 
文件系统的一致模型

命令行
hadoop fs 

mapreduce分析处理

两个阶段 map阶段和reduce阶段    键值对作为输入和输出
两个函数  map函数和reduce函数

输入分片

jobtracker  tasktracker

namenode datanode

50070   HDFS      8020
8088    yarn
map任务将输出写入本地磁盘

combiner 合并函数  一种优化方案 对map输出进行处理 作为reduce的输入 无法确定其次数

RAID 冗余磁盘阵列

搭建虚拟机

指定虚拟机固定ip


安装eclipse

zookeeper 协调服务

leader选举
znode

posix 可移植操作系统界面


sqoop

Oozie

Hue

Hadoop I/O