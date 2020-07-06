# -*- coding: utf-8 -*- 
# @Time : 2020/7/6 2:36 PM 
# @Author : zhaotong 
# @File : 5.TimeProfCount.py

import time as t

s = t.perf_counter()
e = t.perf_counter()
print("no sleep:",e - s)

def wait():
    s1 = t.perf_counter()
    t.sleep(3.3)
    e1 = t.perf_counter()
    return e1 - s1
print("sleep 3.3s:",wait())