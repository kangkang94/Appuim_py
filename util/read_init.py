#conding=utf-8
import configparser

class ReadIni:

    #构造器
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = '/Users/kang/Documents/github/Appuim_py/config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    #通过key获取对应的value
    def get_value(self,key,section=None):
        if section == None:
            section = 'login_element'
        else:
            self.section = section
        try:
            value = self.data.get(section,key)
        except:
            value = None
        return value


if __name__ == '__main__':
        read_ini  = ReadIni()
        print(read_ini.get_value('he','login_element'))
