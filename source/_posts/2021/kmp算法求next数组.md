---
title: kmp算法求next数组
tags:
  - 搭建博客
  - 前端
date: 2021-11-03 10:05:47
abbrlink: 80mgt
---
朴素匹配算法   leetcode 28
在这里存在一个问题，回溯到下一位置可能导致很多多余比较操作

母串：ABABABABACABCAB
样本串：ABABABC
在上述比较中，进行多次多余回溯操作（多次比较无意义）

母串：ABABABABACABCAB
样本串：ABABABC
// 这里位置不是按数组0位开始。
第一次比较在第7位发现与母串不同，那么我们肉眼观察下，下一次比较为
ABABABABACABCAB
    ABABABC
这样最为合理（即母串的第7位与样本串的第5位进行比较）。
那么为什么选择该回溯位置？？

样本串 ABABABC 假如与未知字符串比较，那么求出当未知字符串第i位匹配不同时，样本串与未知字符串第i位重新比较的位置，即为样本串的next数组。

怎么求出其对应的next数组？

样本串 ABABABC，如果第5个位置与未知字符串不同，那么前4位为 ABAB ， （此处可以理解为样本串后移）后移几位合适？后移则是比较前缀和后缀是否相同，其最大公共前后缀的长度几位下一次比较的样本串的位置。

问题转化为求取样本串的当前位置之前的最大公共前后缀的长度（next数组），也是KMP算法的核心部分。

A B A B A B C 的next数组。
0 0 0 1 2 3 4

class Solution {

    /**
	 * 寻找最长公共前缀后缀的长度
	 * 示例：ABABCABAB
	 * 前缀集合（不包含示例本身）：A, AB, ABA, ABAB, ABABC, ABABCA, ABABCAB, ABABCABA
	 * 后缀集合（不包含示例本身）：B, AB, BAB, ABAB, CABAB, BCABAB, ABCABAB, BABCABAB
	 * 最长公共前缀后缀为，ABAB；返回4
	 * @param needle 传入字符串
	 * @return 最长公共前缀后缀的长度
	 */
	public static int publicPrefix(String needle) {
		int length = needle.length();
		int result = length - 1;
		while(result > 0){
			int i = 0;
			while (needle.charAt(i) == needle.charAt(length - result + i)){
				i++;
				if(i == result){
					return result;
				}
			}
			result--;
		}
		return result;
	}

    public int strStr(String haystack, String needle) {
		if(needle.isEmpty()){
			return 0;
		}
        if(haystack.length() < needle.length()){
			return -1;
		}
		/**
		 * KMP算法
		 * 第一步获取needle的next数组
		 **/
		int[] next = new int[needle.length()];
        next[0] = 0;
		for(int i = 1; i < next.length; i++){
			next[i] = publicPrefix(needle.substring(0,i));
		}
		// 遍历母字符串
		// haystack下标指针
		int i = 0;
		int j = 0;
		boolean isExist = false;
		while(i <= haystack.length() - 1){
			if(haystack.charAt(i) != needle.charAt(j)){
                if(j == 0){
                    i++;
                }
				j = next[j];
			} else {
				if (j == next.length - 1) {
					isExist = true;
					break;
				} else {
					i++;
					j++;
				}
			}
		}
		int result = isExist ? i -j : -1;
		return result;
	}
}




class Solution {
    public boolean repeatedSubstringPattern(String s) {
        return kmp(s + s, s);
    }

    public boolean kmp(String query, String pattern) {
        int n = query.length();
        int m = pattern.length();
        int[] fail = new int[m];
        Arrays.fill(fail, -1);
        for (int i = 1; i < m; ++i) {
            int j = fail[i - 1];
            while (j != -1 && pattern.charAt(j + 1) != pattern.charAt(i)) {
                j = fail[j];
            }
            if (pattern.charAt(j + 1) == pattern.charAt(i)) {
                fail[i] = j + 1;
            }
        }
        int match = -1;
        for (int i = 1; i < n - 1; ++i) {
            while (match != -1 && pattern.charAt(match + 1) != query.charAt(i)) {
                match = fail[match];
            }
            if (pattern.charAt(match + 1) == query.charAt(i)) {
                ++match;
                if (match == m - 1) {
                    return true;
                }
            }
        }
        return false;
    }
}


BM算法


散列表：
直接定值法

解决哈希冲突
1 开放定值法    线性探测  二次探测 
 线性探测和二次探测必须考虑载荷因子，超过0.7-0.8就增容，增大效率，（以空间换时间）
其中删除是惰性删除，也就是只标记删除记号，实际操作则待表格重新整理时再进行，因为HashTable中的每一个元素不仅代表自己，也关系到其他元素。

删除：空散列表标志位true  存入新元素标志FALSE  删除元素不改变标志位，元素关键词设为“neverUserd” 
初始时标志位true（查找） 关键词neverUserd （插入）
2 拉链法

[!事务实现](https://blog.csdn.net/qq_42764468/article/details/108572936)

CyclicBarrier reset 重复使用 全部等待
countdownlatch 1个线程等待其他线程执行完成并发出通知

volatile和CAS结合  原子类
ABA  变量原子性 不能保证代码块原子性

ReadWriteLock   读写分离锁
读锁是共享的，写锁是独占的，读和读之间不会互斥，读和写、写和读、
写和写之间才会互斥，提升了读写的性能

Semaphore 就是一个信号量，它的作用是限制某段代码块的并发数

同步的范围越小越好。  范围外异步执行

Executors框架

有符号数  无符号数

栈空间用光了会引发 StackOverflowError，而堆和常量
池空间不足则会引发 OutOfMemoryError

-128-127   Integer是否创建新对象  IntegerCache内部类  

>运行时常量池 String类的 intern()方法就是这样的。

>JIT编译器发展 逃逸分析 对象一定分配在堆上这件事情已经变得不那么绝对了
栈上分配 标量替换

四舍五入的原理是在参数上加 0.5 然后进行下取整

关联关系（Has-A）和依赖关系（Use-A）继承关系（Is-A）

char 2个字节
>加载：class文件->内存 生成Class对象 
验证
准备 （静态变量分配内存 初始化）
解析（将符号引用替换为直接引用）
初始化  有父类先初始化父类 执行初始化语句 类加载器

https://baijiahao.baidu.com/s?id=1715222351753027085&wfr=spider&for=pc
>Error通常是程序无法处理的错误，这些错误大多数与代码编写者执行的操作无关，并且它们是无法被捕获的，因为它们在应用程序的控制和处理能力之外，比如。
OutOfMemoryError, 内存溢出，比较常见的错误，是值内存空间不足以再提供新对象的分配。
StackOverflowError，栈溢出。
虚拟机栈：如果线程请求的栈深度大于虚拟机栈所允许的深度，将会出现StackOverflowError异常；如果虚拟机动态扩展无法申请到足够的内存，将出现OutOfMemoryError。
本地方法栈和虚拟机栈一样。
堆：Java 堆可以处于物理上不连续，逻辑上连续，就像我们的磁盘空间一样，如果堆中没有内存完成实例分配，并且堆无法扩展时，将会抛出 OutOfMemoryError。
方法区：方法区无法满足内存分配需求时，将抛出OutOfMemoryError异常。

>常见的非受检异常有
ArrayIndexOutOfBoundsException，数组越界异常
NullPointerException，空指针异常
IllegalArgumentException，非法参数异常
NegativeArraySizeException，数组长度为负异常
IllegalStateException，非法状态异常
ClassCastException，类型转换异常



字符被从 JVM 内部转移到外部时（例如存入文件系统
中），需要进行编码转换。所以 Java 中有字节流和字符流，以及在字符流和字节
流之间进行转换的转换流，如 InputStreamReader 和 OutputStreamReader，
这两个类是字节流和字符流之间的适配器类，承担了编码转换的任务



>抽象方法需要子类重写，而静态的方法是无法被重写

>本地方法是由本地代码（如 C 代码）实现的方法，而抽象方法是没有实现的

>synchronized 和方法的实现细节有关，抽象方法不涉及实现细
节

Tenured  老年代

接口可以继承接口，而且支持多重继承。抽象类可以实现(implements)接口，抽象类可继承具体类也可以继承抽象类

>强引用 不会回收  内存不足时抛出内存溢出异常 引用赋值null中断和对象关联   
软引用  内存足够垃圾收集器不会回收 内存不够时回收   缓存
弱引用  生命周期更短  被发现就会被回收    静态内部类
虚引用  相当于没有引用 任何时候都可能被垃圾回收器回收
jdk中直接内存的回收就用到虚引用
https://www.cnblogs.com/zeussbook/p/12716173.html

Blob 是指二进制大对象（Binary Large Object），而 Clob 是指大字符对象（Character Large Objec）

面向对象 6原则1法则

leetcode  84    85  单调栈


spring循环依赖
https://www.cnblogs.com/zzq6032010/p/11406405.html