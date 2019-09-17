#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 14:51
# @Author  : dumingxu
# @File    : Portal_Create_Form_elem.py

from selenium.webdriver.common.by import By

class Porttal_Create_Form_Elem:
    '''
    该类下存放的是GM_Portal_Create_Form.py的元素定位方法
    '''
    # 定位器
    More_loc = ("xpath","//div[contains(text(),'更多')]")       # 先找到更多按钮
    My_Task_loc = ("xpath","//ul[@class='more-ul']/li[5]")                      # 我的任务
    New_create_from_loc = ("xpath","//ul[@class='el-menu']/div/div[9]/li/div")  # 新单据申请
    create_Wisdom_office_loc = ("xpath","//span[contains(text(),'智慧办公')]")   # 智慧办公
    get_from_loc = ("xpath","//em[contains(text(),'自动化非自定义单据')]")        # 打开单据
    get_from1_loc = ("xpath","//em[contains(text(),'自动化会签模式多人审批流程')]")# 打开单据