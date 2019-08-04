#!/usr/bin/env python

import xlrd
import os
from config import globalconfig
data_path = globalconfig.data_path
# print(data_path)

# ************
# 读取excel封装到一个类中
# 实现数据驱动测试
# ************
class ReadExcel():
    '''
    打开Excel，读取测试数据
    '''

    # 打开Excel
    # 如下是读取当前目录下的Excel文件
    # def __init__(self,filename,sheetname):
    #     self.workbook = xlrd.open_workbook(filename)
    #     self.sheetname = self.workbook.sheet_by_name(sheetname)
    # 读取其他目录下的Excel
    def __init__(self,filename,sheetname):

        datapath = os.path.join(data_path,filename)
        self.workbook = xlrd.open_workbook(datapath)
        self.sheetname = self.workbook.sheet_by_name(sheetname)

    #获取某个单元格的数据
    def read_excel(self,rownum,colum):
        value = self.sheetname.cell(rownum,colum).value
        return value

# *****************
# 验证ReadExcel类的正确性
# *****************
# cellvalue = ReadExcel("data.xlsx","Sheet1").read_excel(1,0)
# print(cellvalue)
