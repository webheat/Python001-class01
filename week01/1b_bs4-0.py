# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    # print(tags)
    # for tagstr in tags.find_all('span', attrs={'class': 'title'}):
    print(tags.find('span', attrs={'class': 'other'}))
    print(tags.find('span', attrs={'class': 'title'}))
    print(tags.find('span', attrs={'class': 'title'}).text)
    # for tagstr in tags.find_all('span'):
    #     print(tagstr)
    # for atag in tags.find_all('a'):
    #     print(atag.get('href'))
    #     # 获取所有链接
    #     print(atag.find('span').text)
    #     # 获取电影名字
