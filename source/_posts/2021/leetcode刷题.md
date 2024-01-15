---
title: leetcode刷题
tags:
  - 搭建博客
  - 前端
date: 2021-10-19 20:19:01
abbrlink: 8069v
---
a ^ b = c ，则 a ^ c = b，且 b ^ c = a
接雨水  dp  单调栈
76 最小覆盖子串
80  双指针
146  LRU
哈希表+双向链表

221最大正方形


141 环形链表

其实，快慢指针法，就是一种 映射 操作， 链表 里面的 一次映射操作，就是 求 next，且 将位置 更新到 这里； 数组 这里，就是 根据 下标 i 求 nums[i] 这个元素值，且 将 下标 更新到这里。

链表里面 有环，即 一个节点 被不同的 节点指向（映射）； 而 这里说的 数组 有环，即 数组中的一个元素值 被不同的 index 指向（映射）； 所以，求解方法 一样可以 使用 快慢指针法。

图java代码   牛客网美团试题
```
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Graph {
    //边
    public class EdgeNode{
        int index;  //存储该顶点对应的下标
        int weight; //存储权重
    }

    ArrayList<String> pointList;    //顶点数组
    LinkedList<EdgeNode> edjList[]; //邻接表
    int pointNum;       //顶点数
    int edgeNum;        //边数


    public Graph(int n){
        pointList = new ArrayList<>(n);
        edjList = new LinkedList[n];
        for (int i = 0; i < n; i++) {
            edjList[i] = new LinkedList<>();
        }
        pointNum = n;
    }

    //添加一条顶点
    public void addPoint(String name){
        if(pointList.size() >= pointNum){
            System.out.println("point array full");
            return ;
        }
        if(pointList.indexOf(name) != -1){
            System.out.println("已经存在"+name);
            return ;
        }
        pointList.add(name);
    }

    public String getName(int index){
        return pointList.get(index);
    }

    //添加一条边
    public void addEdge(String name1, String name2, int weight){

        int i = pointList.indexOf(name1);
        if(i == -1){
            System.out.println("not find nam1="+name1);
            return ;
        }
        int j = pointList.indexOf(name2);
        if(j == -1){
            System.out.println("not find name2="+name2);
            return ;
        }

        EdgeNode edge = new EdgeNode();
        edge.index = j;
        edge.weight = weight;
        edjList[i].add(edge);
        edgeNum++;

        //加入另一个边 （无向边 两边都加）
        edge = new EdgeNode();
        edge.index = i;
        edge.weight = weight;
        edjList[j].add(edge);
        edgeNum++;
    }

    public void printAll(){
        for (String s : pointList) {

        }
        for (int i=0;i<pointList.size();i++) {
            System.out.print("节点"+pointList.get(i) +"边为:");
            for (EdgeNode edgeNode : edjList[i]) {
                System.out.print(pointList.get(edgeNode.index)+" ");
            }
            System.out.println("");
        }
    }

    /**
     * 广度遍历
     * @param name
     */
    public void BSTTraverse(String name){
        LinkedList<Integer> queue = new LinkedList();

        //找到name
        int i = pointList.indexOf(name);
        if(i == -1){
            System.out.println("not find name="+name);
            return ;
        }
        int[] a = new int[pointNum];
        for (int j = 0; j < pointNum; j++) {
            a[j] = 0;
        }

        a[i] = 1;
        LinkedList<EdgeNode> list = edjList[i];
        for (EdgeNode edgeNode : list) {
            queue.addLast(edgeNode.index);
            a[edgeNode.index] = 1;
        }
        while(queue.size() != 0){
            //从queue中拿出一个节点
            i = queue.removeFirst();
            System.out.println("遍历 " + pointList.get(i));

            list = edjList[i];
            for (EdgeNode edgeNode : list) {
                if(a[edgeNode.index] != 1){
                    queue.addLast(edgeNode.index);
                    a[edgeNode.index] = 1;
                }
            }
        }
    }


    public class Node{
        int index;
        int deep;
    }

    /**
     * 根据深度获取好友队列
     * @param name
     * @param deep 获取1度好友 则深度为2
     * @return
     * 采用广度优先算法
     */
    public LinkedList<Node> getQueueByDeep(String name, int deep){
        LinkedList<Node> queue = new LinkedList();
        //找到name
        int i = pointList.indexOf(name);
        if(i == -1){
            System.out.println("not find name="+name);
            return null;
        }
        int[] a = new int[pointNum];
        for (int j = 0; j < pointNum; j++) {
            a[j] = 0;
        }
        Node node = new Node();
        node.index = i;
        node.deep = 1;
        queue.addLast(node);
        a[i] = 1;

        while(queue.size() != 0){
            //从queue中拿出一个节点
            node = queue.getFirst();
            if(node.deep == deep){
                return queue;
            }
            queue.removeFirst();
            //System.out.println("遍历 " + pointList.get(node.index).data);

            List<EdgeNode> list = edjList[node.index];
            for (EdgeNode edgeNode : list) {
                if(a[edgeNode.index] != 1){
                    Node temp = new Node();
                    temp.index = edgeNode.index;
                    temp.deep = node.deep+1;
                    queue.addLast(temp);
                    a[edgeNode.index] = 1;
                    System.out.println("deep="+temp.deep + pointList.get(edgeNode.index));
                }
            }
        }
        return null;
    }

    public static void main(String[] args) throws Exception{

        Graph g = new Graph(7);
        g.addPoint("小团");
        g.addPoint("小美");
        g.addPoint("小诚");
        g.addPoint("小信");
        g.addPoint("小卓");
        g.addPoint("小越");

        g.addPoint("小孩");

        g.addEdge("小团", "小美", 1);
        g.addEdge("小卓", "小美", 1);
        g.addEdge("小诚", "小美", 1);
        g.addEdge("小团", "小卓", 1);
        g.addEdge("小诚", "小信", 1);
        g.addEdge("小信", "小越", 1);
        g.addEdge("小卓", "小越", 1);

        g.addEdge("小信", "小孩", 1);

        g.printAll();

        g.BSTTraverse("小美");

        int deep = 4;
        LinkedList<Node> queue = g.getQueueByDeep("小美", 4);
        if(queue == null){
            System.out.println("没有"+(deep-1)+"度好友");
        }else{
            for (Node node : queue) {
                System.out.println(node.deep+"度好友为 "+ g.getName(node.index));
            }
        }
    }
}
```

HTTPS的实现原理 HTTP的5个常用Method及其含义，以及5个常用Status Code及其含义

拓扑排序
```
import java.lang.reflect.Array;
import java.util.*;
 
/**
 * 给定按火星字典序排列的单词，求单词中出现过的字符的字典序
 * wrt wrf er ett rftt
 * x z x
 * abc bbc
 * hij ikjk kih jkca jkaa jj
 * 构造一个字符的有向无环图，再找拓扑序列
 */
public class Main {
    // 保存图，定义如果字符i在字符j前，那么存在i到j路径，即map[i][j]=1
    private static int[][] map = new int[26][26];
    // 保存每个节点的入度
    private static int[] indegree = new int[26];
    // 记录出现过的字符
    private static boolean[] flag = new boolean[26];
    private static Set<Character> set = new HashSet<>();
    // 保存结果
    private static List<Character> ans = new ArrayList<>();
 
    public static void main(String[] args) {
        // wrt wrf er ett rftt
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int maxLen = 0;
        // 创建有向图
        build(input);
        // 找拓扑序列
        topology();
        if(ans.size() == set.size()) {
            for (Character c : ans) {
                System.out.print(c);
            }
        } else {
            System.out.println("invalid");
        }
    }
 
    public static void topology() {
        while(ans.size() < set.size()) {
            // 是否在一个遍历中找到入度为0的节点，如果没找到，要break;如果一次遍历找到两个入度为0的点，说明是无法确认顺序的
            int cnt = 0;
            for(int i = 0; i < indegree.length; i++) {
                if(indegree[i] == 0 && flag[i]) cnt++;
            }
            if (cnt != 1) break;
            // 找没有入度的节点，加入序列，在有向图中删除这个节点和从这个节点出发的边
            for (int i = 0; i < indegree.length; i++) {
                if (indegree[i] == 0 && flag[i]) {
                    ans.add((char) ('a' + i));
                    flag[i] = false;    // 删除节点
                    for (int j = 0; j < 26; j++) {       // 删除从这个节点出发的边
                        if (map[i][j] == 0) continue;
                        indegree[j]--;
                        map[i][j] = 0;
                    }
                }
            }
        }
    }
 
 
    //[wrt wrf er ett rftt]
    public static void build(String[] strs) {
        // 找到相邻的两个字符串，第一个不相同的字符可以确定字符的顺序
        // 如wrt和wrf可以得到：t->f
        String pre = strs[0];
        for (char c : pre.toCharArray()) {
            set.add(c);
        }
        for(int i = 1; i < strs.length; i++) {
            String cur = strs[i];
            for (char c : cur.toCharArray()) {
                set.add(c);
            }
            for(int j = 0; j < Math.min(pre.length(), cur.length()); j++) {
                if(pre.charAt(j) == cur.charAt(j)) continue;
                if(map[pre.charAt(j)-'a'][cur.charAt(j)-'a'] == 1) break;
                map[pre.charAt(j)-'a'][cur.charAt(j)-'a'] = 1;
                indegree[cur.charAt(j)-'a'] += 1;
                flag[pre.charAt(j)-'a'] = true;
                flag[cur.charAt(j)-'a'] = true;
                break;
            }
            pre = cur;
        }
    }
}
```

redis

有序集合基于散列表和跳跃表实现，访问中间元素时间复杂度是OlogN



单机版：很少使用。存在的问题：1、内存容量有限 2、处理能力有限 3、无法高可用。

主从模式：master 节点挂掉后，需要手动指定新的 master，可用性不高，基本不用。

哨兵模式：master 节点挂掉后，哨兵进程会主动选举新的 master，可用性高，但是每个节点存储的数据是一样的，浪费内存空间。数据量不是很多，集群规模不是很大，需要自动容错容灾的时候使用。

Redis cluster：主要是针对海量数据+高并发+高可用的场景，如果是海量数据，如果你的数据量很大，那么建议就用Redis cluster，所有主节点的容量总和就是Redis cluster可缓存的数据容量。


105  106 二叉树 前 中 后

#创建普通的索引

 alter table `table_name`  add  index `index_name` (`字段名`)

#创建主键索引

alter  table `table_name` add primary  key (`字段名`)

#创建 唯一索引

alter  table  `table_name` add unique  (`字段名`)

#创建全文的索引

alter table `table_name` add  fulltext (`字段名`)

#创建多个索引

alter  table `table_name`  add index  `index_Name`(`column`,`column1`,`column_N`.......)

 

下面是删除索引的语句

drop  index `index_name` on `table_name`

alter  table `table_name` drop index `index_name`


40  组合总和

分治

int quickMulti(int A, int B) {
    int ans = 0;
    for ( ; B; B >>= 1) {
        if (B & 1) {
            ans += A;
        }
        A <<= 1;
    }
    return ans;
}

约瑟夫环

扩展中心    priority queue   比较器
剑指 Offer II 020. 回文子字符串的个数 Manacher 算法

instance = new Singleton();

这句代码在执行时会分解为三个步骤：

1.为对象分配内存空间。

2.执行初始化的代码。

3.将分配好的内存地址设置给instance引用。

当线程进行一个volatile变量的写操作时，JIT编译器生成的汇编指令会在写操作的指令后面加上一个“lock”指令

#线程池生命周期：
##RUNNING：表示线程池处于运行状态，这时候的线程池可以接受任务和处理任务。值是-1，

##SHUTDOWN：表示线程池不接受新任务，但仍然可以处理队列中的任务，二进制值是0。调用showdown()方法会进入到SHUTDOWN状态。

##STOP：表示线程池不接受新任务，也不处理队列中的任务，同时中断正在执行任务的线程，值是1。调用showdownNow()方法会进入到STOP状态。

##TIDYING：表示所有的任务都已经终止，并且工作线程的数量为0。值是2。SHUTDOWN和STOP状态的线程池任务执行完了，工作线程也为0了就会进入到TIDYING状态。

##TERMINATED：表示线程池处于终止状态。值是3

javap -v 命令查看class文件对应的JVM字节码信息
Java对象的内存布局其实由对象头+实例数据+对齐填充

就是Java对象的内存布局其实由对象头+实例数据+对齐填充三部分组成，而对象头主要包含Mark Word+指向对象所属的类的指针组成。Mark Word主要用于存储对象自身的运行时数据，哈希码，GC分代年龄，锁标志等。

>最左匹配原则  联合索引  范围查询
同时我们还可以发现在a值相等的情况下，b值又是按顺序排列的，但是这种顺序是相对的。所以最左匹配原则遇上范围查询就会停止，剩下的字段都无法使用索引。例如a = 1 and b = 2 a,b字段都可以使用索引，因为在a值确定的情况下b是相对有序的，而a>1and b=2，a字段可以匹配上索引，但b值不可以，因为a的值是一个范围，在这个范围中b是无序的。

链表递归实现

跳跃表  单链表 索引

不用平衡二叉树做索引
指的是逻辑结构上的平衡二叉树，其物理实现是数组。然后由于在逻辑结构上相近的节点在物理结构上可能会差很远。因此，每次读取的磁盘页的数据中有许多是用不上的。因此，查找过程中要进行许多次的磁盘读取操作。

Zset是基于跳跃表+字典实现的，如果只是单key查询，那么就直接从字典中查询(字典的key就是保存了元素的值，value则是元素的分值score)，这样可以用O(1)的时间复杂度完成查询。如果是根据分值score进行范围查询，就是去跳跃表中查询

undo log 事务原子性 （失败回滚）  MVCC
逻辑日志 记录SQL语句

redo log  持久性
将对数据页的更改写入到redo log，此时redo log中这条事务的状态为prepare状态。

MySQL在可重复读的隔离级别下，通过MVCC机制和Next-key Lock解决了幻读的问题

反射机制优缺点：
反射机制的优缺点：
优点： 1）能够运行时动态获取类的实例，提高灵活性； 2）与动态编译结合 缺点： 1）使用反射
性能较低，需要解析字节码，将内存中的对象进行解析。 解决方案： 1、通过setAccessible(true)
关闭JDK的安全检查来提升反射速度； 2、多次创建一个类的实例时，有缓存会快很多 3、
ReflectASM工具类，通过字节码生成的方式加快反射速度 2）相对不安全，破坏了封装性（因为通
过反射可以获得私有方法和属性）

notify可能会导致死锁，而notifyAll则不会

剑指offer33

剑指offer40     小跟堆
647回文子串
网络问题，延迟开销，带宽问题，安全问题
 kafka 的设计理念，broker -> topic -> partition

 高可用：主从

 Lucene 是著名的搜索开源软件，ElasticSearch 和 Solr 底层用的都是它
 分词
 分段的思想大大的提高了维护索引的效率
 TF IDF  TF-IDF = TF / IDF
 ElasticSearch 是集群的 = 主分片 + 副本分片
 脑裂

 maven  pom 项目对象模型

 SaaS系统开发

Zookeeper的核心是原子广播，这个机制保证了各个Server之间的同步。实现这个机制的协议叫做
Zab协议

Zab 协议来保证分布式事务的最终一致性。Zab协议要求每个 Leader 都要经历三个阶段：发现，同
步，广播

Zookeeper 有两种选举算法：基于 basic paxos 实现和基于 fast paxos 实现。默认为 fast paxos

恢复模式  广播模式

spring循环依赖 spring事务隔离级别 spring事务传播行为
http  https   1.0和1.1
mybatis缓存   mybatis设计模式
mybatis 1级缓存 没有容量限定的HashMap  （多个sqlSession或者分布式环境 数据库写操作会引起脏数据）

多个 SqlSession之间需要共享缓存，则需要使用到二级缓存。

跨域  sql语句 linux命令练习   fork()
Docker Netty  unicode和utf8编码

Nginx是一个web服务器和方向代理服务器，用于HTTP、HTTPS、SMTP、POP3和IMAP协议
多进程  异步非阻塞  反向代理 负载均衡  

正向代理（通过正向代理的方式，在我们的客户端运行一个软件，将我们的HTTP请求转发
到其他不同的服务器端）
mongodb文档  vue

select poll epoll

nginx用途：
Nginx服务器的最佳用法是在网络上部署动态HTTP内容，使用SCGI、WSGI应用程序服务器、用于
脚本的FastCGI处理程序。它还可以作为负载均衡器

用户管理：提供用户的相关配置，新增用户后，默认密码为123456
角色管理：对权限与菜单进行分配，可根据部门设置角色的数据权限
菜单管理：已实现菜单动态路由，后端可配置化，支持多级菜单
部门管理：可配置系统组织架构，树形表格展示
岗位管理：配置各个部门的职位
字典管理：可维护常用一些固定的数据，如：状态，性别等
系统日志：记录用户操作日志与异常日志，方便开发人员定位排错
SQL监控：采用druid 监控数据库访问性能，默认用户名admin，密码123456
定时任务：整合Quartz做定时任务，加入任务日志，任务运行情况一目了然
代码生成：高灵活度生成前后端代码，减少大量重复的工作任务
邮件工具：配合富文本，发送html格式的邮件
七牛云存储：可同步七牛云存储的数据到系统，无需登录七牛云直接操作云数据
支付宝支付：整合了支付宝支付并且提供了测试账号，可自行测试
服务监控：监控服务器的负载情况
运维管理：一键部署你的应用

347 前k个高频元素

382. 链表随机节点   蓄水池抽样

28   kmp算法
208   实现Trie
547  省份数量   并查集

leetcode 面试题17.13 恢复空格
方法1 Trie+动态规划
方法2  字符串哈希   Rabin-Karp 

最小k个数 快排 还不会


最长递增子序列

面试题17.07 婴儿名字 并查集

面试题16.09 运算 

面试题  10.03 旋转数组
189  153  154  33 81

不同二叉搜索树  卡特兰数

Morris中序遍历


169  投票算法

以 n = 1234567n=1234567 为例，我们需要统计「百位」上数字 11 出现的次数。我们知道，对于从 00 开始每 10001000 个数，「百位」上的数字 11 都会出现 100100 次，即数的最后三位每 10001000 个数都呈现 [000, 999][000,999] 的循环，其中的 [100, 199][100,199] 在「百位」上的数字为 11，共有 100100 个。

 1382 将二叉搜索树变平衡
 783 二叉搜索树节点最小距离

 337 打家劫舍 III
 递增的三元子序列

 324摆动序列II  桶排序
 321 拼接最大数  单调栈
 316 去除重复字母  单调栈
354  套娃  动态规划
 LIS
 牛顿迭代法
 牛顿迭代法是一种近似求解方程（近似求解函数零点）的方法。其本质是借助泰勒级数，从初始值开始快速向函数零点逼近。

 413 等差数列划分
 416 动态规划
 NP完全问题
 417 太平洋  大西洋
 406
 437
 474
 491
 494

 459  kmp
 463
 498  对角线遍历

 单调栈 下一个更大元素  496 503
 ```
 public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        Deque<Integer> stack = new ArrayDeque<Integer>();
        for (int i = nums2.length - 1; i >= 0; --i) {
            int num = nums2[i];
            while (!stack.isEmpty() && num >= stack.peek()) {
                stack.pop();
            }
            map.put(num, stack.isEmpty() ? -1 : stack.peek());
            stack.push(num);
        }
        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; ++i) {
            res[i] = map.get(nums1[i]);
        }
        return res;
    }
```

543  二叉树直径
零钱兑换看区别

556
746 

678 动态规划

快排 堆排序手写

单词接龙


股票利润

链表排序

合并多个链表排序

416
581
除法

DAG有向无环图

01背包逆序

完全背包正序

字符串哈希



关键路径  AOV  AOE

排序链表

归并排序

PriorityQueue<ListNode> heap = new PriorityQueue<ListNode>((a,b)->a.val-b.val);

单调栈  找左边  正序  *********** 找右边  逆序
```    找下一个更大的     ******更小>=  换成<=
while (!stack.isEmpty() && num >= stack.peek()) {
                stack.pop();
            }
            map.put(num, stack.isEmpty() ? -1 : stack.peek());
            stack.push(num);
```

503


子序列去重的问题。对于序列去重，我们可以使用串哈希算法（即 Rabin-Karp 编码

去重还不太会


1392  最长快乐前缀

139  单词拆分

Rabin-Karp 字符串编码   10的9次方+7     10的9次方+9 

2018  dfs
2012

1235   动态规划

1995

康托对角线

1975   贪心

Floyd 算法

记忆化搜索


1901

1920  原地操作

1922 快速幂    50

1942

最小费用最大流


698 如果求方案 dfs怎么做
状态压缩动态规划   1931
1922    快速幂   50   分治算法       2进制拆分
递归
```
public double quickMul(double x, long N) {
        if (N == 0) {
            return 1.0;
        }
        double y = quickMul(x, N / 2);
        return N % 2 == 0 ? y * y : y * y * x;
    }
```

迭代
```
public double quickMul(double x, long N) {
        double ans = 1.0;
        // 贡献的初始值为 x
        double x_contribute = x;
        // 在对 N 进行二进制拆分的同时计算答案
        while (N > 0) {
            if (N % 2 == 1) {
                // 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                ans *= x_contribute;
            }
            // 将贡献不断地平方
            x_contribute *= x_contribute;
            // 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
            N /= 2;
        }
        return ans;
    }
```

除法实现

1910  应用kmp
1911. 最大子序列交替和

200岛屿数量

394  


并查集   399
「力扣」第 547 题：省份数量（中等）；
「力扣」第 684 题：冗余连接（中等）；
「力扣」第 1319 题：连通网络的操作次数（中等）；
「力扣」第 1631 题：最小体力消耗路径（中等）；
「力扣」第 959 题：由斜杠划分区域（中等）；
「力扣」第 1202 题：交换字符串中的元素（中等）；
「力扣」第 947 题：移除最多的同行或同列石头（中等）；
「力扣」第 721 题：账户合并（中等）；
「力扣」第 803 题：打砖块（困难）；
「力扣」第 1579 题：保证图可完全遍历（困难）;
「力扣」第 778 题：水位上升的泳池中游泳（困难）



兑换零钱贪心

48  原地旋转    先水平翻转  再对角线翻转（实现矩阵顺时针旋转90度）

1856  单调栈

392  判断子序列

1832  状态压缩

回文  中心扩展  manacher

698

688  动态规划

687

684  并查集

718

797

788  动态规划

787   最短路
求解最短路一般有三种方法，floyd算法，dijkstra算法和bellman ford算法。这题使用bellman ford算法是适用性最强的，因为该算法的第k步就是求出的从给定起点到所有节点经过最多k步的最短路。如果只想到了dijkstra算法，说明思考方向是对的，但没有用到最合适的算法。


779  找规律


买股票无限次
买股票只买一次
买股票有手续费
买股票最多买两次

841


csp  收集卡牌  状态压缩dp

Bellman-Ford     https://blog.csdn.net/lym940928/article/details/90209172
它的基本原理是对图进行|V| - 1次松弛操作，得到所有可能的最短路径。
它比Dijkstra算法好的部分在于，在计算最短路径的班的权值可以为负，实现起来比较简单。
缺点则是时间复杂度较高，为O(|V||E|)。不过算法已经有了一些改进方案，比如队列优化的Bellmanford算法（SPFA算法），一定程度上提高了效率。

SPFA算法

改进的Dijkstra算法
由于最小费用最大流网络中存在负权值，Dijkstra算法不能直接求解最小费用最大流问题，如果最小费用最大流网络中的权值都非负，则可使用Dijkstra算法。引入势函数h(u)为上一次Dijkstra算法的dist(u)（表示从源点到顶点u的最短距离），对每一条边（u,v）,h(v)<=h(u)+w(u,v)成立，则下一次计算中dist(v)=dist(u)+w(u,v)+h(u)-h(v)，所有的dist值必然都大于等于0，则可以继续用Dijkstra算法求解最短路。

1928  动态规划

1905  子岛屿

出口

784  字母大小写全排列   和子集看区别  90

322  零钱兑换    518      求组合怎么求？

70  爬楼梯

做链表

同值路径等深搜


39  组合总和 搜索回溯

6  z字型变换


2^31−1=2147483647

17


二分查找经典题  旋转排序数组

字符串相乘

40

75颜色分类  荷兰国旗  单指针  双指针

91 解码方法  
97  交错字符串 动态规划
剑指offer46

做股票

[−2147483648,2147483647]

接雨水   双指针  单调栈  dp
正则表达式匹配

85 单调栈

140 记忆化搜索

698  划分为k个相等子集   状态压缩dp


线性筛  0/1背包  完全背包  最小费用最大流 taj强连通分量

二分图  匈牙利算法

DAG最小路径覆盖

二分图最小点覆盖

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213112909911.jpg)
start法则

二分图最大匹配
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213114319836.jpg)

增广路的匈牙利算法
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213150828410.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213151141492.jpg)

带权二分图最佳完美匹配

manacher算法      最长回文子串    中心检测法O(n2)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213133459307.jpg)

无向图双连通分量      割点  桥
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213124131747.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213124926065.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213125419516.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213125704139.jpg)

有向图强连通分量  Tarjan的SCC算法

树上DP   平衡的艺术  树的重心

FF  EA 最大流算法

最小费用最大流
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213120650002.jpg)
Dinic
ISAP


hash LCP

后缀自动机

线段树和树状数组   lowbit    
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213142024751.jpg)
树状数组  动态前缀和（可修改）
线段树   平衡二叉树

区间最值 线段树
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213140923042.jpg)
ST表  静态RMQ(区间最值)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213143017605.jpg)

组合数学和计数


排序二叉树（二叉搜索树）    平衡树  set map 优势人群   multiset


异象石

Treap


ac自动机

RMQ     倍增法求解LCA    链式前向星



关键路径


增广路
dinic   分层图

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211213150352411.jpg)
sap
ek
sf
ff
https://www.cnblogs.com/ZJUT-jiangnan/p/3632525.html



Java红黑树 https://www.cnblogs.com/skywang12345/p/3624343.html


307 线段树
https://www.cnblogs.com/strongmore/p/14223224.html


Java  bellman-ford和SPFA算法实现
https://www.cnblogs.com/lfri/p/9521271.html


面试题 17.17. 多次搜索  trie  kmp

面试题 08.14. 布尔运算  记忆化搜索  区间dp

剑指 Offer II 063. 替换单词    trie


kmp算法
```
public static int strStr(String haystack, String needle) {
        if(needle.length()==0)return 0;
		int[]next=new int[needle.length()];
		int j=0;
		for(int i=1;i<needle.length();i++) {
			while(j>0&&needle.charAt(i)!=needle.charAt(j))j=next[j-1];
			if(needle.charAt(i)==needle.charAt(j))j++;
			next[i]=j;
		}
		j=0;
		for(int i=0;i<haystack.length();i++) {
			while(j>0&&haystack.charAt(i)!=needle.charAt(j))j=next[j-1];
			if(haystack.charAt(i)==needle.charAt(j)) {
				j++;
			}
			if(j==needle.length())return i-needle.length()+1;
		}

	    return -1;
	}
```

剑指offerII 76 快速排序


单调队列   918. 环形子数组的最大和   前缀和 + 单调队列
1696. 跳跃游戏 VI

双连通分量   1192

强连通分量  1489   tarjan
https://blog.csdn.net/u013376508/article/details/50995675
https://blog.csdn.net/springrolls/article/details/101386049
https://www.cnblogs.com/nullzx/p/7968110.html

关键路径
https://blog.csdn.net/CmdSmith/article/details/60960276


计数排序

基数排序

线段树   673最长递增子序列个数
307. 区域和检索 - 数组可修改


多线程

欧拉回路

马拉车    线性筛

线性探查  二次探查

B树  B+树
https://www.jianshu.com/p/92d15df75027


字节流和字符流
https://blog.csdn.net/qq_35122713/article/details/88793019

阻塞 非阻塞 同步  异步



1717贪心

1734

1695   前缀和   滑动窗口

1901 二分


打断标记为真时 park失效

锁  while(防止虚假唤醒)   wait

无索引行锁升级为表锁

show processlist


in走索引 not in 不走

大批量插入数据
主键顺序
关闭唯一性校验
设置手动提交事务

insert

like 
前缀  覆盖索引

order by
统一升序，统一降序  和索引顺序一致 覆盖索引

group by 
 用order by null 覆盖索引

建议用union替换or

索引提示  
use index,ignore index,force index(针对全表扫描不走索引时)


java图邻接链表实现
https://www.jianshu.com/p/3b09a37cf16d