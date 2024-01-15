---
title: ngrok设置服务器外网访问
tags:
  - ngrok内网穿透
  
date: 2019-06-03 20:43:48
abbrlink: 79cqj
---
Bash
dash
zsh


#可以把实验室服务器上的80端口 即gitlab映射出来
#用这种方法可以将其他端口 如jupyter notebook映射出来
./ngrok -config=ngrok.cfg -subdomain xxx 80


#通过ssh外网访问
./ngrok -config=ngrok.cfg -proto=tcp 22
ssh -p 端口 username@0.tcp.ngrok.ibanzhuan.cn


scp -r  ./linux64 zhangxuefeng@192.168.3.234:/home/zhangxuefeng

nohup

- ubuntu安装软件命令
sudo  apt-get install foo
dpkg -i *.deb
wget http://*

- ubuntu卸载软件命令
sudo apt-get --purge remove foo
sudo  apt-get remove  foo


解决依赖问题
sudo apt-get install -f

创建conda虚拟环境
conda create -n name python=3.5

进入环境
source activate test
退出环境
source deactivate

删除环境： 
conda remove --name env_pytorch --all

检查cuda版本
cat /usr/local/cuda/version.txt

conda install tensorflow-gpu=1.8.0

安装opencv

conda install --channel https://conda.anaconda.org/menpo opencv3

>Anaconda安装Pytorch         （还没成功 还要再尝试）
添加Anaconda的TUNA镜像
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
设置搜索时显示通道地址
  conda config --set show_channel_urls yes

  conda install pytorch torchvision -c soumith

[远程访问服务器Jupyter Notebook的方法](https://www.jianshu.com/p/8fc3cd032d3c)

查看已安装的conda环境
conda info -e

学习IDEA配置maven

配置大数据环境

kali linux 渗透测试系统 

黑客教程 腾讯课堂

关于jupyter notebook的一些事情

装插件 
python3.7 -m pip install jupyter_contrib_nbextensions


import sys
print(sys.executable)

装有关内核的东西
pip install ipykernel --user

python -m ipykernel install --user

pip install --upgrade pip
<!-- 
将当前环境加入内核     这是系统的环境
sudo python3.5 -m ipykernel install --name tf_python3.5


将我自己的环境加入方法

先看anaconda环境
conda info -e

# conda environments:
#
base                     /home/zhangxuefeng/anaconda3
tf_python3            *  /home/zhangxuefeng/anaconda3/envs/tf_python3


再用下面的命令 -->

conda install nb_conda






source ~/.bashrc

安装pytorch
[pytorch官网](https://pytorch.org/)

conda install pytorch torchvision cudatoolkit=9.0 -c pytorch


换源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes


conda config --prepend channels http://mirrors.ustc.edu.cn/anaconda/pkgs/free/


win10关机后自动重启解决办法

关机后电脑自动重启解决办法： 
- 开始/运行/输入 regedit 回车，打开注册表编辑器，依次展开[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Window NT\Currentversion\Winlgon] 然后在右侧新建或修改已有的一个名称为＂PowerdownAfterShutdown＂的字符串值,其值＂1＂表示关机时关闭计算机电源,0表示重新启动电脑。　 
- 如果是因为网络唤醒引起的，双击本地连接选属性/配置/高级/在左侧选关机网络唤醒，在右侧选关闭确定。


pip install -r requirements.txt



方法1 在python程序中

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
 方法2，运行时 

CUDA_VISIBLE_DEVICES=1 python   **.py



conda install cudatoolkit=9.0


#  Anaconda 安装pygame
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygame
