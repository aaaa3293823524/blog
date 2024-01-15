---
layout: git
title: stash用法
date: 2022-06-23 16:48:15
tags:
abbrlink: 87sk0
---
使用场景：
当我们正在修改某个文件的时候，突然当前这个文件有另外一个bug需要马上修复并上线，而当前的修改的功能还没有完善不能直接提交，此时有两种办法可以解决
一、新建分支，将当前的修改功能转移到新的分支上，等待后续完善再合并回来
二、使用临时保存，git stash 将当前修改的功能临时存储在本地，等到后期恢复再继续完善

基本使用方法：

1、git stash save " stash remark "  存储的时候增加一个备注
2、当要恢复继续完善的时候 git stash pop / git stash apply 就可以恢复到当前的工作目录


其他命令：

（1）git stash save "save message"  : 执行存储时，添加备注，方便查找，只有git stash 也要可以的，但查找时不方便识别。

（2）git stash list  ：查看stash了哪些存储

（3）git stash show ：显示做了哪些改动，默认show第一个存储,如果要显示其他存贮，后面加stash@{$num}，比如第二个 git stash show stash@{1}

（4）git stash show -p : 显示第一个存储的改动，如果想显示其他存存储，命令：git stash show  stash@{$num}  -p ，比如第二个：git stash show  stash@{1}  -p

（5）git stash apply :应用某个存储,但不会把存储从存储列表中删除，默认使用第一个存储,即stash@{0}，如果要使用其他个，git stash apply stash@{$num} ， 比如第二个：git stash apply stash@{1} 

（6）git stash pop ：命令恢复之前缓存的工作目录，将缓存堆栈中的对应stash删除，并将对应修改应用到当前的工作目录下,默认为第一个stash,即stash@{0}，如果要应用并删除其他stash，命令：git stash pop stash@{$num} ，比如应用并删除第二个：git stash pop stash@{1}

（7）git stash drop stash@{$num} ：丢弃stash@{$num}存储，从列表中删除这个存储

（8）git stash clear ：删除所有缓存的stash