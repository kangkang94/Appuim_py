#coding=utf-8
import os
import time
#print(os.system('/Users/kang/Library/Android/sdk/platform-tools/adb devices'))
#print(os.popen('/Users/kang/Library/Android/sdk/platform-tools/adb devices').readlines())

class Doscmd:
    # 读取设备信息的函数
    def execute_cmd_result(self,command):

        result_list = []
        results = os.popen(command).readlines()
        for iterm in results:
            if iterm == '\n':
                continue
            result_list.append(iterm.strip('\n'))
        return result_list
    #直接执行command 的函数
    def execute_cmd(self,command):
        os.system(command)


if __name__ == '__main__':
    doscmd = Doscmd()
    doscmd.execute_cmd('appium -p 4700 -bp 4920 -U 9205C037 --no-reset --session-override')
    time.sleep(3)
    doscmd.execute_cmd('appium -p 4701 -bp 4911 -U 95AQSCQ94JJGC --no-reset --session-override')