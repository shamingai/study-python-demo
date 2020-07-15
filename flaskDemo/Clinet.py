# -*- coding: utf-8 -*- 
# @Time : 2020/7/14 1:08 AM 
# @Author : zhaotong 
# @File : Clinet.py

import urllib.parse
import urllib.request
url = "http://127.0.0.1:5000"
p = "广东"
c = "深圳"
note = "巴拉巴拉一堆环境介绍"

p = urllib.parse.quote(p)
c = urllib.parse.quote(c)
note = "note=" + urllib.parse.quote(note)

data = "provice=" + p + "&city=" + c

html = urllib.request.urlopen(url + "?" + data, data=note.encode())
html = html.read()
html = html.decode()

print(html)