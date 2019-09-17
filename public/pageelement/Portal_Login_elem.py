#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 15:15
# @Author  : dumingxu
# @File    : Portal_Login_elem.py

class Login_Ele:
    '''该类下存放的是GM_Portal_Login.py的元素定位方法'''

    # 定位器
    system_loc = ("xpath", "//div[@id='tab-system']")  # 系统登录元素
    user_loc = ("xpath", "//input[@placeholder='用户名']")  # 用户名loc
    pwd_loc = ("xpath", "//input[@placeholder='密码']")  # 密码loc
    source_loc = ("xpath", "//input[@placeholder='数据源']")  # 数据源
    list_source_loc = ("xpath", "//span[@class='el-input__suffix']")  # 数据源下拉框
    sourceid_loc = ("xpath", "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]")  # 电器数据源元素
    login_button_loc = ("xpath", "//button[@type='button']")  # 登录按钮
    logout_loc = ("xpath", "//div[@class='logout']/img")  # 退出按钮
    confirm_loc = ("xpath", "//span[contains(.,'确定')]")  # 退出页面的确定按钮
