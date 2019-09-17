#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 15:21
# @Author  : dumingxu
# @File    : Portal_Submit_Form_elem.py
from selenium.webdriver.common.by import By

class Portal_Submit_Form_Ele:
    '''该类下存放的是GM_Portal_Submit_Form.py的元素定位方法'''

    # 定位器
    SubmitFrom_Button_loc = ("xpath","//span[contains(text(),'提交单据')]")              # 提交单据按钮
    Order_No_loc = ("xpath","//input[@name='billNo_Main']")                             # 单据编号
    submit_iframe_loc = (By.XPATH, "//iframe[@frameborder='0']")                        # 提交后弹出的审批流程页面iframe
    Send_Sign_Button_loc = (By.XPATH,"//input[@type='button' and @value='送签']")        # 送签按钮
    Add_Link_Table_loc = ("xpath", "//table[@id='processTable']")                       # 获取提交页面的表格
    Add_Link_Button_loc = ("xpath","//span[@class='l-btn-empty icon-add']")             # 添加环节按钮
    Switch_Return_page_iframe_loc = ("xpath", "//iframe[@frameborder='0']")             # 切到退回页面iframe
    Switch_turn_page_iframe_loc = ("xpath", "//iframe[contains(@src,'userBillController.do')]")  # 切换到转签二级页面选择审批人的iframe
    SM_Select_Personnel_loc2 = (By.XPATH, "//input[@id='search']")                      # 查找转签的审批人
    SM_Select_Personnel_loc3 = (By.XPATH, "//span[contains(.,'baijinxin1')]")           # 选中转签的审批人
    SM_Confirm_Button_loc = ("xpath", "//input[@value='确定']")                           # 确定按钮
    name_text_loc = ("xpath","//input[@value='白金鑫']")                                   # 断言新增环节的审批人是否是白金鑫