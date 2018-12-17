#coding=utf-8
from page.login_page import LoginPage


class LoginHandle:
    def __init__(self,i):
        self.login_page = LoginPage(i)
    #操作登录页面元素
    def send_username(self,username):
        self.login_page.get_username_element().send_keys(username)

    def send_password(self,password):
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        self.login_page.get_login_button_element().click()