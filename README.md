- [0. 准备](#0---)
- [1. 自动上报脚本](#1-------)
- [2. Win10每日定时执行python脚本](#2-win10------python--)
  * [-1-](#-1-)
  * [-2-](#-2-)
  * [-3-](#-3-)
  * [-4-](#-4-)
- [2021.02.16更新](#20210216--)


# 0. 准备
适用于**车大SEU**每日健康上报系统。
- - -
- win10系统
- Python3
- - -
以下内容的安装参考：[http://www.python3.vip/tut/auto/selenium/01/](http://www.python3.vip/tut/auto/selenium/01/)
- Chrome浏览器
- 对应版本Chrome浏览器的**Chrome浏览器驱动**
- **selenium**（一个Python的库）
# 1. 自动上报脚本
脚本文件可命名为```healthinfo.py```
==代码中标记的两处需要输入自己的一卡通账号和密码==。
- 1.0代码（会打开浏览器界面）
```python
from selenium import webdriver

wd = webdriver.Chrome()

# 设置最大等待时长为 10秒
wd.implicitly_wait(10)

# 打开每日健康上报登录页
wd.get('http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do#/dailyReport')

# 输入一卡通号和密码并回车登录
element = wd.find_element_by_id('username')
element.send_keys('') # 引号中间输入一卡通号

element = wd.find_element_by_id('password')
element.send_keys('\n') # \n前面输入密码

# 点击添加健康上报信息
# 根据属性选择元素
elements = wd.find_elements_by_css_selector('button[class="mint-button geuhjrnk bottom155 mt-btn-primary mint-button--normal"]') # 点击新增按钮
for element0 in elements:
    try:
        if element0.text == "新增":
            element0.click()
            # 输入体温
            element1 = wd.find_element_by_css_selector('input[placeholder="请输入当天晨检体温"]')
            element1.send_keys('36')
            print("已输入体温！\n")
            # 点击提交
            wd.find_element_by_css_selector('button[class="mint-button mt-btn-primary mint-button--large"]').click() # 点击提交按钮
            # 点击弹窗确定
            wd.find_element_by_css_selector('button[class="mint-msgbox-btn mint-msgbox-confirm mt-btn-primary"]').click() # 点击确定按钮
            print("已提交健康表单")
            # 关闭浏览器
            wd.quit()
    except:
        wd.quit()
        print("警告：当日已上报，请勿重复！")
        break

```
- 1.1代码（不打卡浏览器界面）
```python
from selenium import webdriver

# 不打开浏览器页面
option = webdriver.ChromeOptions()
option.add_argument("headless")
wd = webdriver.Chrome(chrome_options=option)

# 设置最大等待时长为 10秒
wd.implicitly_wait(10)

# 打开每日健康上报登录页
wd.get('http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do#/dailyReport')

# 输入一卡通号和密码并回车登录
element = wd.find_element_by_id('username')
element.send_keys('') # 引号中间输入一卡通号

element = wd.find_element_by_id('password')
element.send_keys('\n') # \n前面输入密码

# 点击添加健康上报信息
# 根据属性选择元素
elements = wd.find_elements_by_css_selector('button[class="mint-button geuhjrnk bottom155 mt-btn-primary mint-button--normal"]') # 点击新增按钮
for element0 in elements:
    try:
        if element0.text == "新增":
            element0.click()
            # 输入体温
            element1 = wd.find_element_by_css_selector('input[placeholder="请输入当天晨检体温"]')
            element1.send_keys('36')
            print("已输入体温！\n")
            # 点击提交
            wd.find_element_by_css_selector('button[class="mint-button mt-btn-primary mint-button--large"]').click() # 点击提交按钮
            # 点击弹窗确定
            wd.find_element_by_css_selector('button[class="mint-msgbox-btn mint-msgbox-confirm mt-btn-primary"]').click() # 点击确定按钮
            print("已提交健康表单")
            # 关闭浏览器
            wd.quit()
    except:
        wd.quit()
        print("警告：当日已上报，请勿重复！")
        break

```
# 2. Win10每日定时执行python脚本
## -1- 
按下==“Win键”加“s键”==，搜索“计算机管理”
## -2-
点击==“创建基本任务”==
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210130162959228.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0MzI0MTgx,size_16,color_FFFFFF,t_70)
## -3-
在python脚本所在的文件夹下，创建一个txt文件，里面写上：```python healthinfo.py```。
然后重命名为“==healthinfo.bat==”

## -4-
- 名称：自定义一个
- 触发器：每天执行
	- 每日：填你需要它几点执行
- 操作：启动程序
	- 程序或脚本：填“==healthinfo.bat==”前面加上绝对路径名（右键文件点击属性可查到路径）
	- 起始于：填==bat==文件的绝对路径名

# 2021.02.16更新
最近程序运行时经常报错，无法正常上报体温，已经连续两天被导员打电话催命了。
错误如下：
```bash
selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <button class="mint
element click intercepted: Element <button class="mint-button geuhjrnk<div class="mint-indicator-mask"></div> bottom155 mt-btn-primary mint-button--normal">...</button> is not clickable at point (875, 725). Other element would receive the click: <div class="mint-indicator-mask"></div>
```
经调试，问题在于访问网站服务器速度很慢，相应网页元素还未出现，考虑增加```sleep()```休眠来解决，更新后的代码如下：

```python
from selenium import webdriver
from time import sleep
import selenium as sl

# wd = webdriver.Chrome() # 打开浏览器页面的方式

# 不打开浏览器页面
option = webdriver.ChromeOptions()
option.add_argument("headless")
wd = webdriver.Chrome(chrome_options=option)

# 设置最大等待时长为 10秒
wd.implicitly_wait(10)

# 打开每日健康上报登录页
wd.get('http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do#/dailyReport')

# 输入一卡通号和密码并回车登录
element = wd.find_element_by_id('username')
element.send_keys('')

element = wd.find_element_by_id('password')
element.send_keys('\n')

# 点击添加健康上报信息
# 根据属性选择元素
try:
    elements = wd.find_elements_by_css_selector('button[class="mint-button geuhjrnk bottom155 mt-btn-primary mint-button--normal"]') # 点击新增按钮
    for element0 in elements:
        if element0.text == '新增':
            sleep(1)
            element0.click()
            # 输入体温
            element1 = wd.find_element_by_css_selector('input[placeholder="请输入当天晨检体温"]')
            element1.send_keys('36')
            print("已输入体温！\n")
            # 点击提交
            wd.find_element_by_css_selector('button[class="mint-button mt-btn-primary mint-button--large"]').click() # 点击提交按钮
            # 点击弹窗确定
            wd.find_element_by_css_selector('button[class="mint-msgbox-btn mint-msgbox-confirm mt-btn-primary"]').click() # 点击确定按钮
            print("已提交健康表单")
            # 关闭浏览器
            wd.quit()
except sl.common.exceptions.StaleElementReferenceException:
    print("警告：当日已上报，请勿重复！")       

```
