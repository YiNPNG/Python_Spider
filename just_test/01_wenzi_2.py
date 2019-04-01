# -*- coding:UTF-8 -*-
#! /usr/bin/python3

from bs4 import BeautifulSoup
import requests
import signal,os

class Download_wenzi:
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
    
    def get_text(self,start):
        for each in range(start,10,2):
            print(self.a[each].string)
            f = open(self.a[each].string,'w')
            f.write(self.a[each].string + '\n')
            req = requests.get(url=self.server_url + self.a[each].get('href'))
            html = req.text
            bf = BeautifulSoup(html)
            texts = bf.find_all('div',class_='showtxt')
            f.write(texts[0].text.replace('\xa0'*8,'\n') + '\n\n')
            f.close()
    
if __name__ == "__main__":
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    down = Download_wenzi()
    down.get_url()
    pid = os.fork()
    if pid < 0:
        print('error')
    elif pid == 0:
        down.get_text(5)
    else:
        down.get_text(6)
