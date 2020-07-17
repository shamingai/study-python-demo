# -*- coding: utf-8 -*- 
# @Time : 2020/7/16 6:48 PM 
# @Author : zhaotong 
# @File : 15.Yield.py

def gen(n):
    for i in range(n):
        print("i:", i)
        yield i**2 # 生成器，每次产生一个值函数就被冻结，类似range

for j in gen(5):
    print("gen(i):", j)
