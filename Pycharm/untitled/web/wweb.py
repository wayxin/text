#! /usr/bin/python
#- -*- coding:utf-8

#sesenium:是一个web 自动化的测试工具集，开元的自动化测试工具，由几个工具组成
#版本 ：sesenium1.0和2.0、3.0   （2.0余3.0的差别 不是很大）
#包含：sesenium IDE、sesenium GRID、sesenium RC
#为什么要用selenium：1.开源免费 2.多浏览器支持：火狐，谷歌，IE，Opera，Safari
#3.多语言支持：java，Python，ruby，PHP，C#，JavaScript 4.对web页面有良好支持 5.简单（API简单）

# IDE：是嵌入式的火狐浏览器中的一个插件，实现简单的浏览器操作的录制与回放功能
#应用场景：在测试人员测试的过程中，发现bug后可以通过IDE将重现的步骤录制下来，帮助开发人员更好的重现bug

#GRID：是一种自动化的测试辅助工具，可以方便的同时在不同的多台主机上和异构环境中并行运行多个测试事件
#特点：1.并行执行 2.通过主机统一控制用例在不同环境，不同浏览器下运行 3.灵活添加变动测试机

#RC：是selenium家族中的核心工具，支持不同的语言编写自动化测试脚本，负责控制浏览器行为
#  作用：针对各个浏览器而开发，通过原生浏览器或者浏览器扩展直接控制浏览器，简单来说就是集成了原生浏览器的所有接口直接控制浏览器
#   区别：selenium RC在浏览器中运行的JavaScript应用，使用浏览器内置的JavaScript翻译器来翻译和执行自动化脚本



# from selenium import webdriver
# import time
# #定义一个打开的浏览器
# re=webdriver.Firefox()
# #请求的网页
# re.get('https://www.baidu.com')
# #休眠两秒
# time.sleep(5.0)
# #在上一级的网页中，进入到下一个网页
# re.get('https://www.jd.com')
# time.sleep(2.0)
# #返回到上一级网页
# re.back()
# time.sleep(5.0)
# #前进到下一个网页
# re.forward()
#
# #关闭浏览器
# re.quit()
# #获取网页标题,一般用在断言，判断请求到的标题是否符合预期结果
# print(re.title)
# #获取请求的网址
# print(re.current_url)
#设置浏览器窗口大小
# re.set_window_size(600,600)
# #设置浏览器窗口的位置，默认产生的位置在左上角
# re.set_window_position(400,400)
# #最大化浏览器
# re.maximize_window()
# time.sleep(5.0)
# #最小化浏览器
# re.minimize_window()





# from selenium import webdriver
# from time import sleep
# re=webdriver.Firefox()
# re.get('https://www.baidu.com')
# sleep(2.0)
# #1.id定位
# #1.1、在输入框中输入
# # re.find_element_by_id('kw').send_keys('BOSS直聘')
# # 1.2、点击跳转
# # re.find_element_by_id('su').click()
#
# # 2.class定位  为了与Python中class区分，取为class name  定位是要保证class的值思唯一的
# # re.find_elements_by_class_name('mnav')[0].click()
#
# #3.name定位, 通过name定位 注意要保证文本的唯一性  该输入用send_keys，该点击用click
# # re.find_element_by_name('wd').send_keys('boss直聘')
# # re.find_element_by_id('su').click()
#
# #4.text定位 通过文本来定位    用link_text,注意要保证文本的唯一性
# # re.find_element_by_link_text('hao123').click()
#
# # 5 partial link text 模糊文本定位,注意保证文本的唯一性
# # re.find_element_by_partial_link_text('hao').click()
#
# #6.tag_name 通过标签页名称来定位,不能作为唯一的来定位，可以定位多个
# # re.find_element_by_tag_name()
#
# #7.xpath   通过路径定位   xpath是路径标记语言
# # re.find_element_by_xpath('//*[@id="kw"]').send_keys('boss直聘')
#
# #8.css 通过层叠样式表定位
# # re.find_element_by_css_selector('#kw').send_keys('boss')
#
# # 动作：1.send_keys（） 输入
# #       2.click（）  点击
# #       3.clear（） 清除
# #       4.text（） 文本
# #
# sleep(5.0)
# re.quit()



# from selenium import webdriver
# from time import sleep
# re=webdriver.Firefox()
# re.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# sleep(2.0)
# # re.switch_to.frame('login_frame')
# # 定位一组  element后要跟s就是定位一组
# # re.find_elements_by_id()
# #层级定位：先定位一个顶层元素，在定位这个元素下面的元素,多用于复杂的定位场景
# #是一组的时候要赋给一个变量
# qq=re.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')
# for i in qq:
#     i.click()
#     sleep(2.0)


#弹出框
# from selenium import webdriver
# from time import sleep
# qq=webdriver.Firefox()
# qq.get('file:///C:/Users/wyx/Desktop/abc.html')
# sleep(5.0)
# qq.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# #将鼠标切换到弹出框
# ww=qq.switch_to_alert()
# #获取弹出框上的文本
# print(ww.text)
# #点击确定
# # ww.accept()
# #点击取消
# # ww.dismiss()
# #输入数据
# ww.send_keys('baizp')
# sleep(2.0)
# ww.accept()



# from selenium import webdriver
# from time import sleep
# qq=webdriver.Firefox()
# qq.get('https://qzone.qq.com/')
# sleep(5.0)
# # iframe 网页框架，切换到框架 通过id、name切换或者先定位到框架(通过xpath或者CSS)
# #有多个框架是，要一级一级的切换
# ww=qq.find_element_by_xpath('//*[@id="login_frame"]')
# qq.switch_to.frame(ww)
# sleep(2.0)
# #退出框架,退出到最开始的页面
# # qq.switch_to_default_content()
# # sleep(2)
# #多个框架时，切换到上一级框架
# qq.switch_to.parent_frame()
# sleep(2)

# qq.find_element_by_id('login_button').click()

# sleep(5.0)
# qq.quit()


from selenium import webdriver
from time import sleep
qq=webdriver.Firefox()
qq.get('https://movie.douban.com/')  #一号窗口
sleep(5.0)
#获取 当前窗口的标识
# print(qq.current_window_handle)
qq.find_element_by_xpath('/html/body/div[1]/div/div[3]/ul/li[2]/a').click()  #二号窗口
#获取所有窗口的标识
sleep(2)
aa=qq.window_handles
print(aa)
#切换窗口  浏览器本身是无法决定在什么时候打开哪一个窗口
#是按照窗口打开的顺序进行对窗口标号---唯一标识窗口的字符串
qq.switch_to_window(aa[-1])
print(qq.title)


