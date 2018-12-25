#conding=utf-8
from util.doc_cmd import Doscmd
import time
#获取剪切板内容
class getClipboard:

    def __init__(self):
        self.doscmd = Doscmd()
        self.doscmd.execute_cmd('/Users/kang/Library/Android/sdk/platform-tools/adb shell am startservice ca.zgrs.clipper/.ClipboardService')

    def get_cliptext(self):
        self.doscmd.execute_cmd('/Users/kang/Library/Android/sdk/platform-tools/adb shell am startservice ca.zgrs.clipper/.ClipboardService')
        time.sleep(0.5)
        return self.doscmd.execute_cmd_clipboard('/Users/kang/Library/Android/sdk/platform-tools/adb shell am broadcast -a clipper.get')


if __name__ == '__main__':
    getclipboard = getClipboard()
    print(getclipboard.get_cliptext())