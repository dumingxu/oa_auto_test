#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 15:02
# @Author  : dumingxu
# @File    : Portal_Form_Approval_elem.py
from selenium.webdriver.common.by import By

class Portal_Form_Approval_Elem:
    '''
    该类下存放的是GM_Portal_Form_Approval.py的元素定位方法
    '''

    # 定位器
    Send_Button_loc = (By.LINK_TEXT,"送签")                                                   # 送签按钮
    Return_Start_Send_loc = ("xpath","//input[@value='送签']")                                # 退回到开始环节再次送签
    GoTo_Sign__Button_loc = (By.LINK_TEXT, "转签")                                            # 转签按钮
    Add_Sign_Button_loc = (By.LINK_TEXT,"加签")                                               # 加签按钮
    Back_Button_loc = (By.LINK_TEXT,"退回")                                                   # 退回按钮
    Confirm_Button_loc = ("xpath","//input[@value='确定']")                                   # 确定按钮
    Confirm_Button_loc1 = (By.XPATH,"/html/body/div[2]/table/tbody/tr[2]/td[2]\
                           /div/table/tbody/tr[3]/td/div/input[1]")                          # 转签二级页面确定按钮
    Confirm_Button_loc2 = ("xpath","confirm")
    Switch_Return_page_iframe_loc = ("xpath","//iframe[@frameborder='0']")                   # 切到退回页面iframe
    Switch_Return_page_iframe1_loc = ("xpath","//iframe[contains(@src,'approvalTaskController.do')]")# 退回页面iframe下一级选择退回环节iframe
    Switch_turn_page_iframe_loc = ("xpath","//iframe[contains(@src,'userBillController.do')]")# 切换到转签二级页面选择审批人的iframe
    Select_Back_Designated_loc = ("id","chooseTaskNode")                                     # 退回页面选择指定环节
    Back_Designated_checkbox_loc = ("xpath","//table[@class='formtable'and@id='nodeTb']/tbody/tr/td[5]/input")    # 退回指定环节复选框
    Back_Submit_type_loc = ("id","reSubmitType")                                             # 退回再次提交类型
    Approval_Input_loc = ("xpath","//textarea[@name='currentTextArea']")                     # 审批意见输入框
    Select_Personnel_loc1 = (By.ID, "approver")                                             # 点击转签人的输入框
    Select_Personnel_loc2 = (By.XPATH, "//input[@id='search']")                             # 查找转签的审批人
    Select_Personnel_loc3 = (By.XPATH,"//span[contains(.,'baijinxin1')]")                   # 选中转签的审批人
    Modify_Approver_loc = ("id","modifyButton")                                             # 修改审批人按钮
    assert_Back_loc = ("xpath","//select[@class='inputxt']")                                # 退回类型下拉框
    assert_Backtype_loc = ("xpath","//option[contains(.,'被退环节再提交时”逐级审批“')]")       # 退回类型为逐级审批