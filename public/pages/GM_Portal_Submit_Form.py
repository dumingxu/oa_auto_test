from public.pages.BasePage import *
from public.pages.GM_Portal_Create_Form import Create_Form
from public.pageelement.Portal_Submit_Form_elem import Portal_Submit_Form_Ele

class Submit_from(BasePage):
    '''
    提交单据页面继承BasePage类
    :return:
    '''
    logger = Logger("提交单据", CmdLevel=logging.DEBUG, FileLevel=logging.ERROR)

    def Order_No(self):
        '''
        封装了单据编号方法返回单据编号文本
        用于断言验证
        :return:
        '''
        text = self.find_element(*Portal_Submit_Form_Ele.Order_No_loc)
        return text.get_attribute("value")

    def switch_submit_iframe(self):
        '''
        切换到提交单据弹出页面的iframe
        :return:
        '''
        iframe = self.find_element(*Portal_Submit_Form_Ele.submit_iframe_loc)
        self.switch_to_frame(iframe)

    def Send_Sign_Button(self):
        '''
        封装提交页面送签按钮
        :return:
        '''
        self.switch_to_default_content()
        self.find_element(*Portal_Submit_Form_Ele.Send_Sign_Button_loc).click()

    def Add_Link(self):
        '''
        封装 添加环节的操作
        :return:
        '''
        self.switch_to_window()
        Back_iframe_loc = self.find_element(*Portal_Submit_Form_Ele.Switch_Return_page_iframe_loc)
        self.switch_to_frame(Back_iframe_loc)
        self.logger.info("点击添加环节按钮")
        self.find_element(*Portal_Submit_Form_Ele.Add_Link_Button_loc).click()
        self.wait(2)
        self.switch_to_window()
        Turn_iframe_loc1 = self.find_element(*Portal_Submit_Form_Ele.Switch_turn_page_iframe_loc)
        self.switch_to_frame(Turn_iframe_loc1)
        self.logger.info("输入该环节的审批人")
        self.find_element(*Portal_Submit_Form_Ele.SM_Select_Personnel_loc2).send_keys("baijinxin1", Keys.ENTER)
        self.double_click(*Portal_Submit_Form_Ele.SM_Select_Personnel_loc3)
        self.switch_to_default_content()  # 切出frame
        self.wait(2)
        self.find_element(*Portal_Submit_Form_Ele.SM_Confirm_Button_loc).click()  # 确认按钮
        Turn_iframe_loc1 = self.find_element(*Portal_Submit_Form_Ele.Switch_turn_page_iframe_loc)
        self.switch_to_frame(Turn_iframe_loc1)
        Tab = self.Table_element(*Portal_Submit_Form_Ele.Add_Link_Table_loc)                      # 先获取table
        n = Tab.index('开始环节转签')                                             # 获取开始环节转签的text做校验
        self.logger.info("查找完的用户进行确认操作")
        self.switch_to_default_content()  # 切出frame
        self.wait(2)
        # texts = self.name_text()
        return Tab[n]
    def Submit_From_Button(self):
        '''
        提交按钮
        :return:
        '''
        self.switch_to_window()
        self.logger.info("点击提交单据按钮")
        self.find_element(*Portal_Submit_Form_Ele.SubmitFrom_Button_loc).click()

    def submit_from(self):
        '''
        提交单据后会返回单据编号用于验证单据是否提交成功
        :return: Order
        '''
        self.switch_to_window()
        Order = self.Order_No()
        self.logger.info("单据编号：%s " % Order)
        self.logger.info("点击提交单据按钮")
        self.find_element(*Portal_Submit_Form_Ele.SubmitFrom_Button_loc).click()
        self.logger.info("切换iframe")
        self.switch_submit_iframe()
        self.switch_to_default_content()
        self.logger.info("点击送签按钮")
        self.find_element(*Portal_Submit_Form_Ele.Send_Sign_Button_loc).click()

        return Order
