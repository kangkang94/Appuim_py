#coding=utf-8
from appium import webdriver
#获取工程路径
import sys
sys.path.append('/Users/kang/Documents/github/Appuim_py')
from util.read_init import ReadIni
import time

capabilities = {
  "platformName": "Android",
  "deviceName": "9205C037",
  "appPackage": "cn.com.open.mooc",
  "appActivity": "com.imooc.component.imoocmain.splash.MCSplashActivity"

}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)


#页面滑动函数封装
#获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height

#向左滑
def swipe_left():
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1,y1,x,y1)
#向右滑
def swipe_right():
    x1 = get_size()[0]/10
    y1 = get_size()[1]/2
    x = get_size()[0]/10*9
    driver.swipe(x1,y1,x,y1)
#向上滑
def swipe_up():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10*5
    y = get_size()[1]/10*3
    driver.swipe(x1,y1,x1,y)
#向下滑
def swipe_down():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10
    y = get_size()[1]/10*9
    driver.swipe(x1,y1,x1,y)

def swipe_on(direnction):
    if direnction == 'up':
        swipe_up()
    elif direnction == 'down':
        swipe_down()
    elif direnction == 'left':
        swipe_left()
    else :
        swipe_right()

#id定位进行登录操作
def go_login():

    element = driver.find_element_by_id('cn.com.open.mooc:id/tab_layout')
    elements = element.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    elements[3].click()

    login = driver.find_element_by_id('cn.com.open.mooc:id/header_line')
    login.click();

    driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()

    ##输入手机号和密码
    driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('18525461587')
    driver.find_element_by_id('cn.com.open.mooc:id/password_edit').send_keys('92n38k817625')
    driver.find_element_by_id('cn.com.open.mooc:id/login').click()
    print('+++++++++++++++++++++++')

swipe_on('left')
time.sleep(1)
swipe_left()
time.sleep(1)
swipe_left()
time.sleep(1)
swipe_left()
time.sleep(1)
swipe_up()
time.sleep(7)
go_login()
time.sleep(7)