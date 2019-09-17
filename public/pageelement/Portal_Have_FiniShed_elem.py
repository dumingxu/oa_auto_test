#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 15:10
# @Author  : dumingxu
# @File    : Portal_Have_FiniShed_elem.py

from selenium.webdriver.common.by import By

class GM_Portal_Have_FiniShed_Ele:
    '''GM_Portal_Have_FiniShed.py的元素定位方法'''

    # 定位器
    Have_More_loc = ("xpath", "//div[contains(.,'更多')and @class='header-menu-more-btn']")  # 先找到更多按钮
    # Have_My_Task_loc = ("xpath", "//ul[@class='more-ul']/li[5]")                           # 我的任务
    Have_My_Task_loc = ("xpath", "//li[contains(text(),'我的任务')]")  # 我的任务
    Have_handle_loc = ("xpath", "//span[contains(text(),'新已办')]")  # 新已办页面
    Have_select_oderno1_loc = ("xpath", "//input[@aria-label='单据编号']")  # 查询单据编号的input
    Have_select_results1_loc = ("xpath", "//div[@class='el-tabs__content']/div[1]//div/div/div")  # 查询的结果列表
    Have_select_state_loc = ("xpath", "//a[contains(.,'审批完成')]")  # 单据状态元素
    Have_select_results_loc = ("xpath", "//div[@class='el-tabs__content']/div[1]//div/div/div")  # 查询的结果列表
    Have_To_Withdraw_Button_loc = (By.LINK_TEXT, "撤回")  # 撤回按钮
    Hava_Confirm_Button_loc = ("xpath", "//input[@value='确定']")  # 确定按钮
