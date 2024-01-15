---
title: python开发图床工具
tags:
  - 搭建博客
  - 前端
date: 2021-12-09 21:21:28
abbrlink: 81qzl
---

# picGo传输图片有数量限制所以自己设计用python开发了一个图床工具
## 1 在gitee创建仓库和令牌

## 2 本地用360浏览器截图并保存到固定文件夹中，由于文件夹按顺序排序，python获取文件夹最后一个图片即为刚刚截图的图片，用requests调用方法将图片传到gitee仓库


## 3 用tkinter做图形化界面，加按钮监听调用方法，同时返回需要的字符串，清空剪贴板，将字符串复制到剪贴板中。之后可用pyinstaller将python制作成exe文件运行
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211209213641555.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211209214101301.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211209214231783.jpg)
## 4 源代码

```
import sys
import base64
import hashlib
import datetime
import requests
import urllib.parse
import os
import tkinter
import tkinter.messagebox
from tkinter import *

def main():
    token = gitee的token令牌
    owner = 'mosheng123456789'
    repo = 'pics'
    message = 'personal'
    image_list=os.listdir('D:/newcoder-test/img')
    
    with open('D:/newcoder-test/img/'+image_list[-1], "rb") as f:
        content = base64.b64encode(f.read())
    data = {'access_token': token, 'message': message, 'content': content}
    path = 'img/'+image_list[-1]
    res = requests.post('https://gitee.com/api/v5/repos/' + owner + '/' + repo +'/contents/'+ path, data)

    if res.status_code == 201 or res.text == '{"message":"文件名已存在"}':
        tkinter.messagebox.showinfo('提示', '图片上传成功')

        print('https://gitee.com/' + owner + '/' + repo + '/raw/master/' + path)
        str='![]('+'https://gitee.com/' + owner + '/' + repo + '/raw/master/' + path+')'
        # l1 = Entry(top, text=str)     #输入框

        # l1 = Label(top, text='图片上传成功')
        # l1.pack(side=BOTTOM)
        # top.withdraw()
        top.clipboard_clear()
        top.clipboard_append(str)
    else:
        tkinter.messagebox.showinfo('提示', '图片上传失败')
        
top = tkinter.Tk()
top.geometry("500x400")
top.title('python开发图床工具')
B = tkinter.Button(top, text ="上传截图图片", command = main)
B.pack()
# 进入消息循环
top.mainloop()
```

