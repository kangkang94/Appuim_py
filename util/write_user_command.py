#coding=utf-8
import yaml

class WriteUserCommand:

    #加载yaml数据
    def read_data(self):
        with open('../config/userconfig.yaml') as fr:
            data = yaml.load(fr)
            return data

    #获取value
    def get_value(self,key,port):
        data = self.read_data()
        return data[key][port]

    #往yaml中写入数据
    def write_data(self,i,bp,deviceName,port):

        data = self.join_data(i,bp,deviceName,port)
        with open('../config/userconfig.yaml','a') as fr:
            yaml.dump(data,fr)

    #改变 data数据格式为yaml识别的格式
    def join_data(self,i,bp,deviceName,port):
        data = {
            'user_info_'+str(i):{
                'deviceName': str(deviceName),
                'bp': bp,
                'port': port
            }
        }
        return data
    #在start server之前把yaml里的信息均删除
    def clear_data(self):
        with open('../config/userconfig.yaml','w') as fr:
            fr.truncate()
        fr.close()
    #yaml是字典,data[key][port],所以直接获取数据的行数
    def get_file_lines(self):
        data = self.read_data()
        return len(data)


if __name__ == '__main__':
    writeUserCommand = WriteUserCommand()
    writeUserCommand.write_data('4','4720','111','4721')
