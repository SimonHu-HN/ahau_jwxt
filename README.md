## 安徽农业大学/安农大教务系统成绩查询

**Author: [SimonHu](https://github.com/SimonHu-HN)**

[![Build with python3.5](https://img.shields.io/badge/build%20with-python%203+-green.svg)](https://www.python.org/downloads/release/python-350/)
[![CodeFactor](https://www.codefactor.io/repository/github/simonhu-hn/wiki_emperor/badge/master)](https://www.codefactor.io/repository/github/simonhu-hn/wiki_emperor/overview/master)

---

### 介绍/Introduction：

---

写成时间于一年前，原来的正方系统只需要requests就可以爬取到数据，新版则需要采用【[Splinter](https://splinter-docs-zh-cn.readthedocs.io/zh/latest/),[Selenium](https://www.selenium.dev/documentation/zh-cn/),[Pyppeteer](https://miyakogi.github.io/pyppeteer/)】先渲染拿到cookies（可以用headless模式)，然后构造正确的headers，随后就可以用requests访问了。在获取到数据后使用pandas处理，再使用PrettyTable让数据更加好看。如果你是想尝试便捷查成绩或者学习爬虫的安农学弟学妹，可以试一试，有问题在issues里提出来。现在该爬虫是否可行我已无从知晓了，因为↓

![image-20200523001306681](https://raw.githubusercontent.com/SimonHu-HN/GoPic_Private/master/img/image-20200523001306681.png)

（My AHAU story is over :smirk:）

### 需求/Requirements：

---

```
#python lib

prettytable==0.7.2
requests==2.22.0
splinter==0.7.7
pandas==0.23.4
beautifulsoup4==4.9.1

$ pip install ...
```

### 使用/Usage：

---

```
1.如果你的Lib没有装齐，就首先 pip install -r requirements.txt
2.打开ahau.py,自行编辑参数

#line 22-29
post_data = {
    'xnm': '2017',  # 2017就代表2017-2018学年，e.g 2016就是代表2016-2017
    'xqm': '12',  # 3为XX学年第一学期，12为XX学年第二学期
    'nd': '1533559378012',
    'queryModel.showCount': '45',
    'queryModel.currentPage': '1',
    'queryModel.sortOrder': 'asc',
    'time': '1'
}

# line 36-37
username = 'xxx'  #自己的用户名
password = 'xxx'  #自己的密码

# 启动sangforVPN，建议你自己手动开启，自动开启的代码被我注释了，代码如下
# line 52-54
    # 先启动VPN，这一步可有可无，可以手动开启。
    # result=os.popen(r'C:\Program Files (x86)\Sangfor\SSL\SangforCSClient\SangforCSClient.exe')
    # time.sleep(10)
    
3. $ python ahau.py
```



### 生成内容/Output Content：

---

印象中输出效果还可以，挺适合终端浏览的，但是现在我↓

![image-20200523001306681](https://raw.githubusercontent.com/SimonHu-HN/GoPic_Private/master/img/image-20200523001306681.png)