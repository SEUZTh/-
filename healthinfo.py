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
element.send_keys('一卡通号填这里')

element = wd.find_element_by_id('password')
element.send_keys('密码填这里\n')

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
