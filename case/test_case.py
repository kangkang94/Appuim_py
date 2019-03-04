# coding=utf-8
import unittest
import threading
import multiprocessing
from appium import webdriver
import time

from GUI import monitor
from GUI.monitor import Monitor
from base.base_driver import BaseDriver
from business.download_business import DownloadBusiness
from business.download_friend_info import DoloadFriendInfo
from business.login_business import LoginBusiness
from business.login_business_second import LoginBusinessSecond
from util.server import Server
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(ParameTestCase):
    # 所有case共用只执行一次
    @classmethod
    def setUpClass(cls):
        '''
        cls.login_business = LoginBusiness(parames)
        print(parames)
        '''
        print('this is class')

    # 一个case的开启语
    def setUp(self):
        print('测试用例开始执行+++++++++++++++++++++++++++++')

    # 一个case的结束语
    def tearDown(self):
        print('测试用例执行结束+++++++++++++++++++++++++++++')

    #下载收藏视频
    def test_00(self):
        print('this is test_00')
        print('传入的参数'+str(parames))
        appPackage = "cn.com.open.mooc"
        appActivity = "com.imooc.component.imoocmain.splash.MCSplashActivity"
        self.login_business = LoginBusiness(parames,appPackage,appActivity)
        time.sleep(5)
        self.login_business.main()

    def test_01(self):
        self.show_ui()

    #显示UI
    def show_ui(self):
        img_folder = "/Users/kang/Desktop/phone0/0.png"
        monitor_class = Monitor()
        frame = monitor_class.start_ui(img_folder)
    #显示UI
    def show_ui_1(self):
        img_folder = "/Users/kang/Desktop/phone1/1.png"
        monitor_class = Monitor()
        frame = monitor_class.start_ui(img_folder)
    #显示UI
    def show_ui_2(self):
        img_folder = "/Users/kang/Desktop/phone2/2.png"
        monitor_class = Monitor()
        frame = monitor_class.start_ui(img_folder)

    #下载朋友圈信息
    def test_02(self):
        print('this is test_00')
        print('传入的参数' + str(parames))
        appPackage = "com.tencent.mm"
        appActivity = "com.tencent.mm.ui.LauncherUI"
        self.doload_friend_info = DoloadFriendInfo(parames, appPackage, appActivity)
        time.sleep(5)
        self.doload_friend_info.main_friend()

    def test_03(self):
        self.show_ui_1()

    #优酷提交视频
    def test_04(self):
        print('传入的参数' + str(parames))
        appPackage = "com.youku.phone"
        appActivity = "com.youku.phone.ActivityWelcome"
        self.login_business_second = LoginBusinessSecond(parames, appPackage, appActivity)
        time.sleep(2)
        self.login_business_second.main()

    def test_05(self):
        self.show_ui_2()

# appium命令行客户端初始化,将deviceName 和 port写入yaml中
def appium_init():
    server = Server()
    server.main()


def get_suit(i):
    print(str(i) + 'hello')
    # 初始化一个罐子,将要跑的case实例化,然后加入罐子;跑罐子的测试用例
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_0" + str(i), i))
    unittest.TextTestRunner().run(suite)


# 获取设备个数
def get_count():
    write_user_command = WriteUserCommand()
    count = write_user_command.get_file_lines()
    return count


if __name__ == '__main__':

    # 先初始化server
    appium_init()
    time.sleep(5)

    threads = []
    for i in range(get_count()*2):
        print(str(i))
        t = multiprocessing.Process(target=get_suit, args=(i,))
        threads.append(t)

    for j in threads:
        j.start()
        time.sleep(1)
