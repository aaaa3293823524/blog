---
title: mybatis
tags:
  - 搭建博客
  - 前端
date: 2021-11-05 22:00:25
abbrlink: 80p8o
---
EJB配置复杂  适用范围小
pojo  和数据库表的映射    xml映射文件或者注解
pojo操作数据库数据    hibernate全表映射

mybatis  映射文件  sql语句   支持存储过程   自动映射
mybatis_config.xml 配置文件
sqlsessionFactory  sqlsession  映射器

sqlSession.commit()
sqlSession.rollback()
sqlSession.close()

parameterType参数类型     resultType返回数据类型
读取配置文件生成映射器
SQL Mapper

sqlSession.selectOne  不推荐
sqlSession及时关闭

log4j.properties    打印运行sql和参数

preparedstatement 预处理语句

environments配置环境
配置多个数据源（数据库源  数据库事务）
自定义数据源  实现DataSourceFactory接口

系统别名（基本数据类型 集合类）  自定义别名

文件路径/包名引入映射器/类注册

select   resultMap  (id  result  property column)   useCache

insert flushCache(是否清空本地缓存 二级缓存)   自定义主键生成规则

存储过程支持
自定义缓存

association  collection discriminator 级联  

N+1问题   延迟加载   lazyLoadingEnabled    按层级延迟加载

sqlsessionZ在一级缓存隔离  为了克服用二级缓存
实现二级缓存  pojo序列化    sqlsessionfactory层面共享

自定义缓存

动态sql  
if test
choose  when otherwise
where trim set 
foreach  遍历集合 支持数组 List Set
bind  OGNL表达式

反射
jdk动态代理      映射器
cglib动态代理    mabatis延迟加载用到
建造者模式创建sqlSessionFactory
构建sqlSessionFactory过程

映射器内部组成
sqlSession运行过程   插件基础

Executor 执行器  3种  重用  批量更新
StatementHandler    适配器   prepare()
ParameterHandler   parameterize()
ResultHandler 结果处理器

query/update  执行sql

******************************
spring 
构造方法注入
setter
注解
接口注入   配置jndi数据源

aop:
切点 切面 连接点 通知  目标对象  aop代理

事务传播行为 自调用问题

spring 自动扫描  component-scan



