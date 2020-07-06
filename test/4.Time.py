# -*- coding: utf-8 -*- 
# @Time : 2020/7/6 2:23 PM 
# @Author : zhaotong 
# @File : 4.Time.py.py

import time as t

print(t.time())
print(t.ctime())
print(t.gmtime())

f = t.strftime("%Y-%m-%d %H:%M:%S", t.gmtime())
print(f)


