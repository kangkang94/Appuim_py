#coding=utf-8
from appium import webdriver
import time

from util.write_user_command import WriteUserCommand


class BaseDriver:
    def android_driver(self,i,appPackage,appActivity):
        #device_name
        #port
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_'+str(i),'deviceName')
        port = write_file.get_value('user_info_'+str(i),'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "appPackage": appPackage,
            #activity 选哪一个 要研究透彻 appAwaitActivity
            "appActivity": appActivity,
            #"unicodeKeyboard": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub",capabilities)
        return driver