# coding=utf-8
from public.pages.BasePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from public.Common import Doexcel
from selenium.webdriver.common.keys import Keys
from time import sleep

class Login(BasePage):
    '''登录gome门户页面'''

    #定位器

    system_loc = ("xpath","//div[@id='tab-system']")        # 系统登录元素
    user_loc = ("xpath","//input[@placeholder='用户名']")    # 用户名loc
    pwd_loc = ("xpath","//input[@placeholder='密码']")       # 密码loc
    source_loc = ("xpath","//input[@placeholder='数据源']")              # 数据源
    list_source_loc = ("xpath","//span[@class='el-input__suffix']") # 数据源下拉框
    sourceid_loc = ("xpath","//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]")    # 电器数据源元素
    login_button_loc = ("xpath","//button[@type='button']")  # 登录按钮
    logout_loc = ("xpath","//div[@class='logout']/img")      # 退出按钮
    confirm_loc = ("xpath","//span[contains(.,'确定')]")      # 退出页面的确定按钮

    def login_portal(self,username,password,sourcename=None):
        """登录模块"""
        self.find_element(*self.system_loc).click()          # 系统登录
        print("输入用户名 %s " % username)
        self.find_element(*self.user_loc).send_keys(username)# 输入用户名
        sleep(3)
        self.find_element(*self.user_loc).send_keys(Keys.TAB)
        print("输入用户名 %s " % password)
        self.find_element(*self.pwd_loc).send_keys(int(password)) # 输入密码
        # Datas = self.find_element(*self.source_loc)
        # Source = self.find_elements("//input[@placeholder='数据源']")
        # if len(Source):
        if sourcename == '电器':
            self.find_element(*self.source_loc).click()
            self.find_element(*self.sourceid_loc).click()
            self.find_element(*self.login_button_loc).click()
        else:
            print("仅支持输入电器数据源的账户")
        if sourcename is None:
            self.find_element(*self.login_button_loc).click()
        sleep(3)
        # for i in range(3):
        #     Datas.send_keys(Keys.DOWN) # 数据源选择电器
        # sleep(3)
        # Datas.send_keys(Keys.ENTER)
        # self.find_element(*self.data_loc).send_keys(Keys.ENTER)

    def login_out(self):
        '''
        封装了退出登录的方法
        :return:
        '''
        print("退出登录")
        self.find_element(*self.logout_loc).click()
        self.wait(2)
        self.find_element(*self.confirm_loc).click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    Url = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 0)
    username = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(3, 1)
    password = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(3, 2)
    login = Login(driver)
    login.open(Url)
    login.login_portal(username,password)
    login.wait(5)
    login.login_out()

