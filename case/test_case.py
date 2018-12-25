#coding=utf-8
import unittest
import threading
import multiprocessing
from appium import webdriver
import time

from business.download_business import DownloadBusiness
from business.download_friend_info import DoloadFriendInfo
from business.login_business import LoginBusiness
from business.login_business_second import LoginBusinessSecond
from util.server import Server
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParameTestCase,self).__init__(methodName)
        global parames
        parames = parame

class CaseTest(ParameTestCase):

    #所有case共用只执行一次
    @classmethod
    def setUpClass(cls):
        '''
        cls.login_business = LoginBusiness(parames)
        print(parames)
        '''
        print('this is class')


    #一个case的开启语
    def setUp(self):
        print('测试用例开始执行+++++++++++++++++++++++++++++')
    #一个case的结束语
    def tearDown(self):
        print('测试用例执行结束+++++++++++++++++++++++++++++')
    '''
    def test_00(self):
        print('this is test_00')
        print('传入的参数'+str(parames))
        appPackage = "cn.com.open.mooc"
        appActivity = "com.imooc.component.imoocmain.splash.MCSplashActivity"
        self.login_business = LoginBusiness(parames,appPackage,appActivity)
        time.sleep(5)
        self.login_business.login_pass()
    '''
    def test_00(self):
        print('this is test_00')
        print('传入的参数'+str(parames))
        appPackage = "com.tencent.mm"
        appActivity = "com.tencent.mm.ui.LauncherUI"
        self.doload_friend_info = DoloadFriendInfo(parames,appPackage,appActivity)
        time.sleep(5)
        self.doload_friend_info.do_business_download()


    def test_01(self):
        print('this is test_01')
        print('传入的参数'+str(parames))
        appPackage = "com.youku.phone"
        appActivity = "com.youku.phone.ActivityWelcome"
        self.login_business_second = LoginBusinessSecond(parames,appPackage,appActivity)
        time.sleep(5)
        self.login_business_second.login_pass()

#appium命令行客户端初始化,将deviceName 和 port写入yaml中
def appium_init():
    server = Server()
    server.main()

def get_suit(i):
    print(str(i)+'hello')
    # 初始化一个罐子,将要跑的case实例化,然后加入罐子;跑罐子的测试用例
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_0"+str(i),i))
    unittest.TextTestRunner().run(suite)

#获取设备个数
def get_count():
    write_user_command = WriteUserCommand()
    count = write_user_command.get_file_lines()
    return count

if __name__ == '__main__':

    #先初始化server
    appium_init()
    time.sleep(5)

    threads = []
    for i in range(get_count()):
        print(str(i))
        t = multiprocessing.Process(target=get_suit,args=(i,))
        threads.append(t)

    for j in threads:
        j.start()
        time.sleep(1)
