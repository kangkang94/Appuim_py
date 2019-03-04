#coding=utf-8
import wx
from apscheduler.schedulers.background import BackgroundScheduler
class MonitorUi(wx.Frame):
    #初始化
    def __init__(self):
        #继承父类的__init__()函数
        wx.Frame.__init__(self,None,-1,"手机运行监控器",size=(290,520))

        self.Center()
        self.Show()


    def InitUi(self,filePath):
        self.filePath_1 = filePath
        #创建面板
        panel = wx.Panel(self,-1)
        sizer = wx.GridBagSizer(10,20)
        #获取shanghai.png图片，转化为Bitmap形式，添加到第一行，第二列
        image1 = wx.Image(filePath, wx.BITMAP_TYPE_PNG).Rescale(280, 500).ConvertToBitmap()
        self.bmp1 = wx.StaticBitmap(panel, -1, image1) #转化为wx.StaticBitmap()形式
        sizer.Add(self.bmp1, pos=(0,0), flag=wx.ALL, border=5)
        #为button绑定事件
        #self.Bind(wx.EVT_BUTTON,self.change_picture,button)
        panel.SetSizerAndFit(sizer)


    def change_picture(self):
        image = wx.Image(self.filePath_1,wx.BITMAP_TYPE_PNG).Rescale(280,500).ConvertToBitmap()
        self.bmp1.SetBitmap(wx.BitmapFromImage(image))

if __name__ == '__main__':
    app = wx.App()
    frame = MonitorUi()
    frame.InitUi('/Users/kang/Desktop/phone0/0.png')

    scheduler = BackgroundScheduler()
    scheduler.add_job(frame.change_picture,'interval',seconds=1)
    scheduler.start()

    app.MainLoop()