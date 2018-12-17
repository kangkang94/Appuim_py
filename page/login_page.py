#coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
class LoginPage:
    #获取登录页面所有的登录信息
    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        return self.get_by_local.get_element('password')

    def get_login_button_element(self):
        return self.get_by_local.get_element('login_button')