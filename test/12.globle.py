# -*- coding: utf-8 -*- 
# @Time : 2020/7/8 11:47 PM 
# @Author : zhaotong 
# @File : 12.globle.py

# 1、局部变量和全局变量是不同变量
n,s = 10, 100
def fact(n):
    # s = 1 # 局部变量与全局变量可重名
    global s # 声明使用全局变量
    for i in range(1, n+1):
        s *= i
    return s
print(fact(n), s)

# 2、局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F", "f"] # 通过真实创建的ls是全局变量
def func(a):
    # ls = []
    ls.append(a) # 此处ls是列表类型，未真实创建则等同于全局变量
    return
func("c")
print(ls)