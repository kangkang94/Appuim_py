#coding=utf-8
from util.doc_cmd import Doscmd
class Port:
    def port_is_used(self,portNum):

        # 判断端口是否被占用
        flag = None
        doscmd = Doscmd()
        result = doscmd.execute_cmd_result('lsof -i:'+str(portNum))

        if len(result)> 0 :
            flag = True
        else:
            flag = False
        return flag

    #封装生成可用端口信息
    def create_port_list(self,startPort,devicelist):

        port_list = []
        if devicelist != None:
            while len(port_list)!=len(devicelist):
                if self.port_is_used(startPort) == False:
                    port_list.append(startPort)
                startPort+=1
            return port_list
        else:
            print('无可用设备')
            return None

        return port_list



if __name__ == '__main__':
    list = [1,2,3,4,5]
    port = Port()
    print(port.create_port_list(4720,list))