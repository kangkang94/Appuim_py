#coding=utf-8
import os
import time
from appium import webdriver

from util.swipe_go import SwipeGo
from util.write_friend_info import WriteFriendInfo


def get_driver():
    capabilities = {
      "platformName": "Android",
      "deviceName": "95AQSCQ94JJGC",
      "appPackage": "com.tencent.mm",
        #activity 选哪一个 要研究透彻 appAwaitActivity
      "appActivity": "com.tencent.mm.ui.LauncherUI",
      "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
    return driver

driver = get_driver()
time.sleep(3)

count = 0;

write_Friend_Info = WriteFriendInfo()
get_size = SwipeGo(driver)

def save_path(nickname):
    img_folder = "/Users/kang/Documents/github/Appuim_py/screenshots/"
    name = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))+nickname
    screen_save_path = img_folder+name+".png"
    driver.get_screenshot_as_file(screen_save_path)
def save_path():
    img_folder = "/Users/kang/Documents/github/Appuim_py/screenshots/"
    name = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder+name+".png"
    driver.get_screenshot_as_file(screen_save_path)
def swipe_up_start():
    x1 = get_size.get_size()[0]/2
    y1 = 810
    y = 10
    driver.swipe(x1,y1,x1,y,10000)

def do_open():

    #打开朋友圈
    footer = driver.find_elements_by_id('com.tencent.mm:id/cw2')
    footer[2].click()
    friend = driver.find_element_by_id('android:id/list')
    friend_list = friend.find_elements_by_class_name('android.widget.LinearLayout')
    friend_list[0].click()
    time.sleep(3)

    swipe_up_start()

def do_business():



    element = driver.find_element_by_id('com.tencent.mm:id/e2p')
    frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')

    y = frame_list[0].location['y']
    print(str(y)+"hhhhhh")
    try:
        print(frame_list[0].find_element_by_id('com.tencent.mm:id/azl').text)
        height = frame_list[0].size['height']
    except:
        print(frame_list[0].find_element_by_id('com.tencent.mm:id/azl').text)
        height = frame_list[0].size['height']
    times = 5000
    print(height)

    if height <200:
        height = height +200
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height > 200) and (height <300):
        height = height +180
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height > 400) and (height <500):
        height = height +50
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height > 700) and (height <900):
        height = height -30
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height> 900) and (height <1100):
        height = height -50
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height> 1100) and (height <1300):
        height = height -100
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif height> 1300:
        height = height -200
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        temp = y1 - 1920
        if y1> 1919:
           y1 = 1910

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
        driver.swipe(x,400+(temp)+600,x,400,2000)
        time.sleep(2)
    else:
        height = height
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)


def do_business_merge():
    element = driver.find_element_by_id('com.tencent.mm:id/e2p')
    frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')

    try:
        y = frame_list[3].location['y']
        print(str(y)+"3333hhhhhh")
        print(frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text)
        height = frame_list[3].size['height']
    except:

        try:
            y = frame_list[2].location['y']
            print(str(y)+"2222hhhhhh")
            print(frame_list[2].find_element_by_id('com.tencent.mm:id/azl').text)
            height = frame_list[2].size['height']

        except:

            y = frame_list[1].location['y']
            print(str(y)+"1111hhhhhh")
            print(frame_list[1].find_element_by_id('com.tencent.mm:id/azl').text)
            height = frame_list[1].size['height']



    times = 5000
    print(height)

    if height <200:
        height = height +200
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height > 200) and (height <300):
        height = height +180
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height > 400) and (height <500):
        height = height +50
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height > 700) and (height <900):
        height = height -30
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height> 900) and (height <1100):
        height = height -50
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif (height> 1100) and (height <1300):
        height = height -100
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        if y1> 1919:
           y1 = 1910
           times = 3000

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
    elif height> 1300:
        height = height -200
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2
        temp = y1 - 1920
        if y1> 1919:
           y1 = 1910

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)
        driver.swipe(x,400+(temp)+600,x,400,500)
        time.sleep(2)
    else:
        height = height
        times = 4000
        y1 = y+height+30
        x = get_size.get_size()[0]/2

        driver.swipe(x,y1,x,y,times)
        time.sleep(2)



def do_business6():

    element = driver.find_element_by_id('com.tencent.mm:id/e2p')
    frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')
    #print(len(frame_list))
    #print(frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text)
    y31 = frame_list[3].location['y']
    print(str(y31)+"h6")
    try:
        print(frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text)
    except:
        v = 1
    height = frame_list[3].size['height']
    if height > 800:
        height = height-30
    y32 = y31+height+30
    print(height)
    x = get_size.get_size()[0]/2
    driver.swipe(x,y32,x,y31,10000)
    '''
    element = driver.find_element_by_id('com.tencent.mm:id/e2p')
    print(element)
    frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')
    print(len(frame_list))
    print(frame_list[0].find_element_by_id('com.tencent.mm:id/azl').text)
    print(frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text)
    print(frame_list[3].size['width'])
    print(frame_list[0].size['height'])

    for FrameLayout in frame_list:

        if FrameLayout == frame_list[0]:
            continue

        #说明为图片类型/小视频类型
        if len(FrameLayout.find_elements_by_class_name('android.widget.LinearLayout')) ==1:

            #获取名字
            name = FrameLayout.find_element_by_id('com.tencent.mm:id/azl').text

            try:
                #获取文本信息
                text = FrameLayout.find_element_by_id('com.tencent.mm:id/jv').text
            except:
                text = None

            write_Friend_Info.write_data(count,name,text,str("null"))
            count = count+1

            linearLayout = FrameLayout.find_element_by_id('com.tencent.mm:id/e21')
            #获取所有图片
            views_element = linearLayout.find_elements_by_class_name('android.view.View')

            for view_element in views_element:
                time .sleep(1)
                views_element.click()
                save_path(name)
                time.sleep(1)
                views_element.click()
                time.sleep(1)


        #说明为纯文字
        elif len(FrameLayout.find_elements_by_class_name('android.widget.LinearLayout')) == 0:

            try:
                #获取名字
                name = FrameLayout.find_element_by_id('com.tencent.mm:id/azl').text
            except:
                name = None
            try:
                #获取文本信息
                text = FrameLayout.find_element_by_id('com.tencent.mm:id/jv').text
            except:
                text = None

            write_Friend_Info.write_data(count,name,text,str("null"))
            count = count+1

        #LinearLayout >1 说明为链接类型
        else:
            continue

        '''


do_open()
var = 1

do_business()
'''
do_business1()
do_business2()
do_business3()
do_business4()
do_business5()
do_business6()
'''
while var ==1:
    do_business_merge()