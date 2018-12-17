#coding=utf-8
import os
import time
from appium import webdriver

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

def save_path():
    img_folder = "/Users/kang/Documents/github/Appuim_py/screenshots/"
    name = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder+name+".png"
    driver.get_screenshot_as_file(screen_save_path)

def do_business():

    #打开朋友圈
    footer = driver.find_elements_by_id('com.tencent.mm:id/cw2')
    footer[2].click()
    friend = driver.find_element_by_id('android:id/list')
    friend_list = friend.find_elements_by_class_name('android.widget.LinearLayout')
    friend_list[0].click()
    time.sleep(3)



    element = driver.find_element_by_id('com.tencent.mm:id/e2p')
    frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')

    for FrameLayout in frame_list:
        if len(FrameLayout.find_elements_by_class_name('android.widget.LinearLayout')) ==1:

            name = FrameLayout.find_element_by_id('com.tencent.mm:id/azl').text

            Linear_list = FrameLayout.find_elements_by_class_name('android.widget.LinearLayout')
            element_Linear = Linear_list[1]
            link_text = str(element_Linear.find_element_by_class_name('android.widget.TextView').text)
        elif len(FrameLayout.find_elements_by_class_name('android.widget.LinearLayout')) == 0:
            continue
        else:
            print("hhhgit 测试")






do_business()