#coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
import time
#业务层,直接在业务层写代码
class LoginBusiness:
    def __init__(self,i,appPackage,appActivity):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i,appPackage,appActivity)
        self.get_by_local = GetByLocal(self.driver)
    def login_pass(self):

        #通过resourceId定位
        element = self.driver.find_element_by_id('cn.com.open.mooc:id/tab_layout')
        print(element)
        #层级定位方式 通过classname(控件类型) 定位 再通过索引查找
        elements = element.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
        elements[3].click()

        login = self.driver.find_element_by_id('cn.com.open.mooc:id/header_line')
        login.click()

        #self.driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()

        time.sleep(1)
        ##输入手机号和密码
        self.get_by_local.get_element('username').send_keys('18525461587')
        time.sleep(1)
        self.get_by_local.get_element('password').send_keys('92n38k817625')
        time.sleep(1)
        self.get_by_local.get_element('login_button').click()
        time.sleep(2)
        print('+++++++++++++++++++++++')

        #回到我的课程里点击java入门第一季
        #通过resourceId定位
        element_1 = self.driver.find_element_by_id('cn.com.open.mooc:id/tab_layout')
        print(element)
        #层级定位方式 通过classname(控件类型) 定位 再通过索引查找
        elements_1 = element_1.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
        elements_1[2].click()
        time.sleep(1)

        #点击我的收藏
        '''
        element_store = self.driver.find_element_by_id('cn.com.open.mooc:id/recyclerView')
        print(element)
        #层级定位方式 通过classname(控件类型) 定位 再通过索引查找
        elements_center = element_store.find_elements_by_class_name('android.view.View')
        elements_center_list=elements_center[4].find_element_by_id('cn.com.open.mooc:id/parent')
        elements_center_list[0].click()
        time.sleep(1)
        '''
        self.driver.find_element_by_id('cn.com.open.mooc:id/featureItemName').click()
        time.sleep(1)
        self.driver.find_element_by_id('cn.com.open.mooc:id/iv_course_icon').click()
        time.sleep(1)
        self.driver.find_element_by_id('cn.com.open.mooc:id/iv_add').click()
        self.driver.find_element_by_id('cn.com.open.mooc:id/ll_download_layout').click()
        time.sleep(1)
        self.driver.find_element_by_id('cn.com.open.mooc:id/tv_select_all').click()
        time.sleep(1)
        self.driver.find_element_by_id('cn.com.open.mooc:id/download_tv').click()









