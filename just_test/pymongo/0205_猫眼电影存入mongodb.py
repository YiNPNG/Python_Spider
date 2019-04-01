# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:21:01 2019

@author: Python
"""
import re
import urllib.request
import csv
import pymongo

class MaoyanSpider(object):
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset="
        self.headers = {"User-Agent":"Mozilla/5.0 \
(Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 \
(KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
        self.offset = 0
        # 创建连接对象
        self.conn = pymongo.MongoClient('localhost',27017)
        # 库对象
        self.db = self.conn['MaoDB']
        # 集合对象
        self.myset = self.db['film']

    # 获取页面
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
#        print(html)
        self.parsePage(html)
    
    # 解析页面
    def parsePage(self,html):
        # 创建编译对象
        p = re.compile('<div class="movie-item-info">.*?title="\
(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?\
<i class="integer">(.*?)</i>.*?class="fraction">(.*?)</i>',re.S)
        r = p.findall(html)
#        print(r)
        # [(),(),(),....]
        # self.writeToCSV(r)
        self.writeToMongodb(r)
    
    # 保存数据
    def writeToCSV(self,r):
        for i in r:
            j = []
            j = [i[0].strip(),i[1].strip(),i[2].strip(),
                 i[3].strip()+i[4].strip()]
            print(j)
            with open('猫眼.csv','a',newline="",encoding="gb18030") as f:
                # 创建写入对象
                writer = csv.writer(f)
                # 调用writerow()方法
                writer.writerow(j)   
           
    def writeToMongodb(self,r):
        """
        d = {
            "name":j[0].strip(),
            "star":j[1].strip(),
            "releasetime":j[2].strip(),
            "fen":j[3].strip()
        }
        """
        for i in r:
            j = []
            j = [i[0].strip(),i[1].strip(),i[2].strip(),
                 i[3].strip()+i[4].strip()]
            d = {
                "name":j[0],
                "star":j[1],
                "releasetime":j[2],
                "fen":j[3]
            }
            print(d)     
            self.myset.insert(d)
        print('成功存入')
    
    # 主函数
    def workOn(self):
        while True:
            c = input("爬取按y，退出按q:")
            if c.strip().lower() == "y":
                url = self.baseurl + str(self.offset)
                self.getPage(url)
                self.offset += 10
            else:
                print("结束")
                break
    
if __name__ == "__main__":
    spider = MaoyanSpider()
    spider.workOn()
