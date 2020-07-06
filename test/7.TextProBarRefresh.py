# -*- coding: utf-8 -*- 
# @Time : 2020/7/6 3:26 PM 
# @Author : zhaotong 
# @File : 7.TextProBarRefresh.py

import time as t
for i in range(101):
    print("\r{:0>3}%".format(i), end="")
    t.sleep(0.1)
