from public.pages.BasePage import *
from selenium.webdriver.common.keys import Keys
from public.Common import Doexcel
from public.pages.GM_Portal_Login import Login

class My_From(BasePage):
    """
    我的单据继承自BasePage基类
    """

    logger = Logger("我的单据", CmdLevel=logging.DEBUG, FileLevel=logging.ERROR)

    # 定位器
    My_From_Button_loc = ("xpath","//span[contains(text(),'新我的单据')]")           # 我的单据


    def To_Withdraw(self):
        '''
        封装在我的单据里撤回的操作
        :return:
        '''
        pass