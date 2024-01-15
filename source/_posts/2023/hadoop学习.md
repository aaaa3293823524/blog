---
title: hadoop学习
tags:
  - 搭建博客
  - 前端
date: 2023-12-05 01:17:33
abbrlink: 8o4q5
---

# wordcount示例
word.txt
```
hello hadoop hello itcast
hello hadoop hello
hello itcast itcast
```

hadoop fs -mkdir -p /itcast/wordcount/in
hadoop fs -put word.txt /itcast/wordcount/in
hadoop jar hadoop-mapreduce-examples-3.1.4.jar wordcount /itcast/wordcount/in /itcast/wordcount/out

结果
```
hadoop	2
hello	5
itcast	3
```


# hadoop源码编译


mvn package -Pdist,native -DskipTests -Dmaven.javadoc.skip \
    -Dopenssl.prefix=/Users/zhangxuefeng/miniconda3/bin/openssl


# hdfs
分布式存储
三副本  分块  128M


# mapreduce
分布式计算
抽象编程模型
key,value
隐藏底层细节

离线处理 静态数据 不适合处理动态数据,不适合流式计算(数据增长)


hadoop jar example-mr-1.0.jar /in /out


https://blog.csdn.net/qq_24950043/article/details/122518707


9870  hdfs

8088  yarn

4040 spark



sc.textFile("data/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect


bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master local[2] \
./examples/jars/spark-examples_2.12-3.0.0.jar 10
![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-06_02-05-10.png)


bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master spark://node4:7077 \
./examples/jars/spark-examples_2.12-3.0.0.jar 10

bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master yarn \
--deploy-mode client \
./examples/jars/spark-examples_2.12-3.0.0.jar 10

bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master yarn \
--deploy-mode cluster \
./examples/jars/spark-examples_2.12-3.0.0.jar 10




http://node4:8081/

历史服务器
http://172.16.117.104:18080/


io性能
数据压缩
属性优化

# jni
创建JniDemo.java
```
public class JniDemo {
    public native void sayHello();
}
```
javac JniDemo.java -h .
https://zhuanlan.zhihu.com/p/563584554?utm_id=0




https://blog.csdn.net/ting_happy/article/details/126614295





使用 CLion debug 跟踪 nginx/OpenResty 源码
https://blog.csdn.net/jackaing/article/details/133926039


./auto/configure --prefix="./"



redis源码剖析
https://zhuanlan.zhihu.com/p/621551734

redis-server启动
http://wed.xjx100.cn/news/278217.html?action=onClick

https://zhuanlan.zhihu.com/p/607178276?utm_id=0

-DWITH_DEBUG=1
-DWITH_BOOST=/Users/zhangxuefeng/Downloads/mysql-5.7.32/boost



--defaults-file=/Users/zhangxuefeng/Downloads/mysql-5.7.32/my.cnf --initialize --console


brew link openssl@1.1 --force


https://blog.51cto.com/u_16099304/6933332

初始化
--initialize --console --basedir=/Users/zhangxuefeng/Downloads/mysql-5.7.32 --datadir=/Users/zhangxuefeng/Downloads/mysql-5.7.32/data

![](https://gitee.com/mosheng123456789/pics/raw/master//Users/zhangxuefeng/Desktop/img/Snipaste_2023-12-06_20-21-57.png)

k51uyStc7s_%

重设密码


frm ibd

frm myi myd



# hive

nohup bin/hive --service metastore &
nohup bin/hive --service hiveserver2 &

结构化文件映射为表

order by 全局排序 reduceTask一个 
cluster by   分组+排序 两个字段是同一个
distribute by   sort by

left semi join  左半开连接  只返回左边表字段

运算符,函数
关系运算,逻辑运算,算术运算

not like
rlike,regexp 正则表达式

concat   ||
map
struct
array

udf  
udtf  一进多出
udaf  多进一出

concat_ws
regexp_replace
split
get_json_object

unix_timestamp
from_unixtime
datediff
date_add
date_sub

size
map_keys
map_values
array_contains
sort_array

if
isnull
isnotnull
nvl  空值转换
coalesce   第一个非空

case 
when then
when then
else
end

cast(12.14 as bigint)

数据脱敏函数
mask  
mask_hash

java_method
reflect

增强聚合  
grouping sets
cube
rollup
窗口聚合 rows between        ntile
窗口分析  lead   lag   first_value   last_value
抽样 随机,桶表,块(速度快,不随机)


多行转单列 collect_list   collect_set

json_tuple

拉链表

explain extended

orc 行组索引  布隆过滤器索引   矢量化查询(一次读取多行)

SMB   关联优化
CBO 代价 RBO 规则
PPD   谓词下推  过滤条件提前执行
倾斜优化
LLAP  tez

@GrpcService

spring.main.web-application-type:none 不用tomcat


mvn dependency:tree -Dincludes=groupId:artifactId


单reactor 单reactor多线程  多reactor  主从reactor


thrift -r --gen java --out src/main/java src/main/thrift/user.thrift


https://pan.baidu.com/s/1PkCjWWCF9EEG6KQrC255hA
1234

心跳端口 选举端口

scp -r apache-zookeeper-3.7.0-bin root@node1:/opt/software/


chmod u+x zkServer.sh
./zkServer.sh start
./zkServer.sh status

https://blog.csdn.net/u013516966/article/details/125631413

./startup.sh -m standalone
http://127.0.0.1:8848/nacos


nohup ./bin/kafka-server-start.sh config/server.properties &

kafka-eagle
admin 123456
http://127.0.0.1:8048/ke/



dubbo泛化调用
https://blog.csdn.net/li12412414/article/details/128680443
https://www.jianshu.com/p/e3a42571e4d7
https://blog.csdn.net/lkforce/article/details/106929812
https://cloud.tencent.com/developer/article/2283217?areaSource=102001.17&traceId=J72c4dLC-1tdssPPS_BRz




# hbase
web ui
http://node4:16010/



es路由
https://blog.csdn.net/m0_67393827/article/details/123922565

https://blog.csdn.net/qq_36963950/article/details/108952827


man 7 signal
/dev/zero
/dev/null
ps ajx
man 7 ip
flatMap

hive设置spark
https://www.cnblogs.com/doublexi/p/15638331.html


ssh-keygen -t rsa -b 4096


