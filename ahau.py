# -*- coding:utf-8 -*-
"""
@author:SimonHu
@file:domy.py
@time:2018/8/4 19:16
formatting shift+f
run alt+x
debug alt+d
"""
import os
import pandas
from prettytable import PrettyTable

from bs4 import BeautifulSoup
import requests
from splinter.browser import Browser
import time

# cookie overdue time=Tue Aug 06 2019 20:41:21 GMT+0800 (中国标准时间)


post_data = {
    'xnm': '2017',  # 2017就代表2017-2018学年，e.g 2016就是代表2016-2017
    'xqm': '12',  # 3为第一学期，12为第二学期
    'nd': '1533559378012',
    'queryModel.showCount': '45',
    'queryModel.currentPage': '1',
    'queryModel.sortOrder': 'asc',
    'time': '1'
}

login_url = 'http://newjwxt.ahau.edu.cn/jwglxt/xtgl/login_slogin.html'  # 登录界面
url = 'http://newjwxt.ahau.edu.cn/jwglxt/xtgl/index_initMenu.html'  # 用户主界面
query_url = 'http://newjwxt.ahau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005'  # 查询成绩界面
session = requests.Session()
username = 'xxxxx'
password = 'xxxxx'


def get_cookies():  # 模拟登录获取jsession，规避js加密算法
    driver = Browser(driver_name='chrome',
                     executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe', headless=True)
    driver.visit(login_url)
    driver.fill('yhm', username)  # name,value
    driver.find_by_id('mm').fill(password)
    driver.click_link_by_id('dl')
    for k, v in driver.cookies.all().items():
        return v  # 返回cookies


if __name__ == '__main__':
    # 先启动VPN，这一步可有可无，可以手动开启。
    # result=os.popen(r'C:\Program Files (x86)\Sangfor\SSL\SangforCSClient\SangforCSClient.exe')
    # time.sleep(10)
    s_time = time.time()
    jsessionid = get_cookies()
    print(jsessionid)
    query_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        'Connection': 'Keep-Alive',
        'Cookie': 'JSESSIONID={}'.format(str(jsessionid)),
        'Referer': 'http://newjwxt.ahau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=15103829'

    }
    query_score = session.post(query_url, data=post_data, headers=query_headers)
    soup = BeautifulSoup(query_score.text, 'lxml')
    content = soup.text
    jw = pandas.read_json(content)
    print(type(jw))
    th = PrettyTable(['课程名称', '课程性质', '学分', '成绩'])
    for i in jw['items']:
        if 'kclbmc' in i:
            th.add_row([i['kcmc'], i['kclbmc'], i['xf'], i['cj']])
        else:
            th.add_row([i['kcmc'], '必修课', i['xf'], i['cj']])
    print(th)
    e_time = time.time()
    print(e_time - s_time)
