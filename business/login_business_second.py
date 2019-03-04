#coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
import time
import threading
from apscheduler.schedulers.background import BackgroundScheduler
#业务层,直接在业务层写代码
class LoginBusinessSecond:
    def __init__(self,i,appPackage,appActivity):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i,appPackage,appActivity)
        self.get_by_local = GetByLocal(self.driver)
    def login_pass(self):

        self.driver.find_element_by_id('com.youku.phone:id/layout_user').click()
        time.sleep(1)

        self.driver.find_element_by_id('com.youku.phone:id/ucenter_user_pic').click()
        #self.driver.find_element_by_id('com.youku.phone:id/passport_login_type').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/passport_sms_login').click()
        time.sleep(1)

        self.driver.find_element_by_id('com.youku.phone:id/passport_username').send_keys('18525461587')
        self.driver.find_element_by_id('com.youku.phone:id/passport_password').send_keys('92n38k817625')
        self.driver.find_element_by_id('com.youku.phone:id/passport_login').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("上传")').click()
        time.sleep(1)
        try:
            self.driver.find_element_by_id('com.youku.phone:id/upload_video_btn').click()
        except:
            self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/upload_source_local_lin').click()
        time.sleep(1)
        element = self.driver.find_element_by_id('com.youku.phone:id/video_picker_recycleview')
        elements = element.find_elements_by_class_name('android.widget.LinearLayout')
        elements[1].find_element_by_id('com.youku.phone:id/container').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.youku.phone:id/video_cut_next').click()
        time.sleep(1)
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/video_upload').click()

        try:
            self.driver.find_element_by_id('com.youku.phone:id/upload_video_btn').click()
        except:
            self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/upload_source_local_lin').click()
        time.sleep(1)
        element = self.driver.find_element_by_id('com.youku.phone:id/video_picker_recycleview')
        elements = element.find_elements_by_class_name('android.widget.LinearLayout')
        elements[3].find_element_by_id('com.youku.phone:id/container').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.youku.phone:id/video_cut_next').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/edit_video_title').clear()
        self.driver.find_element_by_id('com.youku.phone:id/edit_video_title').send_keys('康宇航发布的视频')
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/video_upload').click()

        try:
            self.driver.find_element_by_id('com.youku.phone:id/upload_video_btn').click()
        except:
            self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()

        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/upload_source_local_lin').click()
        time.sleep(1)
        element = self.driver.find_element_by_id('com.youku.phone:id/video_picker_recycleview')
        elements = element.find_elements_by_class_name('android.widget.LinearLayout')
        elements[5].find_element_by_id('com.youku.phone:id/container').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.youku.phone:id/video_cut_next').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/edit_video_title').clear()
        self.driver.find_element_by_id('com.youku.phone:id/edit_video_title').send_keys('康宇航发布的视频')
        time.sleep(1)
        self.driver.find_element_by_id('com.youku.phone:id/video_upload').click()


    def save_path(self, i):

        img_folder = "/Users/kang/Desktop/phone"+str(i)+"/"
        screen_save_path = img_folder + str(i) + ".png"
        self.driver.get_screenshot_as_file(screen_save_path)



    def main(self):

        scheduler = BackgroundScheduler()
        scheduler.add_job(self.save_path,'interval',seconds=1,args=(0,))
        scheduler.start()

        self.login_pass()


