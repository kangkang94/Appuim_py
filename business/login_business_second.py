#coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
import time
#业务层,直接在业务层写代码
class LoginBusinessSecond:
    def __init__(self,i,appPackage,appActivity):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i,appPackage,appActivity)
        self.get_by_local = GetByLocal(self.driver)
    def login_pass(self):

        self.driver.find_element_by_id('com.youku.phone:id/layout_user').click()


        self.driver.find_element_by_id('com.youku.phone:id/ucenter_user_pic').click()
        #self.driver.find_element_by_id('com.youku.phone:id/passport_login_type').click()

        self.driver.find_element_by_id('com.youku.phone:id/passport_username').send_keys('18525461587')
        self.driver.find_element_by_id('com.youku.phone:id/passport_password').send_keys('92n38k817625')
        self.driver.find_element_by_id('com.youku.phone:id/passport_login').click()
        time.sleep(1)

        self.driver.find_element_by_id('com.youku.phone:id/layout_home').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.youku.phone:id/home_tool_bar_search_frame').click()
        print(str(len(self.driver.find_elements_by_class_name('android.widget.EditText')))+"hhhhhhhhhhhhhhhhhhhhhh")
        element_list = self.driver.find_elements_by_class_name('android.widget.EditText')
        element_list[0].click()
        element_list[0].send_keys('火影忍者')
        #self.driver.find_element_by_id('com.youku.phone:id/et_widget_search_text_soku').send_keys('火影忍者')
        self.driver.find_element_by_id('com.youku.phone:id/suggestion_item_img').click()









