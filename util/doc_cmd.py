#coding=utf-8
import os
import time


# print(os.system('/Users/kang/Library/Android/sdk/platform-tools/adb devices'))
# print(os.popen('/Users/kang/Library/Android/sdk/platform-tools/adb devices').readlines())

class Doscmd:
    # 读取设备信息的函数
    def execute_cmd_result(self, command):

        result_list = []
        results = os.popen(command).readlines()
        for iterm in results:
            if iterm == '\n':
                continue
            result_list.append(iterm.strip('\n'))
        return result_list

    # 直接执行command 的函数
    def execute_cmd(self, command):
        os.system(command)

    def get_string(self, iterm):
        results_list = iterm.split('data=')
        return results_list[1]

    def execute_cmd_clipboard(self, command):
        result_list = []
        results = os.popen(command).readlines()
        for iterm in results:
            if 'Intent' in iterm:
                continue
            if 'data' in iterm:
                result_list.append(self.get_string(iterm))
                continue
            result_list.append(iterm)
        plaintext = " "
        for st in result_list:
            plaintext = plaintext + st + '  '

        return plaintext


if __name__ == '__main__':
    doscmd = Doscmd()
    doscmd.execute_cmd(
        'appium  -p 4700 -bp 4900 -U 95AQSCQ94JJGC --no-reset --session-override')
    time.sleep(3)
    doscmd.execute_cmd('/Users/kang/Library/Android/sdk/platform-tools/adb pull sdcard/tencent/micromsg/WeiXin/康康.jpg /Users/kang/Documents/github/Appuim_py/screenshots/k2.jpg')
