#coding=utf-8
import os
import time
from appium import webdriver

from util.get_clipboard import getClipboard
from util.swipe_go import SwipeGo
from util.write_friend_info import WriteFriendInfo


def get_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "192.168.1.130:5555",
        "appPackage": "com.tencent.mm",
        # activity 选哪一个 要研究透彻 appAwaitActivity
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": "true",
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver


driver = get_driver()
time.sleep(3)

get_clipboard = getClipboard()

write_Friend_Info = WriteFriendInfo()
get_size = SwipeGo(driver)


def save_path(nickname):
    img_folder = "/Users/kang/Documents/github/Appuim_py/screenshots/"
    name = time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + nickname
    screen_save_path = img_folder + name + ".png"
    driver.get_screenshot_as_file(screen_save_path)


def save_path():
    img_folder = "/Users/kang/Documents/github/Appuim_py/screenshots/"
    name = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + name + ".png"
    driver.get_screenshot_as_file(screen_save_path)


def swipe_up_start():
    x1 = get_size.get_size()[0] / 2
    y1 = 810
    y = 10
    driver.swipe(x1, y1, x1, y, 10000)


# 校正滑动距离
def adjust_distance(y, height):
    if (y > 200) and (y < 300):
        height = height + 50

    if (y > 300) and (y < 400):
        height = height + 200
    if (y > 400) and (y < 500):
        height = height + 300
    return y, height


# 获取朋友圈正文内容
def get_view(element):
    try:
        text_view = element.find_element_by_id('com.tencent.mm:id/jv')
        t_x = text_view.location['x']
        t_y = text_view.location['y']
        driver.tap([(t_x + 100, t_y + 20)], 1000)
        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("复制")').click()
        time.sleep(3)
        text = get_clipboard.get_cliptext()

    except:
        text = "用户没有发表正文信息"

    return text


# 获取朋友圈图片或者朋友圈链接
def get_picture(element):
    try:
        picture_Linear = element.find_element_by_id('com.tencent.mm:id/e21')
        try:
            view_1 = picture_Linear.find_element_by_id('com.tencent.mm:id/e3e')
            click_pictures(picture_Linear)
            picture_path = '/Users/kang/Documents/github/Appuim_py/screenshots/WeiXin'
            link = " "
            link_text = " "
        except:
            link_text = get_link_text(picture_Linear)
            link = get_link(picture_Linear)
            print("这是链接-----" + link_text)
            print(link)
            picture_path = " "

        print(str(len(picture_Linear.find_elements_by_class_name('android.view.View'))) + "图片数量")
        print(str(len(picture_Linear.find_elements_by_class_name('android.widget.LinearLayout'))) + "链接是否正常")

    except:
        print("没有识别到图片")
        picture_path = " "
        link_text = " "
        link = " "

    return picture_path, link_text, link


# 点击图片,保存到sdcard/tencent/micromsg/WeiXin
def click_pictures(picture_Linear):
    view_elements = picture_Linear.find_elements_by_class_name('android.view.View')
    for element_item in view_elements:
        try:
            element_item.click()
            time.sleep(2)
            driver.tap([(540, 860)], 1500)
            time.sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().text("保存图片")').click()
            time.sleep(1)
            driver.tap([(540, 860)], 300)
            time.sleep(1)
        except:
            print("图片保存出错了")
        time.sleep(3)


# 点击链接 获取链接
def get_link_text(element):
    try:
        link_text = element.find_element_by_id('com.tencent.mm:id/cot').text
    except:
        link_text = " "
    return link_text


def get_link(element):
    try:
        element.find_element_by_id('com.tencent.mm:id/cot').click()
        time.sleep(5)
        driver.find_element_by_id('com.tencent.mm:id/j1').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("复制链接")').click()
        driver.find_element_by_id('com.tencent.mm:id/jc').click()
        time.sleep(2)
        link = get_clipboard.get_cliptext()

    except:
        link = "没有获取到链接"
    return link


def save_to_yaml(nickname,plainText,view_list):
    write_Friend_Info.write_data(nickname,plainText,view_list)


def do_open():
    # 打开朋友圈
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
    print(len(frame_list))
    y = frame_list[0].location['y']
    print(str(y) + "hhhhhh")
    try:
        print(frame_list[0].find_element_by_id('com.tencent.mm:id/azl').text)
        height = frame_list[0].size['height']
    except:
        print(frame_list[0].find_element_by_id('com.tencent.mm:id/azl').text)
        height = frame_list[0].size['height']
    times = 5000
    print(height)

    if height < 200:
        height = height + 200
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 200) and (height < 300):
        height = height + 180
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 400) and (height < 500):
        height = height + 50
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 700) and (height < 900):
        height = height - 30
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 900) and (height < 1100):
        height = height - 50
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 1100) and (height < 1300):
        height = height - 100
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif height > 1300:
        height = height - 200
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        temp = y1 - 1920
        if y1 > 1919:
            y1 = 1910

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
        driver.swipe(x, 400 + (temp) + 600, x, 400, 2000)
        time.sleep(2)
    else:
        height = height
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)


def do_business_merge():
    element = driver.find_element_by_id('com.tencent.mm:id/e2p')
    frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')

    try:
        y = frame_list[3].location['y']
        print(str(y) + "3333hhhhhh")
        nickname = frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text
        time.sleep(1)
        plain_text = get_view(frame_list[3])
        time.sleep(1)
        view_list = get_picture(frame_list[3])
        height = frame_list[3].size['height']
        #保存数据
        save_to_yaml(nickname,plain_text,view_list)
    except:

        try:
            y = frame_list[2].location['y']
            print(str(y) + "3333hhhhhh")
            nickname = frame_list[2].find_element_by_id('com.tencent.mm:id/azl').text
            time.sleep(1)
            plain_text = get_view(frame_list[2])
            time.sleep(1)
            view_list = get_picture(frame_list[2])
            height = frame_list[2].size['height']
            #保存数据
            save_to_yaml(nickname,plain_text,view_list)
        except:

            y = frame_list[1].location['y']
            print(str(y) + "3333hhhhhh")
            nickname = frame_list[1].find_element_by_id('com.tencent.mm:id/azl').text
            time.sleep(1)
            plain_text = get_view(frame_list[1])
            time.sleep(1)
            view_list = get_picture(frame_list[1])
            height = frame_list[1].size['height']
            #保存数据
            save_to_yaml(nickname,plain_text,view_list)
    times = 5000
    print(height)

    if height < 200:
        height = height + 200
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 200) and (height < 300):
        height = height + 180
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 400) and (height < 500):
        height = height + 50
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 700) and (height < 900):
        height = height - 30
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 900) and (height < 1100):
        height = height - 50
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif (height > 1100) and (height < 1300):
        height = height - 100
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        if y1 > 1919:
            y1 = 1910
            times = 3000

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
    elif height > 1300:
        height = height - 200
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2
        temp = y1 - 1920
        if y1 > 1919:
            y1 = 1910

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)
        driver.swipe(x, 400 + (temp) + 600, x, 400, 500)
        time.sleep(2)
    else:
        height = height
        y = adjust_distance(y, height)[0]
        height = adjust_distance(y, height)[1]
        times = 4000
        y1 = y + height + 30
        x = get_size.get_size()[0] / 2

        driver.swipe(x, y1, x, y, times)
        time.sleep(2)


def do_business6():
    element = driver.find_element_by_id('com.tencent.mm:id/e2p')
    frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')
    # print(len(frame_list))
    # print(frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text)
    y31 = frame_list[3].location['y']
    print(str(y31) + "h6")
    try:
        print(frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text)
    except:
        v = 1
    height = frame_list[3].size['height']
    if height > 800:
        height = height - 30
    y32 = y31 + height + 30
    print(height)
    x = get_size.get_size()[0] / 2
    driver.swipe(x, y32, x, y31, 10000)


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
while var == 1:
    do_business_merge()
