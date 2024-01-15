---
title: java并发学习
tags:
  - 搭建博客
  - 前端
date: 2021-12-03 12:13:36
abbrlink: 81jwd
---
函数式编程 lambda
应用  原理
多线程设计模式


spring
双重检查锁 2次检查1级缓存

读取配置
BeanDefinitionReader

解析
配置类解析器
Configurationclassparser

扫描
ClassPathBeanDefinitionScanner doScan方法

所有bean创建完扩展
实现SmartInitializingSingleton接口
创建ContextRefreshedEvent事件监听器

javaConfig
AnnotaionConfigApplicationContext
AnnotedBeanDefinitionReader
解析各种注解@Bean  @Component
ConfigureClassParser

xml
ClassPathXmlApplicationContext
XmlBeanDefinitionReader
解析
DefaultBeanDefinitionDocumentReader
