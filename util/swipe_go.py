#coding=utf-8

class SwipeGo:

    def __init__(self,driver):
        self.driver = driver
    #页面滑动函数封装
    #获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width,height
