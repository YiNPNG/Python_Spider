# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

# 获取章节链接
if __name__ == '__main__':
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    # 构造一个向服务器请求资源的request对象
    # 返回一个包含服务器资源的response对象
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div',class_='listmain')
    # print(div[0])
    # print(dir(div))
    # print(type(div))
    # print(div)
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    # print(a_bf)
    b = 0
    for each in a:
        # print(type(each))
        # print(each)
        if b < 2:
            print(each.string,server+each.get('href'))
        b += 1