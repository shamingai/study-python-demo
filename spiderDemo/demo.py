# -*- coding: utf-8 -*- 
# @Time : 2020/7/15 11:17 PM 
# @Author : zhaotong 
# @File : spiderDemo.py

# https://bj.ke.com/robots.txt
# https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
import requests
from bs4 import BeautifulSoup
import bs4

# TODO:分页
url = "https://tj.fang.ke.com/loupan/p4/"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    soup = BeautifulSoup(r.text, 'html.parser')
    list = []
    for tr in soup.find("ul", "resblock-list-wrapper").children:
        if isinstance(tr, bs4.element.Tag):
            name = tr.find("a", "name").string
            number = tr.find("span", "number").string
            totalNum = tr.find("div", "second").string
            location = tr.find("a", "resblock-location").contents[2]
            list.append([name, number, totalNum, location])

    tplt = "{:<15}\t{:<6}\t{:<10}\t{:<10}"
    print(tplt.format("楼盘", "均价", "总价", "地址"))
    for i in range(len(list)):
        l = list[i]
        print(tplt.format(l[0], l[1], l[2][2:], l[3][:-6]))

except Exception as err:
    print(err)

# import requests
# from bs4 import BeautifulSoup
# import bs4
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""
# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[3].string])
# def printUnivList(ulist, num):
#     pass
#     print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
#     for i in range(num):
#         u = ulist[i]
#         print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
# def main():
#     uinfo = []
#     url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     printUnivList(uinfo, 20)  # 20 univs
# main()