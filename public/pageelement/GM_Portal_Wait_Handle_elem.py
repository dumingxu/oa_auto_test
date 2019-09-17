#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 15:24
# @Author  : dumingxu
# @File    : GM_Portal_Wait_Handle_elem.py

from selenium.webdriver.common.by import By

class Portal_Wait_Handle_Ele:
    '''该类下存放的是GM_Portal_Wait_Handle.py的元素定位方法'''

    # 定位器
    wait_More_loc = ("xpath", "//div[contains(text(),'更多')]")                   # 先找到更多按钮
    wait_My_Task_loc = ("xpath", "//li[contains(.,'我的任务')]")                 # 我的任务
    wait_handle_loc = ("xpath","//span[contains(text(),'新待办')]")               # 新待办页面
    select_oderno_loc = ("xpath","//input[@aria-label='单据编号']")               # 查询单据编号的input
    select_results_loc = ("xpath","//div[@class='el-tabs__content']/div[1]//div/div/div")  # 查询的结果列表
    select_state_loc = ("xpath","//a[contains(.,'审批完成')]")                          # 单据状态元素
    select_state1_loc = ("xpath", "//a[contains(.,'审批中')]")                     # 单据状态元素
    select_state2_loc = ("xpath", "//a[contains(.,'退回')]")                     # 单据状态元素
