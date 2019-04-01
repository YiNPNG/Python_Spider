# -*- coding:UTF-8 -*-
#! /usr/bin/python3

from bs4 import BeautifulSoup
import requests

class download_wenzi:
    def __init__(self):
        self.server_url = 'http://www.biqukan.com/'
        self.host_url = 'http://www.biqukan.com/1_1094/'

    def get_url(self):
        req = requests.get(url=self.host_url)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div',class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        self.a = a_bf.find_all('a')

    def get_text(self,file_n):
        for each in range(2,12):
            print(self.a[each].string)
            file_n.write(self.a[each].string + '\n')
            req = requests.get(url=self.server_url+self.a[each].get('href'))
            html = req.text
            bf = BeautifulSoup(html)
            texts = bf.find_all('div',class_='showtxt')
            file_n.write(texts[0].text.replace('\xa0'*8,'\n') + '\n\n')

if __name__ == '__main__':
    down = download_wenzi()
    down.get_url()
    try:
        with open('wenzi.txt','w') as file_na:
            down.get_text(file_na)
    except:
        print('open file error')