#coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
import time
#业务层,直接在业务层写代码
class DownloadBusiness:
    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)












