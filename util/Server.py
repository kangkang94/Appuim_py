#coding=utf-8
from util.doc_cmd  import Doscmd
from util.port import Port
import threading
import multiprocessing
from util.write_user_command import WriteUserCommand
import time
class Server:
    def __init__(self):

        #获取设备信息
        self.dos = Doscmd()
        self.device_list = self.get_device()
        self.write_file = WriteUserCommand()

    def get_device(self):

        #存储设备信息
        device_list = []

        result_list = self.dos.execute_cmd_result('/Users/kang/Library/Android/sdk/platform-tools/adb devices')

        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                device_info = i.split('\t')
                if device_info[1] == 'device':
                    device_list.append(device_info[0])
            return device_list
        else:
            return None

    def create_port_list(self,startPort):
        port_list = []
        port = Port()
        port_list = port.create_port_list(startPort,self.device_list)
        return port_list

    #封装生成启动命令行函数
    def create_command_list(self,i):

        #appium -p 4700 -bp 4701 -U 127.0.0.1:21503
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        command = 'appium -p '+str(appium_port_list[i])+' -bp '+str(bootstrap_port_list[i])+' -U '+device_list[i]+' --no-reset --session-override'
        command_list.append(command)
        self.write_file.write_data(i,str(bootstrap_port_list[i]),str(device_list[i]),str(appium_port_list[i]))
        return command_list

    #启动命令行
    def start_server(self,i):
        #启动服务
       self.start_list = self.create_command_list(i)
       print(self.start_list)
       self.dos.execute_cmd(self.start_list[0])

    #杀死appium服务
    def kill_server(self):

        server_list = self.dos.execute_cmd_result('ps -ef | grep node | grep -v grep')
        if len(server_list)>0:
            self.dos.execute_cmd('killall -9 node')

    #启动
    def main(self):
        # 一进来先杀进程再清楚yaml文件
        self.kill_server()
        thread_list = []
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = multiprocessing.Process(target=self.start_server,args=(i,))
            thread_list.append(appium_start)

        for j in thread_list:
            j.start()
        time.sleep(25)



if __name__ == '__main__':
    server = Server()
    print(server.main())

