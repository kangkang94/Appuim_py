# conding=utf-8
from util.doc_cmd import Doscmd
import time
from util.write_user_command import WriteUserCommand

#
class getFromPhone:
    def __init__(self):
        self.doscmd = Doscmd()

    # 将图片名称命名为时间戳和人名
    def get_from_phone(self,i, time, nickname):
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_'+str(i//2),'deviceName')
        self.doscmd.execute_cmd(
                "adb -s "+ devices +" shell ls sdcard/tencent/micromsg/WeiXin/mmexport" + str(time) + "*.jpg | tr '\r' ' ' | xargs -n1 -I '{}' adb pull {} /Users/kang/Documents/github/Appuim_py/screenshots/" + str(
                    time) + str(nickname) + ".jpg")

    def text_time(self):
        return int(time.time())


if __name__ == '__main__':
    get_from_phone = getFromPhone()
    print(get_from_phone.text_time())
    get_from_phone.get_from_phone(0,1545703347,"康宇航")


