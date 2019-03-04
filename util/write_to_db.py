# coding=utf-8

import pymysql

class WriteToDb:
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="kangkang94",
            database="test",
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)


    def writeData(self,nickname,plain_text,link,linkText,picturePath,version):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute("INSERT INTO friendinfo(nickname,content,linkText,link,picturePath,version) VALUES(%s,%s,%s,%s,%s,%s);",
                   (nickname,plain_text,link,linkText,picturePath,version))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

        finally:
            self.cursor.close()


if __name__ == '__main__':
    writeToDb = WriteToDb()
    writeToDb.writeData("hello","","","https://mp.weixin.qq.com/s?__biz=MjM5ODYxMDA5OQ==&mid=2651961910&idx=1&sn=4eda5b5c327bbaaf5ff1ac344ca9a499&chksm=bd2d0fea8a5a86fc56b80d197876a17bd24c989c15d89abf8d2b356a1f6dc3756cc5b78c9f58&mpshare=1&scene=2&srcid=&from=timeline&ascene=2&devicetype=android-25&version=2607033d&nettype=WIFI&abtest_cookie=BQABAAgACgALABMAFAAFAJ2GHgAmlx4AV5keAJuZHgCcmR4AAAA%3D&lang=zh_CN&pass_ticket=wei7UZFWhHMViyuDRt6ELSIvsw7ZMY7o7WMVXfH9jFAYIvZY6A%2FxeJ%2FcACjbmF1O&wx_header=1\"\
    \n ","")