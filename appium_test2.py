#coding=utf-8
from appium import webdriver
#获取工程路径
import sys
sys.path.append('/Users/kang/Documents/github/Appuim_py')
from util.read_init import ReadIni
import time
from util.get_by_local import GetByLocal
def get_driver():
    capabilities = {
      "platformName": "Android",
      "deviceName": "95AQSCQ94JJGC",
      "appPackage": "com.youku.phone",
        #activity 选哪一个 要研究透彻 appAwaitActivity
      "appActivity": "com.youku.phone.ActivityWelcome",
      "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
    return driver

driver = get_driver()

#页面滑动函数封装
#获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height

#向左滑
def swipe_left():
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1,y1,x,y1)
#向右滑
def swipe_right():
    x1 = get_size()[0]/10
    y1 = get_size()[1]/2
    x = get_size()[0]/10*9
    driver.swipe(x1,y1,x,y1)
#向上滑
def swipe_up():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10*5
    y = get_size()[1]/10*3
    driver.swipe(x1,y1,x1,y)
#向下滑
def swipe_down():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10
    y = get_size()[1]/10*9
    driver.swipe(x1,y1,x1,y)

def swipe_on(direnction):
    if direnction == 'up':
        swipe_up()
    elif direnction == 'down':
        swipe_down()
    elif direnction == 'left':
        swipe_left()
    else :
        swipe_right()

#原生app转换为H5页面
def get_web_view():
    webview = driver.contexts
    for viw in webview:
        if 'WEBVIEW_com.android.quicksearchbox' in viw:
            driver._switch_to.context(viw)


#id定位进行登录操作
def download_video():

    '''
    #点击登录
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/bgs').click()
    time.sleep(1)


    driver.find_element_by_id('com.ss.android.ugc.aweme:id/age').click()

    driver.find_element_by_id('com.ss.android.ugc.aweme:id/ac7').send_keys('18525461587')
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/afq').send_keys('92n38k817625')
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/ac9').click()
    '''

    driver.find_element_by_id('com.youku.phone:id/layout_user').click()


    driver.find_element_by_id('com.youku.phone:id/ucenter_user_pic').click()
    driver.find_element_by_id('com.youku.phone:id/passport_login_type').click()

    driver.find_element_by_id('com.youku.phone:id/passport_username').send_keys('18525461587')
    driver.find_element_by_id('com.youku.phone:id/passport_password').send_keys('92n38k817625')
    driver.find_element_by_id('com.youku.phone:id/passport_login').click()

    driver.find_element_by_id('com.youku.phone:id/home_tool_bar_search_frame').send_keys('火影忍者')
    driver.find_element_by_id('com.youku.phone:id/suggestion_item_img').click()

    '''
    element_1 = driver.find_element_by_id('com.ss.android.ugc.aweme:id/im')
    elements_1 = element_1.find_elements_by_class_name('android.widget.ImageView')
    elements_1[0].click()
    time.sleep(4)

    webview = driver.contexts
    print(webview)
    for viw in webview:
        if 'WEBVIEW_com.android.quicksearchbox' in viw:
            driver.switch_to.context(viw)
            break
    print(driver.current_context)


    print('++++++++++++++++++++++++++++')
    '''

download_video()



