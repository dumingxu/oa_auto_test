from public.pages.BasePage import *
from selenium.webdriver.common.keys import Keys
from public.Common import Doexcel
from public.pages.GM_Portal_Login import Login
from public.pageelement.GM_Portal_Wait_Handle_elem import Portal_Wait_Handle_Ele

class Wait_Handle(BasePage):
    '''
    待办页面继承基础basepage类
    '''

    logger = Logger("待办页面", CmdLevel=logging.DEBUG, FileLevel=logging.ERROR)

    def Wait_Page(self):
        '''
        打开待办页面
        :return:
        '''
        self.logger.info("点击更多按钮")
        self.move_to(self.find_element(*Portal_Wait_Handle_Ele.wait_More_loc))  # 点击更多按钮
        self.logger.info("点击我的任务")
        self.find_element(*Portal_Wait_Handle_Ele.wait_My_Task_loc).click()  # 点击我的任务
        self.logger.info("点击新待办")
        self.find_element(*Portal_Wait_Handle_Ele.wait_handle_loc).click()  # 点击新待办

    def Select_OrderNo(self,oderno=None,state='审批中'):
        '''

        :param oderno:需要传入单据编号  单据编号由 submit_from 方法获取
        :return:返回查询结果中的单据状态用于验证单据是否审批成功
        '''
        # state_list = ['审批中','审批完成','未提交','退回']
        self.logger.info("输入单据编号：%s" % oderno)
        K = self.find_element(*Portal_Wait_Handle_Ele.select_oderno_loc)
        K.send_keys(oderno)
        K.send_keys(Keys.ENTER)                                                          # 模拟回车键查询
        # re = self.find_element(*self.select_results_loc)
        self.wait(3)
        # print(re)
        # table_rows = re.find_elements_by_tag_name('tr')                                 # 获取查询结果的行数
        if state == '审批中':
            state = self.find_element(*Portal_Wait_Handle_Ele.select_state1_loc).text
        elif state == '审批完成':
            state = self.find_element(*Portal_Wait_Handle_Ele.select_state_loc).text
        else:
            state = self.find_element(*Portal_Wait_Handle_Ele.select_state2_loc).text
        # state = re.find_elements_by_tag_name('td')[10].text
        # if state in state_list:
        #     self.logger.info('查询该单据的状态为： %s'% state)
        return state

    def Get_OrderNo(self,order,state='审批中'):
        '''
        根据查询出的单据号打开该单据
        :param results_orderno:由Select_OrderNo返回的单据号
        :return:
        '''
        self.Wait_Page()
        self.Select_OrderNo(order,state)
        self.wait(2)
        re = self.find_element(*Portal_Wait_Handle_Ele.select_results_loc)
        re.find_elements_by_tag_name('td')[4].click()                     # 打开列表中第一行的单据


if __name__ == '__main__':
    driver = webdriver.Chrome()
    Url = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 0)
    username = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 1)
    password = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 2)
    login = Login(driver)
    login.open(Url)
    login.login_portal(username, password,'电器')
    wt = Wait_Handle(driver)
    # wt.Wait_Page()
    # odder = wt.Select_OrderNo()
    wt.Get_OrderNo("RCF20190730ZT00010")
