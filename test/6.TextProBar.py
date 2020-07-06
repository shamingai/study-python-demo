# -*- coding: utf-8 -*- 
# @Time : 2020/7/6 3:02 PM 
# @Author : zhaotong 
# @File : 6.TextProBar.py

import time as t
scale = 10
print("----执行开始----")

for i in range(scale + 1):
    a = '*'*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    # print("{:>3.0f}%[{}->{}]".format(c,a,b))
    print("\r{:>3.0f}%[{}->{}]".format(c,a,b), end='')
    t.sleep(0.1)

# print("----执行结束----")
print("\n"+"执行结束".center(scale//1,'-'))