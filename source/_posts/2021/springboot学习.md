---
title: springboot学习
tags:
  - 搭建博客
  - 前端
date: 2021-11-15 23:40:27
abbrlink: 810fg
---
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113095408385.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113100240611.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113100425175.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113101458509.jpg)

数组

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113101716195.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113101835865.jpg)

Environment env
env.getProperty("")

@Configuration(prefix="")

开发 测试  生产
profile动态配置切换
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113103255897.jpg)
spring.profiles.active=dev

内部配置顺序
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113103943833.jpg)
外部配置顺序（命令行参数等）

EnableAutoConfigutation

@Conditional()  括号里加实现Condition接口的类matches方法

自定义注解
context metadata
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113113313816.jpg)
@ComponentScan
@Import注解导入配置类
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113115930538.jpg)

META-INF/spring.factories
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113120753512.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20220113122225328.jpg)
4个核心
起步依赖     依赖传递
自动配置  利用了Spring 4的条件化配置特性，以及Maven和Gradle提供的传递依赖解析，以此实现Spring应用程序上下文里的自动配置
Actuator   运行时检视应用程序内部情况的能力

@SpringBootApplication   开启组件扫描和自动配置

springboot插件    构建插件的主要功能是把项目打包成一个可执行的超级JAR（uber-JAR）包括把应用程序的
所有依赖打入JAR文件内，并为JAR添加一个描述文件，其中的内容能让你用java -jar来运行
应用程序

spring-boot:run

起步依赖本身的版本是由正在使用的Spring Boot的版本来决定
的，而起步依赖则会决定它们引入的传递依赖的版本

在Maven里，可以用<exclusions>元素来排除传递依赖

配置Thymeleaf的模板解析器、视图解析器以及模板引擎。

实现Condition接口，覆盖它
的matches()方法

自定义配置
两种影响自动配置的方式——使用显式配置进行覆盖和使用属性进行精细
化配置

默认情况下，Spring Boot会用Logback（http://logback.qos.ch）来记录日志，并用INFO级别输
出到控制台

要设置日志级别，你可以创建以logging.level开头的属性

自定义错误页    名为error视图   为错误视图提供错误属性

图片放在src/main/resources/static或src/main/resources/public里

>测试   单元测试  集成测试   测试辅助工具

Spring Mock MVC测试框架来测试Web应用程序

Actuator Web端点
REST端点、远程shell和JMX
<dependency> 
 <groupId>org.springframework.boot</groupId> 
 <artifactId>spring-boot-starter-actuator</artifactId> 
</dependency>
端点可以分为三大类：配置端点、度量端点和其他端点     健康指示器
http://localhost:8080/beans
最重要的端点就是/beans。它会返回一个JSON文档，
描述上下文里每个Bean的情况，包括其Java类型以及注入的其他Bean

保护Actuator端点

连接 Actuator 的远程 shell
<dependency> 
 <groupId>org.springframework.boot</groupId> 
 <artifactId>spring-boot-starter-remote-shell</artifactId> 
</dependency>

定制 Actuator

部署

把spring.profiles.active属性设置为production。

PaaS提供了现成的应用程序部署平台，带有附加服务（比如数据库和消息代理），
可以绑定到应用程序上

应用程序部署到Cloud Foundry和Heroku这两个著名的PaaS平台

事件
事件源
监听器

这2个需要配置（建立META-INF/spring.factories 设置键值对）
ApplicationContextInitializer
SpringApplicationRunListener
环境对象准备
上下文对象准备
上下文对象加载

项目启动后执行
CommandLineRunner
ApplicationRunner

默认info  health
需要配置才能暴露所有