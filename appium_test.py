#coding=utf-8
from appium import webdriver

capabilities = {
  "platformName": "Android",
  "deviceName": "9205C037",
  "appPackage": "cn.com.open.mooc",
  "appActivity": "com.imooc.component.imoocmain.splash.MCSplashActivity"
}
webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)