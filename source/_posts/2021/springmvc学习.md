---
title: springmvc学习
tags:
  - 搭建博客
  - 前端
date: 2021-12-20 11:24:43
abbrlink: 822r0
---
DispatcherServlet
Servlet
@Controller 
@RequestMapping
@Scope
@RequestParam(name="")   defaultValue  required

重定向  改变浏览器url
转发   不改变浏览器url
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220120428533.jpg)
HttpServletRequest
HttpServletResponse
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220120756004.jpg)

redirct 重定向
forward 转发    默认转发
视图解析器与中文乱码问题
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220122325451.jpg)
视图解析器对重定向无效 只对转发有效
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220122624117.jpg)

过滤器
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220123045633.jpg)
配置过滤器      字符编码过滤器  CharsetEncoderFilter
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220123257827.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220123554021.jpg)
带数据与统一异常处理问题

# 1
request.setAttribute("user",user);
通过request域来保存数据   ${requestScope.user}

# 2
model.addAttribute("user",user);    实际封装了request
通过request域来保存数据   ${requestScope.user}

# 3 通过map集合带数据 Map<String,Object>map     map集合存在于request
map.put("aaa","ssss");
${requestScope.aaa}

只能处理当前Controller异常
@ExceptionHandler(Exception.class)   ArithmeticException   精确匹配

统一异常处理 用@ControllerAdvice注解

json   @ResponseBody
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220133124912.jpg)

实体类转化为json

Map集合转化为json

List集合转化为json

返回boolean int

单文件上传
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220134126406.jpg)
导入jar包
fileupload和io包
springmvc.xml配置
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220134259916.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220134643241.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220135007001.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220135513667.jpg)

pageContext request  session  application
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220135953013.jpg)
ServletContext

UUID   网卡号 时间戳
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220140636734.jpg)
多文件上传

数据校验  @Valid BindingResult
@Pattern(regexp="",message="")

正则表达式 可读性差

导入校验jar包

配置
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220141624128.jpg)
@Valid         BindingResult  (校验错误信息封装)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220142223896.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220142514234.jpg)
任务定时器
task

配置定时器   Cron表达式    秒 分 时 天  月 周 年
@Scheduled(Cron="")
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220143011954.jpg)
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220143309123.jpg)

SimpleDateFormat

HttpClient

数据回显 错误处理页面   404 500处理页面

拦截器  implements HandlerIntercepter
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220150935209.jpg)

springmvc配置拦截器
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220152549497.jpg)

![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220153238373.jpg)

数据交互   json
RequestBody
ResponseBody

onsubmit事件
![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220155949624.jpg)


![](https://gitee.com/mosheng123456789/pics/raw/master/img/360截图20211220160738534.jpg)

ajaxs


HandlerMapping   映射器
HandlerAdapter   适配器




过滤器和拦截器区别

https://blog.csdn.net/aoxiangzhe/article/details/90399909


springmvc  9个内置对象 4个作用域
https://blog.csdn.net/Miracle_Gaaral/article/details/99863769
