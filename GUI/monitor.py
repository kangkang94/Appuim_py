#coding=utf-8
import time
import wx
from apscheduler.schedulers.background import BackgroundScheduler

from GUI.monitor_ui import MonitorUi


class Monitor:

    def start_ui(self,filePath):
        app = wx.App()
        frame = MonitorUi()
        frame.InitUi(filePath)
        scheduler = BackgroundScheduler()
        scheduler.add_job(frame.change_picture,'interval',seconds=2)
        scheduler.start()

        app.MainLoop()

        return frame

