#!/usr/bin/env python
from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import globalconfig
import time

# **************
# 定义截图方法
# **************
def insert_img(driver,filename):
    # func_path = os.path.dirname(__file__)
    # print(func_path)
    #
    # base_dir = os.path.dirname(func_path)
    # print(base_dir)
    #
    # base_dir = str(base_dir)
    # base_dir = base_dir.replace('\\','/')
    # print(base_dir)
    # base = base_dir.split('/Website')[0]
    # print(base)
    screenshot_path = globalconfig.screenshot_path
    data_time = time.strftime('%Y-%m-%d')   # 当前日期时间
    filepath = screenshot_path + '\\' + data_time + filename
    driver.get_screenshot_as_file(filepath)

# *************
# 发送邮件
# *************
def send_mail(latest_report):
    f = open(latest_report,'rb')
    mail_content = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名密码
    user = 'testdumingxu@163.com'
    password = 'dmx159753'
    # 发送和接收人邮箱
    sender = 'testdumingxu@163.com'
    receives = ['dumingxu@gome.com.cn']         # 测试邮箱 'dumingxu12@163.com','315832247@qq.com'
    # 发送邮件主题和内容
    subject = 'OA自动化测试报告'
    # content = '<html><h1 style="color:red">我要自学成才！</h1></html>'
    # HTML 邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receives)
    # SSl 协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 邮箱登录服务器用户名和密码
    smtp.login(user, password)

    print("开始发送邮件...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("发送邮件完成...")

# *******************
# 获取最新测试报告文件
# *******************
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is   " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file




if __name__=='__main__':
    #以下代码验证发送邮件和截图
    #测试报告路径
    report_path = globalconfig.report_path
    new_report = latest_report(report_path)
    send_mail(new_report)
    # driver = webdriver.Chrome()
    # driver.get("http://www.sogou.com")
    # insert_img(driver,'sougou1.png')
    # driver.quit()