import unittest
from public.pages.GM_Portal_Login import *
from time import sleep
from public.Common.function import insert_img
from public.pages.GM_Portal_Submit_Form import *
from public.pages.GM_Portal_Wait_Handle import Wait_Handle
from public.pages.GM_Portal_Create_Form import Create_Form
from public.pages.GM_Portal_Form_Approval import Form_Approval
from public.pages.GM_Portal_Have_FiniShed import Have_FiniShed

class Test_Document(unittest.TestCase):
    """
        测试单据申请
        """

    def setUp(self):
        # cellvalue = ReadExcel("data.xlsx", "Sheet1")
        self.Url = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 0)  # 读取URL地址
        self.username = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 1)  # 读取杜明旭用户名
        self.password = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(1, 2)  # 读取杜明旭密码
        self.username1 = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(2, 1)  # 读取李鑫用户名
        self.password1 = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(2, 2)  # 读取李鑫密码
        self.username2 = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(3, 1)  # 读取白金鑫用户名
        self.password2 = Doexcel.ReadExcel("data.xlsx", "Sheet1").read_excel(3, 2)  # 读取白金鑫密码
        self.driver = webdriver.Chrome()

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    # @unittest.skip("用例1调试完成暂不执行")
    def test_SendToSign01(self):
        '''
        抢占:开始 A-->B(送签)C-->C(结束)
        :return:
        '''
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username,self.password,"电器")
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        # submit.switch_to_default_content()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Send.logger.info("环节三送签开始")
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state,"审批完成","抢占:开始 A-->B(送签)C-->C(结束)用例未通过")
        except AssertionError as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign01失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign01失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.wait(2)
            Have.logger.info("抢占模式用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign1成功用例截图.png")

    # @unittest.skip("用例2已完成")
    def test_SendToSign02(self):
        '''
        开始A->会签B、C(送签)D->D(结束)
        :return:
        '''
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username,self.password,'电器')
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化会签模式多人审批流程')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        # submit.switch_to_default_content()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        lg.login_out()
        lg.login_portal(self.username1,self.password1,'电器')   # 登录账户
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        lg.login_out()
        lg.login_portal(self.username, self.password,'电器')  # 登录账户
        Send.logger.info("环节三送签开始")
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state,"审批完成","开始A->会签B、C(送签)D->D(结束)")
        except AssertionError as e:
            insert_img(self.driver, "test_SendToSign02失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign02失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.logger.info("多人会签模式用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign02成功用例截图.png")

    # @unittest.skip("略略略")
    def test_SendToSign03(self):
        '''
            A(开始)->B(转签)C->C(送签)D(结束)
        :return:
        '''
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, "电器")
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Get_Turn_Sign()
        self.driver.switch_to.window(main_window)
        lg.login_out()
        lg.login_portal(self.username2, self.password2, '电器')  # 登录账户
        Send.logger.info("登录转签人账户开始进行审批")
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        lg.login_out()
        lg.login_portal(self.username, self.password, '电器')  # 登录账户
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state,"审批完成","A(开始)->B(转签)C->C(送签)D(结束)")
        except AssertionError as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign03失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign03失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.wait(2)
            Have.logger.info("转签成功后送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign03成功用例截图.png")

    # @unittest.skip("用例4")
    def test_SendToSign04(self):
        '''
        A(开始)送签->B（环节2）逐级退回到A->
        A（开始）送签->B（会签，最少两个审批人)送签->C(抢占)结束
        :return:
        '''
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, "电器")
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.switch_to_window()
        Send.Back_Button()
        self.driver.switch_to.window(main_window)
        wait.Get_OrderNo(orderno,'退回')                  # 打开单据查看状态是否是退回的
        Send.Return_Start_Send()
        self.driver.switch_to.window(main_window)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        wait.wait(2)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state,"审批完成","A(开始)送签->B（环节2）逐级退回到A->\
                            A（开始）送签->B（会签，最少两个审批人)送签->C(抢占)结束")
        except AssertionError as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign04失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign04失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.wait(2)
            Have.logger.info("退回到开始环节送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign04成功用例截图.png")

    # @unittest.skip("用例5")
    def test_SendToSign05(self):
        '''
        A(开始)送签->B（环节2）直接退回到A->
        A（开始）送签->B（会签，最少两个审批人)送签->C(抢占)结束
        :return:
        '''
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, "电器")
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.switch_to_window()
        Send.Back_Button(val='0')
        self.driver.switch_to.window(main_window)
        wait.Get_OrderNo(orderno,'退回')             # 打开单据查看状态是否是退回的
        wait.switch_to_window()
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        wait.wait(2)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state, "审批完成", "A(开始)送签->B（环节2）直接退回到A->\
                            A（开始）送签->B（会签，最少两个审批人)送签->C(抢占)结束")
        except AssertionError as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign05失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign05失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.wait(2)
            Have.logger.info("直退开始环节送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign05成功用例截图.png")

    # @unittest.skip("用例6")
    def test_SendToSign06(self):
        '''
        A(开始)送签->B（抢占）修改下级审批人为C ->C(送签)结束

        :return:
        '''
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, "电器")
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        # submit.switch_to_default_content()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Modify_Approver_Button()
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        lg.login_out()
        lg.login_portal(self.username2, self.password2, '电器')  # 登录账户
        Send.logger.info("登录修改的审批人用户名开始进行审批")
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state, "审批完成", " A(开始)送签->B（抢占）修改下级审批人为C ->C(送签)结束")
        except AssertionError as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign06失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign06失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.wait(2)
            Have.logger.info("退回到开始环节送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign06成功用例截图.png")

    # @unittest.skip("用例7")
    def test_SendToSign07(self):
        '''
        A(开始)送签->B(会签)直退给A
        验证会签模式退回时不能进行直退
        :return:
        '''
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, '电器')
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化会签模式多人审批流程')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        # submit.switch_to_default_content()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.switch_to_window()
        backtype = Send.assert_Back()
        try:
            self.assertEqual(backtype, "被退环节再提交时”逐级审批“", "A(开始)送签->B(会签)直退给A\
                                        验证会签模式退回时不能进行直退")
        except AssertionError as e:
            Send.wait(2)
            insert_img(self.driver, "test_SendToSign07失败用例截图.png")
            raise Send.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Send.wait(2)
            insert_img(self.driver, "test_SendToSign07失败用例截图.png")
            raise Send.logger.error("验证单据时发生异常：%s" % e)
        else:
            Send.wait(2)
            Send.logger.info("退回到开始环节送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign07成功用例截图.png")

    # @unittest.skip("用例8")
    def test_SendToSign08(self):
        """
        A(开始)送签->B送签C->B撤回单据重新送签->C,C送签（结束）
        :return:
        """
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, "电器")
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.switch_to_window()
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        Have.Select_OrderNo(orderno,'审批中')
        Have.To_Withdraw()
        self.driver.switch_to.window(main_window)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state, "审批完成", " A(开始)送签->B送签C->B撤回单据重新送签->C,C送签（结束）")
        except AssertionError as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign08失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign08失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.wait(2)
            Have.logger.info("撤回后继续送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign08成功用例截图.png")

    # @unittest.skip("用例9")
    def test_SendToSign09(self):
        """
        A(开始)送签->B（加签）C->C（送签）D->D送签（结束）
        :return:
        """
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, "电器")
        main_window = lg.current_window()
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        orderno = submit.submit_from()
        submit.wait(5)
        submit.logger.info("环节二送签开始")
        self.driver.switch_to.window(main_window)
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send = Form_Approval(self.driver)
        Send.Get_Add_Sign()
        self.driver.switch_to.window(main_window)
        lg.login_out()
        lg.login_portal(self.username2, self.password2, '电器')  # 登录账户
        Send.logger.info("登录转签人账户开始进行审批")
        wait = Wait_Handle(self.driver)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        lg.login_out()
        lg.login_portal(self.username, self.password, '电器')  # 登录账户
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        wait.Get_OrderNo(orderno)
        Send.Send_Button()
        self.driver.switch_to.window(main_window)
        Have = Have_FiniShed(self.driver)
        Have.Hava_Page()
        try:
            state = Have.Select_OrderNo(orderno)
            self.assertEqual(state, "审批完成", " A(开始)送签->B（加签）C->C（送签）D->D送签（结束）")
        except AssertionError as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign09失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            Have.wait(2)
            insert_img(self.driver, "test_SendToSign09失败用例截图.png")
            raise Have.logger.error("验证单据时发生异常：%s" % e)
        else:
            Have.wait(2)
            Have.logger.info("加签成功后送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign09成功用例截图.png")

    # @unittest.skip("用例10")
    def test_SendToSign10(self):
        """
        开始环节添加环节->直至送签结束
        :return:
        """
        lg = Login(self.driver)
        lg.open(self.Url)
        lg.login_portal(self.username, self.password, "电器")
        cr = Create_Form(self.driver)
        cr.create_from('自动化非自定义单据')
        submit = Submit_from(self.driver)
        submit.Submit_From_Button()
        try:
            text = submit.Add_Link()
            self.assertEqual(text,"开始环节转签","开始环节添加环节->直至送签结束")
        except AssertionError as e:
            submit.wait(2)
            insert_img(self.driver, "test_SendToSign10失败用例截图.png")
            raise submit.logger.error("验证单据时发生异常：%s" % e)
        except Exception as e:
            submit.wait(2)
            insert_img(self.driver,"test_SendToSign10失败用例截图.png")
            raise submit.logger.error("验证单据时发生异常：%s" % e)
        else:
            submit.wait(2)
            submit.logger.info("加签成功后送签用例执行通过>>>>>>>>>>>>>>>>>")
            insert_img(self.driver, "test_SendToSign10成功用例截图.png")
            submit.wait(2)
            submit.Send_Sign_Button()