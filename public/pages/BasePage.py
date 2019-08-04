#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import logging
import time
from log.log import *

class BasePage():
    '''
    封装所有页面的公共方法
    '''
    def __init__(self,selenium_driver):
        try:
            self.driver = selenium_driver
            self.driver.maximize_window()
            self.wait(3)
        except Exception:
            raise NameError("Not Chrome")
    def open(self,url):
        if url != '':
            self.driver.get(url)
        else:
            raise ValueError("Please input a url!")

    # 寻找指定元素
    def find_element(self,*loc):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self,loc))
        # return self.driver.find_element(*loc)

    #寻找指定的一批元素
    def find_elements(self,loc):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            # elements = self.driver.find_elements_by_xpath(loc)
            # return elements
            elements = self.driver.find_elements_by_xpath(loc)
            return elements
        except Exception as e:
            print(u"%s 页面中未能找到 %s 元素:%s" % (self, loc,e))

        # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 判断复选框能否被选中
    def check_box(self,*loc):

        return self.find_element(*loc).is_selected()

    def checks_boxs(self,loc):

        return self.find_elements(*loc).is_selected()

    # def click(self):
    #     self.click()


    # def enter(self,loc):
    #     loc.send_keys(Keys.ENTER)

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    #元素不可见时用此方法改为可见
    def display(self,id):
        self.driver = webdriver.Chrome()
        js = "document.getElementById(list[id]).style.display='block'"
        self.driver.execute_script(js)

    def addAttribute(self,driver, elementObj, attributeName, value):
        # 封装向页面添加标签中添加新属性的方法
        # 调用JavaScript代码给页面标签添新属性，arguments[0]-arguments[2]分别会用
        # 后面的element、attributeName和value参数值进行替换，并执行该JavaScript代码
        # 添加新属性的JavaScript代码语法为：element.attributeName = value
        # 比如input.name = "test"
        driver.execute_script("arguments[0]. %s =arguments[1]" % attributeName,
                              elementObj, value)

    def getAttribute(self,elementObj, attributeName):
        '''查看定位到的元素属性名称的value值：'''
        return elementObj.get_attribute(attributeName)
    # 获取当前窗口句柄
    def current_window(self):
        return self.driver.current_window_handle

    # 获取所有窗口句柄
    def handles(self):
        return self.driver.window_handles

    # 睡眠一段时间
    def wait(self, seconds=3):
        time.sleep(seconds)

    # 鼠标双击操作
    def double_click(self,*loc):
        element = self.find_element(*loc)
        ActionChains(self.driver).double_click(element).perform()

    # 移动到指定元素
    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def switch_towindow(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    # 切换窗口
    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        # logger = Logger("Box", CmdLevel=logging.INFO, FileLevel=logging.ERROR)
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:

            print('只有1个window!')
        elif len(all_windows) == 2:
            # other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(all_windows[-1])
            # self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        print(self.driver.current_url)
    # 下拉框Select选项
    def Select(self,val,value,*loc):
        select = Select(self.driver.find_element(*loc))
        if val == 'text':
            select.select_by_visible_text(value)
        if val == 'value':
            select.select_by_value(value)

    # 切换frame页面
    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    # 根据table获取所有的tb
    def Table_element(self,*loc):
        '''
        获取所有tb的text文本
        :param loc:
        :return:
        '''
        table = self.find_element(*loc)
        row = table.find_elements_by_tag_name('tr')
        list = []
        for i in row:
            j = i.find_elements_by_tag_name('td')
            for item in j:
                text = item.text
                list.append(text)
        return list

    # 切出frame页面
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # 切换alter
    def switch_to_alert(self):
        return self.driver.switch_to.alert

if __name__ == '__main__':
    # shuru = ("id","kw")
    # button = ("id","su")
    driver = webdriver.Chrome()
    B = BasePage(driver)
    A = B.addAttribute(driver,'input','name','con')
    print(A)
    # driver = webdriver.Chrome()
    # BP = BasePage(driver)
    # B.open("https://www.baidu.com")
    # ele = B.find_element(By.LINK_TEXT,"设置")
    # B.move_to(ele)
    # BP.logger.info("打开百度网址")
    # BP.wait(3)
    # BP.find_element(shuru).send_keys("selenium")
    # BP.logger.info("定位输入框元素")
    # BP.logger.info("输入selenium字符串")
    # BP.find_element(button).click()
    # BP.logger.info("点击搜索按钮")
    # BP.wait(3)
    # BP.logger.info("等待3秒后退出")
    # BP.quit()
