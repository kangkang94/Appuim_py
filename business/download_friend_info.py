#coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
import time
from appium import webdriver

from util.get_clipboard import getClipboard
from util.get_from_phone import getFromPhone
from util.swipe_go import SwipeGo
from util.write_friend_info import WriteFriendInfo

class DoloadFriendInfo:
    def __init__(self,i,appPackage,appActivity):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i,appPackage,appActivity)
        self.get_by_local = GetByLocal(self.driver)
        self.get_clipboard = getClipboard()

        self.write_Friend_Info = WriteFriendInfo()
        self.get_size = SwipeGo(self.driver)



    def save_path(self,nickname):
        img_folder = "/Users/kang/Documents/github/Appuim_py/screenshots/"
        name = time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + nickname
        screen_save_path = img_folder + name + ".png"
        self.driver.get_screenshot_as_file(screen_save_path)



    def swipe_up_start(self):
        x1 = self.get_size.get_size()[0] / 2
        y1 = 810
        y = 10
        self.driver.swipe(x1, y1, x1, y, 10000)


    # 校正滑动距离
    def adjust_distance(self,y, height):
        if (y > 200) and (y < 300):
            height = height + 50

        if (y > 300) and (y < 400):
            height = height + 200
        if (y > 400) and (y < 500):
            height = height + 300
        return y, height


    # 获取朋友圈正文内容
    def get_view(self,element):
        try:
            text_view = element.find_element_by_id('com.tencent.mm:id/jv')
            t_x = text_view.location['x']
            t_y = text_view.location['y']
            self.driver.tap([(t_x + 100, t_y + 20)], 1000)
            time.sleep(2)
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("复制")').click()
            time.sleep(3)
            text = self.get_clipboard.get_cliptext()

        except:
            text = "用户没有发表正文信息"

        return text


    # 获取朋友圈图片或者朋友圈链接
    def get_picture(self,element):
        try:
            picture_Linear = element.find_element_by_id('com.tencent.mm:id/e21')
            try:
                view_1 = picture_Linear.find_element_by_id('com.tencent.mm:id/e3e')
                self.click_pictures(picture_Linear)
                picture_path = '/Users/kang/Documents/github/Appuim_py/screenshots/WeiXin'
                link = " "
                link_text = " "
            except:
                link_text = self.get_link_text(picture_Linear)
                link = self.get_link(picture_Linear)
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



    #从手机中拉取当前下载的图片并重命名-(注意 魅族手机和电脑的unix相差34秒)
    def pull_picture(self):
        get_from_phone = getFromPhone()

        nowtime = int(time.time())
        print(str(nowtime)+"#################################################################################")
        #注意 电脑的unix时间戳一定要和手机的unix时间戳一致
        for itime in range(nowtime-35,nowtime-33,1):
            get_from_phone.get_from_phone(itime, self.nickname)
        return (nowtime-34)

    # 点击图片,保存到sdcard/tencent/micromsg/WeiXin
    def click_pictures(self,picture_Linear):
        view_elements = picture_Linear.find_elements_by_class_name('android.view.View')
        for element_item in view_elements:

            element_item.click()
            time.sleep(2)
            self.driver.tap([(540, 860)], 1500)
            time.sleep(1)
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("保存图片")').click()

            version = self.pull_picture()
            time.sleep(2)
            self.driver.tap([(540, 860)], 300)
            time.sleep(2)

            print("图片保存出错了")
            time.sleep(2)


    # 点击链接 获取链接
    def get_link_text(element):
        try:
            link_text = element.find_element_by_id('com.tencent.mm:id/cot').text
        except:
            link_text = " "
        return link_text


    def get_link(self,element):
        try:
            element.find_element_by_id('com.tencent.mm:id/cot').click()
            time.sleep(5)
            self.driver.find_element_by_id('com.tencent.mm:id/j1').click()
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("复制链接")').click()
            self.driver.find_element_by_id('com.tencent.mm:id/jc').click()
            time.sleep(2)
            link = self.get_clipboard.get_cliptext()

        except:
            link = "没有获取到链接"
        return link


    def save_to_yaml(self,nickname,plainText,view_list):
        self.write_Friend_Info.write_data(nickname,plainText,view_list)

    def do_open(self):
         # 打开朋友圈
        footer = self.driver.find_elements_by_id('com.tencent.mm:id/cw2')
        footer[2].click()
        friend = self.driver.find_element_by_id('android:id/list')
        friend_list = friend.find_elements_by_class_name('android.widget.LinearLayout')
        friend_list[0].click()
        time.sleep(3)

        self.swipe_up_start()


    def do_business(self):
        element = self.driver.find_element_by_id('com.tencent.mm:id/e2p')
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
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 200) and (height < 300):
            height = height + 180
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 400) and (height < 500):
            height = height + 50
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 700) and (height < 900):
            height = height - 30
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 900) and (height < 1100):
            height = height - 50
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 1100) and (height < 1300):
            height = height - 100
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif height > 1300:
            height = height - 200
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            temp = y1 - 1920
            if y1 > 1919:
                y1 = 1910

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
            self.driver.swipe(x, 400 + (temp) + 600, x, 400, 2000)
            time.sleep(2)
        else:
            height = height
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)

    def down_info(self):
        element = self.driver.find_element_by_id('com.tencent.mm:id/e2p')
        frame_list = element.find_elements_by_class_name('android.widget.FrameLayout')

        try:
            y = frame_list[3].location['y']
            print(str(y) + "3333hhhhhh")
            self.nickname = frame_list[3].find_element_by_id('com.tencent.mm:id/azl').text
            time.sleep(1)
            plain_text = self.get_view(frame_list[3])
            time.sleep(1)
            view_list = self.get_picture(frame_list[3])
            height = frame_list[3].size['height']
            #保存数据
            self.save_to_yaml(self.nickname,plain_text,view_list)
        except:

            try:
                y = frame_list[2].location['y']
                print(str(y) + "3333hhhhhh")
                nickname = frame_list[2].find_element_by_id('com.tencent.mm:id/azl').text
                time.sleep(1)
                plain_text = self.get_view(frame_list[2])
                time.sleep(1)
                view_list = self.get_picture(frame_list[2])
                height = frame_list[2].size['height']
                #保存数据
                self.save_to_yaml(nickname,plain_text,view_list)
            except:

                y = frame_list[1].location['y']
                print(str(y) + "3333hhhhhh")
                nickname = frame_list[1].find_element_by_id('com.tencent.mm:id/azl').text
                time.sleep(1)
                plain_text = self.get_view(frame_list[1])
                time.sleep(1)
                view_list = self.get_picture(frame_list[1])
                height = frame_list[1].size['height']
                #保存数据
                self.save_to_yaml(nickname,plain_text,view_list)
        times = 5000
        print(height)

        if height < 200:
            height = height + 200
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 200) and (height < 300):
            height = height + 180
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 400) and (height < 500):
            height = height + 50
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 700) and (height < 900):
            height = height - 30
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 900) and (height < 1100):
            height = height - 50
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif (height > 1100) and (height < 1300):
            height = height - 100
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            if y1 > 1919:
                y1 = 1910
                times = 3000

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
        elif height > 1300:
            height = height - 200
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2
            temp = y1 - 1920
            if y1 > 1919:
                y1 = 1910

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)
            self.driver.swipe(x, 400 + (temp) + 600, x, 400, 500)
            time.sleep(2)
        else:
            height = height
            y = self.adjust_distance(y, height)[0]
            height = self.adjust_distance(y, height)[1]
            times = 4000
            y1 = y + height + 30
            x = self.get_size.get_size()[0] / 2

            self.driver.swipe(x, y1, x, y, times)
            time.sleep(2)

        #业务入口
    def do_business_download(self):
        self.do_open()
        var = 1
        self.do_business()

        while var == 1:

            self.down_info()














