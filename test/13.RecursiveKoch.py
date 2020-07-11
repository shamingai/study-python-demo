# -*- coding: utf-8 -*- 
# @Time : 2020/7/11 4:22 PM 
# @Author : zhaotong 
# @File : 13.RecursiveKoch.py

import turtle as t
t.setup(800, 800, 20, 20)
t.penup()
t.goto(-300, 150)
t.pendown()

def koch(n, len):
    if n == 0:
        t.forward(len)
    elif n == 1: # TODO:简化角度
        t.forward(len/3)
        t.lt(60)
        t.forward(len/3)
        t.rt(120)
        t.forward(len/3)
        t.lt(60)
        t.forward(len/3)
    else:
        koch(n-1, len/3)
        t.lt(60)
        koch(n-1, len/3)
        t.rt(120)
        koch(n-1, len/3)
        t.lt(60)
        koch(n-1, len/3)

if __name__ == '__main__':
    # i = eval(input("科赫雪花阶数："))
    # inLen = 600
    for i in range(3):
        koch(3, 600)
        t.rt(120)
    t.done()
