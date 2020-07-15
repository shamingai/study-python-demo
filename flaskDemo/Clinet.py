# -*- coding: utf-8 -*- 
# @Time : 2020/7/14 1:08 AM 
# @Author : zhaotong 
# @File : Clinet.py

import urllib.parse
import urllib.request

# upload 需要添加header（http规定）
# download
url = "http://127.0.0.1:5000/down"

try:
    html = urllib.request.urlopen(url)
    html = html.read()
    print(html)
    fileName = html.decode()
    print("准备下载：" + fileName)

    data = urllib.request.urlopen(url + "?fileName=" + urllib.parse.quote(fileName))
    data = data.read()

    fobj = open("download" + fileName, "wb")
    fobj.write(data)
    fobj.close()
    print("下载完毕：", len(data), "字节")

except Exception as err:
    print(err)

## get/post
# p = "广东"
# c = "深圳"
# note = "巴拉巴拉一堆环境介绍"
#
# p = urllib.parse.quote(p)
# c = urllib.parse.quote(c)
# note = "note=" + urllib.parse.quote(note)
#
# data = "provice=" + p + "&city=" + c
#
# html = urllib.request.urlopen(url + "?" + data, data=note.encode())
# html = html.read()
# html = html.decode()

# print(html)