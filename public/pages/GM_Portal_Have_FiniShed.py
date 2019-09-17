from public.pages.BasePage import *
from selenium.webdriver.common.keys import Keys
from public.Common import Doexcel
from public.pages.GM_Portal_Login import Login
from public.pages.GM_Portal_Wait_Handle import Wait_Handle
from public.pageelement.Portal_Have_FiniShed_elem import GM_Portal_Have_FiniShed_Ele  # 存放页面元素的类

class Have_FiniShed(BasePage):
    '''
    已办页面
    封装了查询单号及单据状态
    撤回功能
    '''

    logger = Logger("已办页面", CmdLevel=logging.DEBUG, FileLevel=logging.ERROR)

    def Hava_Page(self):
        '''
        打开已办页面
        :return:
        '''
        self.logger.info("点击更多按钮")
        self.move_to(self.find_element(*GM_Portal_Have_FiniShed_Ele.Have_More_loc))  # 点击更多按钮
        self.logger.info("点击我的任务")
        self.find_element(*GM_Portal_Have_FiniShed_Ele.Have_My_Task_loc).click()     # 点击我的任务
        self.logger.info("点击新已办")
        self.find_element(*GM_Portal_Have_FiniShed_Ele.Have_handle_loc).click()      # 点击新已办

    def To_Withdraw(self):
        '''
        封装在已办页面里撤回的操作
        :return:
        '''
        self.switch_to_window()
        self.logger.info("点击撤回按钮")
        self.wait(2)
        self.find_element(*GM_Portal_Have_FiniShed_Ele.Have_To_Withdraw_Button_loc).click()  # 撤回操作
        self.wait(2)
        self.switch_to_window()
        self.find_element(*GM_Portal_Have_FiniShed_Ele.Hava_Confirm_Button_loc).click()


    def Select_OrderNo(self,oderno=None,state='审批完成'):
        '''

        :param oderno:需要传入单据编号  单据编号由 submit_from 方法获取
        :return:返回查询结果中的单据状态用于验证单据是否审批完成
        '''
        self.logger.info("输入单据编号：%s" % oderno)
        K = self.find_element(*GM_Portal_Have_FiniShed_Ele.Have_select_oderno1_loc)
        K.send_keys(oderno)
        K.send_keys(Keys.ENTER)                                                          # 模拟回车键查询
        # re = self.find_element(*self.Have_select_results1_loc)
        # print(re)
        # table_rows = re.find_elements_by_tag_name('tr')                                 # 获取查询结果的行数
        # state = re.find_elements_by_tag_name('td')[9].text
        if state == '审批中':
            self.wait(2)
            re = self.find_element(*GM_Portal_Have_FiniShed_Ele.Have_select_results_loc)
            re.find_elements_by_tag_name('td')[4].click()                     # 打开列表中第一行的单据
        if state == '审批完成':
            state = self.find_element(*GM_Portal_Have_FiniShed_Ele.Have_select_state_loc).text
        return state

if __name__ == '__main__':

    # 调试时启用
    driver = webdriver.Chrome()
    Url = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 0)
    username = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 1)
    password = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 2)
    login = Login(driver)
    login.open(Url)
    login.login_portal(username, password, '电器')
    Have = Have_FiniShed(driver)
    Have.Hava_Page()
    Have.Select_OrderNo('20190801FZDY00063',state='审批中')
    Have.To_Withdraw()

    # Wa = Wait_Handle(driver)
    # state = Wa.Select_OrderNo("20190731FZDY00029")
    # print(state)