#encoding=utf-8
#将秒级别转换为毫秒级别
from util.get_from_phone import getFromPhone
import time

def change_haomiao(time_now):

    return int(round(time_now * 1000))

#从手机中拉取当前下载的图片并重命名
def pull_picture():
    get_from_phone = getFromPhone()

    nowtime = change_haomiao(time.time())
    #注意 电脑的unix时间戳一定要和手机的unix时间戳一致
    for i in range(nowtime-33600,nowtime-33500,1):
        get_from_phone.get_from_phone(0,i,"测试照片")

if __name__ == '__main__':
    pull_picture()