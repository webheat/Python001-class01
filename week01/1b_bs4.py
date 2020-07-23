# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装

import os
from requests_html import HTMLSession
from requests_file import FileAdapter

session = HTMLSession()

session.mount('file://', FileAdapter())


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent': user_agent}

# myurl = 'https://movie.douban.com/top250'
# myurl = 'https://maoyan.com/films?showType=3'
myurl = "file:///D://vue2//geekbangtrain//maoyan.html"

#html_obj = session.get(f'file:///D://vue2//geekbangtrain//maoyan.html')
html_obj = session.get(
    f'file:///D://vue2//Python001-class01//week01//maoyan.html')
# print(html_obj.text)
#response = requests.get(myurl, headers=header)

# with open('D://vue2//geekbangtrain//maoyan.html', 'r', encoding='utf-8') as f:
#    print(f.read())

# bs_info = bs(response.text, 'html.parser')
bs_info = bs(html_obj.text, 'html.parser')
# print(bs_info)

# # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
# # for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
# for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}):
for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    # print(tags)
    for atag in tags.find_all('a'):
        # print(atag)
        print(atag.get('href'))
        # 获取所有链接
        print(atag.text)
        # print(atag.find('span').text)
        # print(atag.find('span'), attrs={'class': 'name'})
        # print(atag.get('span'))
        # 获取电影名字