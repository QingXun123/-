# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import threading
import time

import requests     #导入requests包
import json
# from selenium import webdriver
import time

# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header

# from selenium.webdriver.common.by import By

flag = False
n_time = None
day = None

def send_mail(to_addr, To_msg, subject, text):#转发邮箱函数： to_addr = 接收者的邮箱, To_msg = 接收者的名字, subject = 邮箱主题, text = 邮箱内容
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '*********@qq.com'
    password = '******************' # 不是登录qq要用的密码，是在qq邮箱"设置"中使用stmp协议功能产生的密码

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(text, 'plain', 'utf-8')
    # 邮件头信息
    msg['From'] = Header('宿舍电量查询程序')  # 发送者
    msg['To'] = Header(To_msg)  # 接收者
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题

    try:
        smtpobj = smtplib.SMTP_SSL(smtp_server)
        # 建立连接--qq邮箱服务和端口号（可百度查询）
        smtpobj.connect(smtp_server, 465)
        # 登录--发送者账号和口令
        smtpobj.login(from_addr, password)
        # 发送邮件
        smtpobj.sendmail(from_addr, to_addr, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")
    finally:
        # 关闭服务器
        smtpobj.quit()

def req():#爬取程序
    global n_time, day
    url = "http://ecard.jyu.edu.cn:8988/web/Common/Tsm.html"  # 210.38.160.91
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
        ,
        "cookie": "JSESSIONID=8C5E5265875ADD82A3C04ADCD4F8C860; username=211110025; ASP.NET_SessionId=av1rtzvcdkiuy53c5yhl4mo5; hallticket=3FDBD0F5454D4F069C99AC242B14CB0E"
    }
    data = {
        "jsondata": "{ \"query_elec_roominfo\": { \"aid\":\"0030000000002501\", \"account\": \"30483\",\"room\": { \"roomid\": \"201\", \"room\": \"201\" },  \"floor\": { \"floorid\": \"\", \"floor\": \"\" }, \"area\": { \"area\": \"嘉应学院\", \"areaname\": \"嘉应学院\" }, \"building\": { \"buildingid\": \"9318\", \"building\": \"中4A栋\" },\"extdata\":\"info1=\" } }"
        , "funname": "synjones.onecard.query.elec.roominfo"
        , "json": "true"
    }
    # 请求表单数据
    response = requests.post(url, data=data, headers=headers)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    # 打印数据
    # print(content)
    errmsg = float(content['query_elec_roominfo']['errmsg'][7:])

    if errmsg < 10.0:
        send_mail('947338658@qq.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('2105287320@qq.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('1286805840@qq.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('2601260031@qq.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('1933727856@qq.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('3132475656@qq.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('2031915277@qq.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('c1470005346@163.com', '201舍友', '宿舍剩余电量不足10，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
    elif errmsg < 40.0:
        send_mail('947338658@qq.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('2105287320@qq.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('1286805840@qq.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('2601260031@qq.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('1933727856@qq.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('3132475656@qq.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('2031915277@qq.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
        send_mail('c1470005346@163.com', '201舍友', '宿舍剩余电量不足40，请及时缴费！\n宿舍剩余电量：' + str(errmsg), '')
    else:
        send_mail('947338658@qq.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')
        send_mail('2105287320@qq.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')
        send_mail('1286805840@qq.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')
        send_mail('2601260031@qq.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')
        send_mail('1933727856@qq.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')
        send_mail('3132475656@qq.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')
        send_mail('2031915277@qq.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')
        send_mail('c1470005346@163.com', '201舍友', '宿舍剩余电量：' + str(errmsg), '')

    if "21:00:00" <= n_time and day == 0:
        day = 1
        n_time = "09:00:00"
        timer_mission(n_time, day)
    else:
        day = 0
        n_time = "21:00:00"
        timer_mission(n_time, day)

def timer_mission(time, num): # 计时器，设置特定时间自动运行爬取电费数据
    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+num)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " " + time,
                                           "%Y-%m-%d %H:%M:%S")
    # 获取距离“num"天“time”点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print(timer_start_time)

    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    timer = threading.Timer(timer_start_time, req)
    timer.start()

# def login():#自动登录校园网
#     driver = webdriver.Chrome()
#     # driver.maximize_window()
#     driver.implicitly_wait("3")
#     url = "http://210.38.163.113/0.htm"
#     driver.get(url)
#     driver.find_element(By.XPATH,
#                         '/html/body/div/div/div[2]/form[1]/div[1]/input[1]').send_keys("*****")#账号
#     driver.find_element(By.XPATH,
#                         '/html/body/div/div/div[2]/form[1]/div[1]/input[2]').send_keys("*****")#密码
#     driver.find_element(By.XPATH,
#                         '/html/body/div/div/div[2]/form[1]/div[2]/input[1]').click()
#     time.sleep(3)
#     driver.close()

def test():#测试是否能登录，真正运行时不调用此函数
    url = "http://ecard.jyu.edu.cn:8988/web/Common/Tsm.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
        , "cookie": "JSESSIONID=8C5E5265875ADD82A3C04ADCD4F8C860; username=211110025; ASP.NET_SessionId=av1rtzvcdkiuy53c5yhl4mo5; hallticket=3FDBD0F5454D4F069C99AC242B14CB0E"
    }
    data = {
        "jsondata": "{ \"query_elec_roominfo\": { \"aid\":\"0030000000002501\", \"account\": \"30483\",\"room\": { \"roomid\": \"201\", \"room\": \"201\" },  \"floor\": { \"floorid\": \"\", \"floor\": \"\" }, \"area\": { \"area\": \"嘉应学院\", \"areaname\": \"嘉应学院\" }, \"building\": { \"buildingid\": \"9318\", \"building\": \"中4A栋\" },\"extdata\":\"info1=\" } }"
        , "funname": "synjones.onecard.query.elec.roominfo"
        , "json": "true"
    }
    # 请求表单数据
    response = requests.post(url, data=data, headers=headers)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    # 打印数据
    print(content)
    errmsg = float(content['query_elec_roominfo']['errmsg'][7:])
    print(errmsg)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # login()
    # test()
    n_time = "21:00:00"
    day = 0
    timer_mission(n_time, day)
    # 发送邮件
    # send_mail('947338658@qq.com', '201舍友', '', '')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
