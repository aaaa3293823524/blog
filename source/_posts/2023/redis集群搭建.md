---
title: redis集群搭建
tags:
  - 搭建博客
  - 前端
date: 2023-11-09 23:02:29
abbrlink: 8ncue
---

yum install gcc-c++ -y

wget https://download.redis.io/releases/redis-6.2.4.tar.gz

tar xzf redis-6.2.4.tar.gz

cd redis-6.2.4

make MALLOC=libc

cd src

./redis-server &

./redis-cli



./src/redis-server redis.conf


编辑redis.conf
```
protected-mode no
bind 0.0.0.0
```

垂直扩容  恢复时间长
水平扩容 丢数据
拆分扩容
xpipe

keeper 减少master全量同步
metaServer管理keeper   元信息管理

双向复制
CRDT  多活一致性解决方案
全量状态  数据结构支持结合，交换，幂等
状态转换成操作  交换

CDN静态加速
CDN动态加速
CDN动态域名切换

动态数据源

单机多应用  请求domain，path

SLB 软负载  基于nginx conf
用户绝大多数操作会转化为对Group对象操作
多版本化，操作日志，两阶段提交机制
更新 激活  生效
减少用户操作风险，多次变更，一次生效减小SLB压力

QMQ  Hermes

健康检测
配置中心

sql server
hbase
tidb

ddl 表创建 表结构调整 索引调整

gh-ost工具  表结构字段发布

OPDB运维数据库  表记录运维监控数据，通过存储过程记录速查命令 定位问题

perfcormancea_schema 语句性能数据


速度快，风险小发布方式
蓝绿部署，滚动部署，金丝雀发布
暗部署，重建部署
第一代Croller
第二代Tars发布系统




useradd elsearch
chown -R elsearch:elsearch elasticsearch-6.2.4/


vim /etc/sysctl.conf
一个进程创建内存映射最大数量
vm.max_map_count=655360

sysctl -p



vi /etc/security/limits.conf


sudo ifconfig tun0 down

磁盘扩容
fdisk -l
fdisk /dev/nvme0n1
mkfs.ext4 /dev/nvme0n1

mkdir /app
echo "/dev/sdb1 /app ext4 defaults 0 0" >> /etc/fstab

mount -a
df -h

dmsetup status
dmsetup remove_all
mke2fs -t ext4 /dev/nvme0n1p2

vgdisplay

pvcreate  /dev/nvme0n1p2
vgextend cl_fedora /dev/nvme0n1p2
https://blog.51cto.com/u_11451960/2520531




