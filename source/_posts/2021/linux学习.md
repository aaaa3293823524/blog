---
title: linux学习
tags:
  - 搭建博客
  - 前端
date: 2021-11-16 18:03:21
abbrlink: 811a3
---
编译驱动程序

显卡 x window cpu

如果内存不够大， 就会使用到硬盘的内存交换空间（swap）

磁盘阵列（RAID）是利用硬件技术将数个硬盘整合成为一个大硬盘的方法，操作系统只会看到最后被整合起来的大硬盘  备份

在Linux系统中，每个设备都被当成一个文件来对待

SATA接口的硬盘的文件名称即为/dev/sd[a-d]
打印机   软盘 分别是/dev/lp0, /dev/fd0
Linux核心侦测到磁盘的顺序
磁盘的组成主要有盘片、机械手臂、磁头与主轴马达所组成， 而数据 的写入其实是在盘片上面

盘片上面又可细分出扇区（Sector）与磁道（Track）两种单位， 其中扇区的物理量设计有两种大小，分别是 512Bytes 与 4KBytes
第一个扇区  MBR （Master Boot Record） 格式   主要开机记录区     安装开机管理程序（446）   分区表（64）
GPT （GUID partition table）
柱面   

延伸分区的目的是使用额外的扇区来记录分区信息，延伸分区本身并不能被 拿来格式化。 然后我们可以通过延伸分区所指向的那个区块继续作分区的记录

主要分区与延伸分区最多可以有四笔
延伸分区最多只能有一个
逻辑分区是由延伸分区持续切割出来的分区

GPT  逻辑区块位址 LBA0   GPT 使用了 34 个 LBA 区块来纪录分区 信息
GPT 除了前面 34 个 LBA 之外，整个磁盘的最后 33 个 LBA 也拿来作为另一个备份

开机管理程序 grub

开机检测程序  BIOS UEFI
开机管理程序的目的是在载入（load）核心文件
挂载点
--help
man   info
编辑器  nano
关机 shutdown   -h 关机  -r 重启     reboot
init 0关机   init 6重启
echo $LANG  语系 locale
#代表以 root 的身份登陆系统，而 $ 则代表一般身份使用者

GNOME/KDE

i-node  属性记录的有多少 不同的文件名链接到相同的一个i-node号码

u g o a  + - =

区块（block）设备文件    储存数据， 以提供系统随机存取的周边设备，举 例来说，硬盘与软盘等就是啦
字符（character）设备文件  键盘、鼠标 一次性读取”的，不能够截断输出

第5章 linux目录配置
寻找文件和指令

basename  dirname
cat -n -v  -A

g前进到第一行  G前进到最后一行
chattr   设置文件隐藏属性
lsattr

文件特殊权限    SUID SGID SBIT
file 文件类型
which （寻找“可执行文件”）   type （bash shell）   命令
whereis 或者是 locate 来检查

第7章 inode  block
命令别名设置功能： （alias）
管线  数据流重定向
环境变量例如 PATH、HOME、MAIL、SHELL,HOSTNAME,USER
export 变量变为环境变量
PS1 提示字符
read  declare
变量内容删除

bash环境配置文件
/etc/profile   ~/.bash_profile
source 或者.  读入配置文件
&   工作控制 （job control）：将指令变成背景下工作
>  取代   >>累加
/dev/null 垃圾桶黑洞设备与特殊写法
2>&1    1>&2

cut 处理多空格相连数据吃力    选行中的段
cut -d 分割字符  -f

grep   选行  -n
-i  忽略大小写
-v 反向选择

sort  r  f u          sort -t   -k (和cut类似)

uniq  -c 计数  -i  忽略大小写

wc -l ：仅列出行； -w ：仅列出多少字（英文单字）； -m ：多少字符；

双向重导向  tee
字符转换命令 tr,col,join,paste,expand
split  大文件分为小文件

xargs  x 是加减乘除的乘号，args 则是 arguments （参数） 的意思
xargs -n 1
--color=auto
行首 ^  行尾 $
只有行首跟行尾 （^$）  空白行
.*
{}
第11章 正则表达式
sed本身也是管线命令    取代、删除、新增、撷取特定行
-n ：使用安静（silent）模式。在一般 sed 的用法中，所有来自 STDIN 的数据一般都会被列出到屏幕上。 但如果加上 -n 参数后，则只有经过 sed 特殊处理的那一行（或者动作）才会被列出来。 -e ：直接在命令行界面上进行 sed 的动作编辑； -f ：直接将 sed 的动作写在一个文件内， -f filename 则可以执行 filename 内的 sed 动作； -r ：sed 的动作支持的是延伸型正则表达式的语法。（默认是基础正则表达式语法） -i ：直接修改读取的文件内容，而不是由屏幕输出。

sed 's/要被取代的字串/新的字串/g'
sed -i
awk

awk '条件类型1{动作1} 条件类型2{动作2} ...' filename
$1    $0代表一整列数据

NF 每一行 （$0） 拥有的字段总数 
NR 目前 awk 所处理的是“第几行”数据 
FS 目前的分隔字符，默认是空白键

BEGIN    END

磁盘与文件系统
ext2  block群组

>压缩 打包
>进程管理

select  poll epoll
>I/O

## 压缩和打包
网络传输也用压缩，加快传输速度

*.Z compress 程序压缩的文件；
*.zip zip 程序压缩的文件； 
*.gz gzip 程序压缩的文件； 
*.bz2 bzip2 程序压缩的文件； 
*.xz xz 程序压缩的文件； 
*.tar tar 程序打包的数据，并没有压缩过； 
*.tar.gz tar 程序打包的文件，其中并且经过 gzip 的压缩 
*.tar.bz2 tar 程序打包的文件，其中并且经过 bzip2 的压缩 
*.tar.xz tar 程序打包的文件，其中并且经过 xz 的压缩
这些指令通常仅能针对一个文件来压缩与解压缩，如此一来， 每 次压缩与解压缩都要一大堆文件，岂不烦人？此时，那个所谓的“打包软件, tar”就显的很重要 啦、

目前 gzip 可以解开 compress, zip 与 gzip 等软件所 压缩的文件

选项与参数：
 -c ：将压缩的数据输出到屏幕上，可通过数据流重导向来处理； 
 -d ：解压缩的参数； 
 -t ：可以用来检验一个压缩文件的一致性～看看文件有无错误； 
 -v ：可以显示出原文件/压缩文件的压缩比等信息； 
 -# ：# 为数字的意思，代表压缩等级，
 -1 最快，但是压缩比最差、
 -9 最慢，但是压缩比最好！
 默认是 -6

 如果你还想要从文字压缩文件当中找数据的话，可以通过 egrep 来搜寻关键字喔！而 不需要将压缩文件解开才以 grep 进行！ 这对查询备份中的文本文件数据相当有用

 bzip2, bzcat/bzmore/bzless/bzgrep
 若说 gzip 是为了取代 compress 并提供更好的压缩比而成立的，那么 bzip2 则是为了取代 gzip 并提供更佳的压缩比而来的

 选项与参数： 
 -c ：将压缩的过程产生的数据输出到屏幕上！ 
 -d ：解压缩的参数 
 -k ：保留原始文件，而不会删除原始的文件喔！ 
 -z ：压缩的参数 （默认值，可以不加） 
 -v ：可以显示出原文件/压缩文件的压缩比等信息； 
 -# ：与 gzip 同样的，都是在计算压缩比的参数， 
 -9 最佳， -1 最快！

 xz, xzcat/xzmore/xzless/xzgrep
 xz 这个压缩比更高
 选项与参数： 
 -d ：就是解压缩啊！ 
 -t ：测试压缩文件的完整性，看有没有错误 
 -l ：列出压缩文件的相关信息 
 -k ：保留原本的文件不删除～ 
 -c ：同样的，就是将数据由屏幕上输出的意思！ 
 -# ：同样的，也有较佳的压缩比的意思！

 选项与参数： 
 -c ：创建打包文件，可搭配 
 -v 来察看过程中被打包的文件名（filename）
-t ：察看打包文件的内容含有哪些文件名，重点在察看“文件名”就是了； 
-x ：解打包或解压缩的功能，可以搭配 
-C （大写） 在特定目录解开 特别留意的是， 
-c, -t, -x 不可同时出现在一串命令行中。 
-z ：通过 gzip 的支持进行压缩/解压缩：此时文件名最好为 *.tar.gz 
-j ：通过 bzip2 的支持进行压缩/解压缩：此时文件名最好为 *.tar.bz2 
-J ：通过 xz 的支持进行压缩/解压缩：此时文件名最好为 *.tar.xz 特别留意， -z, -j, -J 不可以同时出现在一串命令行中 
-v ：在压缩/解压缩的过程中，将正在处理的文件名显示出来！ 
-f filename：-f 后面要立刻接要被处理的文件名！建议 -f 单独写一个选项啰！（比较不会忘记） 
-C 目录 ：这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项。
 其他后续练习会使用到的选项介绍： 
 -p（小写） ：保留备份数据的原本权限与属性，常用于备份（-c）重要的配置文件 
 -P（大写） ：保留绝对路径，亦即允许备份数据中含有根目录存在之意； --exclude=FILE：在压缩的过程中，不要将 FILE 打包！
 ![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211209230213649.jpg)
 dd 可备份完整的 partition 或 disk ，因为 dd 可读取磁盘的 sector 表面数据 cpio 为相当优秀的备份指令，不过必须要搭配类似 find 指令来读入欲备份的文件名数 据，方可进行备份动作。



## shell脚本
 shell script 有点像是早期的批处理文件

/etc/init.d/* 这个脚本启动的方式 （systemV） 已经被新一代的 systemd 所取 代 （从 CentOS 7 开始）
- 自动化管理的重要依据
- 追踪与管理系统的重要工作

防火墙连续规则 （iptables），开机载入程序的项目 （就是在 /etc/rc.d/rc.local 里头的数据）
用在系统管理上面是很好的一项工具，但是用在处理大量数值运算上， 就不够好

shell.sh 文件必须要具备可读与可执行 （rx） 的权限
将 shell.sh 放在 PATH 指定的目录内

PATH 与 LANG （如果有使用到输出相关的信息时） 是当中最重要的

程序码

使用 vim 而不是 vi ，因为 vim 会有额外的 语法检验机制

利用 test 指令的测试功能

在中括号 [] 内的每个元件都需要有空白键来分隔； 在中括号内的变量，最好都以双引号括号起来； 在中括号内的常数，最好都以单或双引号括号起来。


如果你想要重新 启动系统的网络，可以这样做：
/etc/init.d/network restart

$*
$#
$@

条件判断式  if  then

if [ 条件判断式 ]; then 
   当条件判断式成立时，可以进行的指令工作内容； 
else
    当条件判断式不成立时，可以进行的指令工作内容；
fi

if [ 条件判断式一 ]; then 
   当条件判断式一成立时，可以进行的指令工作内容； 
elif [ 条件判断式二 ]; then 
   当条件判断式二成立时，可以进行的指令工作内容； 
else
    当条件判断式一与二均不成立时，可以进行的指令工作内容； 
fi


netstat 的指令，这个 指令可以查询到目前主机有打开的网络服务端口 （service ports）

80: WWW 22: ssh 21: ftp 25: mail 111: RPC（远端程序调用） 631: CUPS（打印服务功能）

case ${1} in "hello"）
 echo "Hello, how are you ?" 
 ;; 
 ""）
 echo "You MUST input parameters, ex&gt; {${0} someword}"
  ;; 
  *） # 其实就相当于万用字符，0~无穷多个任意字符之意！ 
  echo "Usage ${0} {hello}" 
  ;;
esac

## 循环
while do done, until do done （不定循环）

while [ condition ] &lt;==中括号内的状态就是判断式 
do         &lt;==do 是循环的开始！ 
   程序段落 done &lt;==
done 是循环的结束 

while 的中文是“当....时”，所以，这种方式说的是“当 condition 条件成立时，就进行循环，直 到 condition 的条件不成立才停止”的意思。还有另外一种不定循环的方式： 

until [ condition ] 
do 
程序段落
 done
这种方式恰恰与 while 相反，它说的是“当 condition 条件成立时，就终止循环， 否则就持续 进行循环的程序段

for var in con1 con2 con3 ... 
do 
  程序段 
done

for （（ i=1; i&lt;=${nu}; i=i+1 ））
 do 
    s=$（（${s}+${i}））
 done

## 例行性工作调度（crontab）
 Linux 工作调度的种类： at, cron
at ：at 是个可以处理仅执行一次就结束调度的指令，不过要执行 at 时， 必须要有 atd 这个服务的支持才行

crontab ：crontab 这个指令所设置的工作将会循环的一直进行下去！ 可循环的时间为分 钟、小时、每周、每月或每年等。crontab 除了可以使用指令执行外，亦可编辑 /etc/crontab 来支持。 至于让 crontab 可以生效的服务则是 crond 这个服务喔！

一只程序“ logwatch ”来主动分析登录信息

利用 /etc/at.allow 与 /etc/at.deny 这两个文件来进行 at 的使用限制

系统的配置文件： /etc/crontab, /etc/cron.d/*

anacron

nohup

## 程序管理与SELinux
fork and exec：程序调用的流程

程序都会借由父程序以复制 （fork） 的方式产生一个一模一样的子程序， 然后被复制出来的子程序再以 exec 的方式来执行实际 要进行的程序，最终就成为一个子程序的存在

PPID

系统或网络服务：常驻在内存的程序

多重登陆环境的七个基本终端窗口
六个文字界面登陆窗口，以及一个图形界面

再按 [Alt]+[F1].....[F7] 来 切换到其他的终端机界面，然后以 ps -aux 找出刚刚的错误程序，然后给他 kill 一下

工作管理
前景：你可以控制与下达指令的这个环境称为前景的工作 （foreground）； 
背景：可以自行运行的工作，你无法使用 [ctrl]+c 终止他，可使用 bg/fg 调用该工作

观察目前的背景工作状态： jobs

将背景工作拿到前景来处理：fg

让工作在背景下的状态变成运行中： bg

如果你想要让在背景的工作在你登出后还能够继续的执行，使用 nohup 搭配 & 是不错的

静态的 ps 或者是动态的 top，还能以 pstree 来查阅程序树之间的关系静 态的 ps 或者是动态的 top，还能以 pstree 来查阅程序树之间的关系

观察系统所有程序： ps aux
仅观察自己的 bash 相关程序： ps -l


选项与参数：
 -d ：后面可以接秒数，就是整个程序画面更新的秒数。默认是 5 秒； -b ：以批次的方式执行 top ，还有更多的参数可以使用喔！ 通常会搭配数据流重导向来将批次的结果输出成为文件。 
 -n ：与 -b 搭配，意义是，需要进行几次 top 的输出结果。
  -p ：指定某些个 PID 来进行观察监测而已。
   在 top 执行过程当中可以使用的按键指令： 
  ? ：显示在 top 当中可以输入的按键指令； 
  P ：以 CPU 的使用资源排序显示； 
  M ：以 Memory 的使用资源排序显示；
   N ：以 PID 来排序喔！ 
   T ：由该 Process 使用的 CPU 时间累积 （TIME+） 排序。 
   k ：给予某个 PID 一个讯号 （signal）
    r ：给予某个 PID 重新制订一个 nice 值。 
    q ：离开 top 软件的按键。

程序管理

系统资源的观察
free ：观察内存使用情况
uname：查阅系统与核心相关信息
uptime：观察系统启动时间与工作负载
netstat ：追踪网络或插槽档
dmesg ：分析核心产生的讯息
vmstat ：侦测系统资源变化

特殊文件与程序
查询已打开文件或已执行程序打开之文件

lsof ：列出被程序所打开的文件文件名

pidof ：找出某支正在执行的程序的 PID

SELinux   安全强化的 Linux


## 系统服务
Unix 的 system V 版本
基本上 init 的管理机制有几个特色
使用 bash shell script 所写成的脚本程序，需要启动、关闭、重新启动、观察状 态时， 可以通过如下的方式来处理： 
启动：/etc/init.d/daemon start 
关闭：/etc/init.d/daemon stop 
重新启动：/etc/init.d/daemon restart 
状态观察：/etc/init.d/daemon status

systemd
从 CentOS 7.x 以后，Red Hat 系列的 distribution 放弃沿用多年的 System V 开机启动服务的 流程，就是前一小节提到的 init 启动脚本的方法， 改用 systemd 这个启动服务管理机制

平行处理所有服务，加速开机流程： 旧的 init 启动脚本是“一项一项任务依序启动”的模 式，因此不相依的服务也是得要一个一个的等待
系统启动的速度变快

一经要求就回应的 on-demand 启动方式： systemd 全部就是仅有一只 systemd 服务搭 配 systemctl 指令来处理，无须其他额外的指令来支持

首先 systemd 先定义所有的服务为一个服务单位 （unit），并将该 unit 归类到不同的服务类型 （type） 去

向下相容旧有的 init 服务脚本

systemd 的配置文件放置目录

通过 systemctl 管理服务

systemctl [command] [unit]
command 主要有： 
start ：立刻启动后面接的 unit 
stop ：立刻关闭后面接的 unit 
restart ：立刻关闭后启动后面接的 unit，亦即执行 stop 再 start 的意思
 reload ：不关闭后面接的 unit 的情况下，重新载入配置文件，让设置生效 
 enable ：设置下次开机时，后面接的 unit 会被启动 
 disable ：设置下次开机时，后面接的 unit 不会被启动 
 status ：目前后面接的这个 unit 的状态，会列出有没有正在执行、开机默认执行否、登录等信息等！ 
 is-active ：目前有没有正在运行中 is-enable ：开机时有没有默认要启用这个 unit

/etc    /usr/lib

## 登录文件
 记录系统活动信息的几个文件， 例如：何时、何地 （来源 IP）、何人 （什么服务名称）、做了什么动作 （讯息登录啰）。 换句话说就是：记 录系统在什么时候由哪个程序做了什么样的行为时，发生了何种的事件等等
 /var/log/

 systemd-journald.service：最主要的讯息收受者，由 systemd 提供的； 
 rsyslog.service：主要登录系统与网络等服务的讯息； 
 logrotate：主要在进行登录文件的轮替功能。

## 开机流程，模块管理 loader
按下电源按键后计算机硬件会主动的读取 BIOS 或 UEFI BIOS 来载入硬件信息及 进行硬件系统的自我测试， 之后系统会主动的去读取第一个可开机的设备 （由 BIOS 设置 的） ，此时就可以读入开机管理程序

开机管理程序可以指定使用哪个核心文件来开机，并实际载入核心到内存当中解压缩与执行， 此时核心就能够开始在内存内活动，并侦测所有硬件信息与载入适当的驱动程序来使整 部主机开始运行， 等到核心侦测硬件与载入驱动程序完毕后，一个最阳春的操作系统就开始 在你的 PC 上面跑了。

主机系统开始运行后，此时 Linux 才会调用外部程序开始准备软件执行的环境，并且实际的 载入所有系统运行所需要的软件程序哩！ 最后系统就会开始等待你的登陆与操作啦

核心： /boot/vmlinuz 或 /boot/vmlinuz-version； 
核心解压缩所需 RAM Disk： /boot/initramfs （/boot/initramfs-version）； 
核心模块： /lib/modules/version/kernel 或 /lib/modules/$（uname -r）/kernel； 
核心源代码： /usr/src/linux 或 /usr/src/kernels/ （要安装才会有，默认不安装）

核心版本： /proc/version 
系统核心功能： /proc/sys/kernel/

如果我有个新的硬件，偏偏我的操作系统不支持，该怎么办
重新编译核心，并加入最新的硬件驱动程序源代码；
将该硬件的驱动程序编译成为模块，在开机时载入该模块

核心模块与相依性

lsmod
模块名称（Module）； 
模块的大小（size）；
 此模块是否被其他模块所使用 （Used by）

 modinfo

 核心模块的载入与移除
insmod 则完全由使用者自行载入一个完整文件名的模块
rmmod

使用 insmod 与 rmmod 的问题就是，你必须要自行找到模块的完整文件名才行

核心模块的额外参数设置：/etc/modprobe.d/*conf


第一支程序 systemd 及使用 default.target 进入开机程 序分析

grub2
boot loader 的两个 stage
Stage 1：执行 boot loader 主程序：
Stage 2：主程序载入配置文件：

配置文件是放在哪里啊？这些与 grub2 有关的文件都放置到 /boot/grub2 中

grub2 的配置文件 /boot/grub2/grub.cfg 初探

grub2 配置文件维护 /etc/default/grub 与 /etc/grub.d

忘记root密码
文件系统错误无法开机

## x window设置介绍

## linux核心编译与管理
系统移植
编译前的任务：认识核心与取得核心源代码

这个核心文件通常被放置成 /boot/vmlinuz-xxx ，不过也不见得， 因为一部主机上面可以拥有 多个核心文件，只是开机的时候仅能选择一个来载入而已

自制核心 - 核心编译

关于驱动程序 - 是厂商的责任还是核心的责任

核心的编译重点在于“你要你的 Linux 作什么

核心的版本

核心源代码的解压缩/安装/观察

核心的编译与安装

开始安装新核心与多重核心菜单 （grub）

