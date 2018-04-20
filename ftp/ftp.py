#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

# FTP操作
import ftplib

class FTPManager(object):
    def __init__(self, host, port, username, password, file):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.file = file
        self.file_local = '/Users/renshangui/{}'.format(self.file)
        self.ftp = ftplib.FTP()

    def connect(self, host, port):
        self.ftp.connect(host, port)

    def login(self):
        self.connect(self.host, self.port)
        self.ftp.login(self.username, self.password)
        # 获取当前路径
        pwd_path = self.ftp.pwd()
        print("FTP当前路径:", pwd_path)

    def ftp_download(self):
        '''以二进制形式下载文件'''

        bufsize = 1024  # 设置缓冲器大小
        fp = open(self.file_local, 'wb')
        self.ftp.retrbinary('RETR %s' % self.file, fp.write, bufsize)
        fp.close()

    def ftp_upload(self):
        '''以二进制形式上传文件'''
        bufsize = 1024  # 设置缓冲器大小
        fp = open(self.file_local, 'rb')
        self.ftp.storbinary('STOR ' + self.file, fp, bufsize)
        fp.close()

    def quit(self):
        self.ftp.quit()

host = 'yg45.dydytt.net'
port = 8150
username = 'ygdy8'
password = 'ygdy8'
file = '阳光电影www.ygdy8.com.湮灭.BD.720p.中英双字幕.mkv'


# 逐行读取ftp文本文件
# f.retrlines('RETR %s' % file)

if __name__ == '__main__':
    ftp_manager = FTPManager(host, port, username, password, file)
    ftp_manager.login()
    ftp_manager.ftp_download()
    ftp_manager.quit()