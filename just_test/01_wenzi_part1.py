# -*- coding:UTF-8 -*-

#! /usr/bin/python3
from bs4 import BeautifulSoup
import requests

# 获取正文
if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    # print(req.text)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div',class_='showtxt')
    # print(texts[0].text)
    print(texts[0].text.replace('\xa0'*8,'\n\n'))