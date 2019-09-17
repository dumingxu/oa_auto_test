from public.pages.BasePage import *
from public.Common import Doexcel
from public.pages.GM_Portal_Login import Login
from public.pages.GM_Portal_Wait_Handle import Wait_Handle
from public.pageelement.Portal_Form_Approval_elem import Portal_Form_Approval_Elem

class Form_Approval(BasePage):
    '''
    单据审批页面封装
    加签、转签、退回按钮
    '''
    logger = Logger("单据审批", CmdLevel=logging.DEBUG, FileLevel=logging.ERROR)

    def Input_Box(self,value='自动化审批意见输入'):
        '''
        封装审批意见输入框
        :return:
        '''
        self.logger.info("输入的审批意见为: %s" % value)
        self.wait(2)
        self.find_element(*Portal_Form_Approval_Elem.Approval_Input_loc).send_keys(value)

    def Modify_Approver_Button(self):
        '''
        封装修改审批人操作步骤
        :return:
        '''
        self.switch_to_window()
        self.logger.info("点击修改审批人按钮")
        self.find_element(*Portal_Form_Approval_Elem.Modify_Approver_loc).click()
        self.switch_to_window()
        Turn_iframe_loc = self.find_element(*Portal_Form_Approval_Elem.Switch_Return_page_iframe_loc)  # 先切进iframe
        self.switch_to_frame(Turn_iframe_loc)
        self.find_element(*Portal_Form_Approval_Elem.Select_Personnel_loc2).send_keys("baijinxin1", Keys.ENTER)
        self.double_click(*Portal_Form_Approval_Elem.Select_Personnel_loc3)
        self.switch_to_default_content()
        self.wait(2)
        self.logger.info("修改审批人页面点击确定按钮")
        self.find_element(*Portal_Form_Approval_Elem.Confirm_Button_loc1).click()                      # 确认按钮


    def Send_Button(self):
        '''
        封装了送签的逻辑
        ### 如果是退回再次提交的单据送签后再点击送签按钮提交流程
        :return:
        '''
        self.switch_to_window()
        self.Input_Box()
        self.find_element(*Portal_Form_Approval_Elem.Send_Button_loc).click()

    def Return_Start_Send(self):
        '''
        封装退回到开始环节再次送签的逻辑
        :return:
        '''
        self.Send_Button()
        self.switch_to_window()
        self.find_element(*Portal_Form_Approval_Elem.Return_Start_Send_loc).click()


    def Get_Turn_Sign_page(self):
        '''
        加签和转签查询的人员共用此方法
        封装了加签/转签二级页面选择加/转签人
        :return:
        '''
        Turn_iframe_loc = self.find_element(*Portal_Form_Approval_Elem.Switch_Return_page_iframe_loc)        # 先切进iframe
        self.switch_to_frame(Turn_iframe_loc)
        self.logger.info("点击转签人将跳转到选择转签人页面>>>>>")
        self.find_element(*Portal_Form_Approval_Elem.Select_Personnel_loc1).click()
        self.logger.info("输入转签人的用户名进行查找")
        self.switch_to_default_content()
        Turn_iframe_loc1 = self.find_element(*Portal_Form_Approval_Elem.Switch_turn_page_iframe_loc)
        self.switch_to_frame(Turn_iframe_loc1)
        self.find_element(*Portal_Form_Approval_Elem.Select_Personnel_loc2).send_keys("baijinxin1",Keys.ENTER)
        self.double_click(*Portal_Form_Approval_Elem.Select_Personnel_loc3)
        self.switch_to_default_content()                                            # 切出frame
        self.wait(2)
        self.find_element(*Portal_Form_Approval_Elem.Confirm_Button_loc1).click()                        # 确认按钮
        self.logger.info("查找完的用户进行确认操作")
        self.switch_to_default_content()  # 切出frame
        self.wait(2)
        self.find_element(*Portal_Form_Approval_Elem.Confirm_Button_loc1).click()

    def Get_Add_Sign(self):
        '''
        封装了加签逻辑
        :return:
        '''
        self.switch_to_window()
        self.logger.info("输入退回的审批意见")
        self.wait(2)
        self.find_element(*Portal_Form_Approval_Elem.Approval_Input_loc).send_keys("加签给某人一起审批一下....")
        self.find_element(*Portal_Form_Approval_Elem.Add_Sign_Button_loc).click()
        self.switch_to_window()
        self.Get_Turn_Sign_page()

    def Get_Turn_Sign(self):
        '''
        封装了转签逻辑
        :return:
        '''
        self.switch_to_window()
        self.logger.info("输入退回的审批意见")
        self.wait(2)
        self.find_element(*Portal_Form_Approval_Elem.Approval_Input_loc).send_keys("转签给一个人重新审批一下....")
        self.find_element(*Portal_Form_Approval_Elem.GoTo_Sign__Button_loc).click()
        self.Get_Turn_Sign_page()



    def Back_Designated_link(self):
        '''
        封装了退回页面>选择指定环节的二级页面
        :return:
        '''
        Back_iframe_loc = self.find_element(*Portal_Form_Approval_Elem.Switch_Return_page_iframe_loc)
        self.switch_to_frame(Back_iframe_loc)
        self.logger.info("选择退回到开始环节>>>>>")
        self.find_element(*Portal_Form_Approval_Elem.Select_Back_Designated_loc).click()
        # self.switch_to_window()
        self.switch_to_default_content()                                    # 切出frame
        Return_page_iframe1 = self.find_element(*Portal_Form_Approval_Elem.Switch_Return_page_iframe1_loc)
        self.switch_to_frame(Return_page_iframe1)                               # 重新切入frame
        self.find_element(*Portal_Form_Approval_Elem.Back_Designated_checkbox_loc).click()
        self.switch_to_default_content()
        self.logger.info("选择退回到开始环节后点击确定按钮")
        self.find_element(*Portal_Form_Approval_Elem.Confirm_Button_loc).click()
        self.switch_to_default_content()

    def assert_Back(self):
        '''
        退回类型的断言验证
        :return:
        '''
        self.find_element(*Portal_Form_Approval_Elem.Back_Button_loc).click()
        Back_iframe_loc = self.find_element(*Portal_Form_Approval_Elem.Switch_Return_page_iframe_loc)
        self.switch_to_frame(Back_iframe_loc)
        self.find_element(*Portal_Form_Approval_Elem.assert_Back_loc).click()
        types = self.find_element(*Portal_Form_Approval_Elem.assert_Backtype_loc).text
        return types

    def Back_Button(self,value='value',val='1'):
        '''
        封装了退回页面的逻辑
        入参
        value：为下拉框用value取值
        val：为1表示退回类型是"逐级审批"，为0是"直退"
        :return:
        '''
        self.logger.info("输入退回的审批意见")
        self.find_element(*Portal_Form_Approval_Elem.Approval_Input_loc).send_keys("退回到开始环节重新审批一下....")
        self.logger.info("点击退回按钮")
        self.find_element(*Portal_Form_Approval_Elem.Back_Button_loc).click()
        self.Back_Designated_link()
        Back_iframe_loc = self.find_element(*Portal_Form_Approval_Elem.Switch_Return_page_iframe_loc)
        self.switch_to_frame(Back_iframe_loc)
        if value == 'value':
            self.Select(value,val,*Portal_Form_Approval_Elem.Back_Submit_type_loc)
        else:
            self.logger.error("传入的值不是value！")
        self.switch_to_default_content()
        self.logger.info("退回页面点击确认按钮>>>>>")
        self.find_element(*Portal_Form_Approval_Elem.Confirm_Button_loc).click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    Url = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 0)
    username = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 1)
    password = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 2)
    login = Login(driver)
    login.open(Url)
    login.login_portal(username,password,'电器')
    # print(login.current_window())
    wt = Wait_Handle(driver)
    wt.Get_OrderNo("20190801FZDY00078")
    F = Form_Approval(driver)
    F.switch_to_window()
    F.Get_Add_Sign()
    # F.Get_Turn_Sign()
    # F.Back_Button()
    # F.Back_Designated_link()
    # F.assert_Back()