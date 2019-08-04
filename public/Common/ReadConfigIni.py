#!/usr/bin/env python
import configparser
import codecs
import os

class ReadConfigIni():
    '''
    实例化configparser
    '''

    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    #读操作
    def getConfigValue(self,config,name):
        value = self.cf.get(config,name)
        return value

# *************
# 验证ReadConfigIni是否可以读取ini文件，该部分为测试代码，实际框架中可以删除
# *************
# file_path = os.path.dirname(__file__)
# file_path = os.path.split(os.path.realpath(__file__))[0]

# file_path = os.path.abspath("./")

# print(file_path)
# read_config = ReadConfigIni(os.path.join(file_path,'config.ini'))
# print(read_config)
# value = read_config.getConfigValue("Url","baidu_url")
# print(value)
