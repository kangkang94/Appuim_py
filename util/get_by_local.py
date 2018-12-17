#coding=utf-8
from util.read_init import ReadIni

class GetByLocal:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_init = ReadIni()
        local = read_init.get_value(key)
        if local != None:
            type = local.split('>')[0]
            element = local.split('>')[1]
            if type == 'id':
                return self.driver.find_element_by_id(element)
            elif type == 'classname':
                return self.driver.find_element_by_class_name(element)
        else:
            print("从LocalElement.ini文件中读取不到定位元素")
            return None