from public.pages.BasePage import *
from public.Common import Doexcel
from public.pages.GM_Portal_Login import Login
from public.pages.GM_Portal_Submit_Form import *
class Create_Form(BasePage):
    """
    创建单据页面的模板
    继承该类后既拥有创建单据的方法
    create_from()方法是创建单据
    """
    logger = Logger("打开单据", CmdLevel=logging.DEBUG, FileLevel=logging.ERROR)

    # 定位器
    More_loc = ("xpath","//div[contains(text(),'更多')]")       # 先找到更多按钮
    My_Task_loc = ("xpath","//ul[@class='more-ul']/li[5]")                      # 我的任务
    New_create_from_loc = ("xpath","//ul[@class='el-menu']/div/div[9]/li/div")  # 新单据申请
    create_Wisdom_office_loc = ("xpath","//span[contains(text(),'智慧办公')]")   # 智慧办公
    get_from_loc = ("xpath","//em[contains(text(),'自动化非自定义单据')]")        # 打开单据
    get_from1_loc = ("xpath","//em[contains(text(),'自动化会签模式多人审批流程')]")# 打开单据
    def create_from(self,formname):
        '''
        封装了从智慧办公页面的创建单据的业务逻辑
        :return:
        '''
        self.logger.info("点击更多按钮")
        self.move_to(self.find_element(*self.More_loc))  # 点击更多按钮
        self.logger.info("点击我的任务")
        self.find_element(*self.My_Task_loc).click()  # 点击我的任务
        self.logger.info("点击新单据申请")
        self.find_element(*self.New_create_from_loc).click() # 点击新单据申请
        self.logger.info("点击智慧办公")
        self.find_element(*self.create_Wisdom_office_loc).click() # 点击新智慧办公
        self.wait(2)
        # C = self.current_window()
        # print(C)
        if formname == '自动化非自定义单据':
            self.find_element(*self.get_from_loc).click() # 打开自动化测试单据
        elif formname == '自动化会签模式多人审批流程':
            self.find_element(*self.get_from1_loc).click()  # 打开自动化测试单据
        else:
            self.logger.error("输入的单据名称为：%s ,没有在页面中找到" % formname)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    Url = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 0)
    username = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 1)
    password = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 2)
    login = Login(driver)
    login.open(Url)
    login.login_portal(username, password)

    # C = Create_Form(driver)
    # C.create_from()
    # Submit = Submit_from(driver)
    # Order = Submit.submit_from()
