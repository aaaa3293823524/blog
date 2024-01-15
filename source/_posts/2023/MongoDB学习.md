---
title: MongoDB学习
tags:
  - 搭建博客
  - 前端
date: 2023-11-01 17:23:35
abbrlink: 8n3oz
---
数据量大
读取写入操作频繁
对事务要求不高（4.2支持事务）

开源 高性能 无模式  nosql
BSON 二进制json   
最像关系型数据库的非关系型数据库

数据库
collection 集合
document 文档


嵌入式文档替代多表连接
_id 自动生成的主键


默认27017端口

use articledb  使用或创建数据库  此时在内存，当放入集合时可在磁盘查到

admin  用户和权限
local   不被复制
config  分片设置


db.dropDatabase()
主要用来删除持久化的数据库

创建集合
显式创建
db.createCollection("mycollection")

隐式创建 插入文档顺便创建集合

删除集合
db.集合。drop()

文档crud
单文档插入 db.集合.insert()   括号内json格式
批量插入 db.集合.insertMany()

查询
db.集合.find() 

db.集合.findOne()  查一条

查询集合
show collections

投影查询（类似mysql select）

文档更新
db.集合.update(query,update,options)

覆盖修改
局部修改   $set
批量修改   options填 {multi:true}
列值增长的修改  $inc  NumberInt(1)

文档删除
db.集合.remove()


文档分页查询
统计查询  db.集合.count(query,options)
分页列表查询   db.集合.find().skip(2).limit(2)
排序    db.集合.find().sort()   -1降序  1升序

文档更多查询
正则   正则表达式是js语法  db.集合.find({字段:/正则/})
比较   $gt $lt  $gte $lte
包含  $in
条件连接  $and  $or

索引  使用B树结构

单字段索引
复合索引
其他索引  地理空间索引（二维索引） 文本索引 哈希索引

索引的管理操作
索引的查看  db.集合.getIndexes()
索引的创建  db.集合.createIndex(keys,options)
索引的移除  db.集合.dropIndex(index)

执行计划
db.集合.find().explain(options)

文章评论
mongodb-driver
springDataMongoDB  封装了mongodb-driver

mongotemplate

副本集  主节点 副本节点  仲裁节点
路由节点


Pageable


亲缘性线程池实现  KeyAffinityExecutor 原理  线程池中套了多个单线程的线程池

https://github.com/PhantomThief/more-lambdas-java

https://developer.aliyun.com/article/903119

docker pull mysql --platform arm64



