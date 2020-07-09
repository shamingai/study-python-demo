# -*- coding: utf-8 -*- 
# @Time : 2020/7/9 2:14 PM 
# @Author : zhaotong 
# @File : 2.Turtle7.py

import turtle as t
import time
t.setup(800, 400, 10, 10)

# point
pointA = (0, 100)
pointB = (0, 0)
pointC = (0, -100)
pointD = (100, 100)
pointE = (100, 0)
pointF = (100, -100)
def x(i):
    if i == 0:
        return -300
    elif i == 1:
        return -150
    elif i == 2:
        return 50
    else:
        return 200
def changeX(i):
    global pointA
    global pointB
    global pointC
    global pointD
    global pointE
    global pointF
    pointA = (0 + x(i), 100)
    pointB = (0 + x(i), 0)
    pointC = (0 + x(i), -100)
    pointD = (100 + x(i), 100)
    pointE = (100 + x(i), 0)
    pointF = (100 + x(i), -100)

# line
def line(pointStart, pointEnd):
    t.penup()
    t.goto(pointStart)
    t.pendown()
    t.goto(pointEnd)
# number
def number(num):
    line1 = [pointB, pointE]
    line2 = (pointE, pointF)
    line3 = (pointC, pointF)
    line4 = (pointB, pointC)
    line5 = (pointA, pointB)
    line6 = (pointA, pointD)
    line7 = (pointD, pointE)

    if 1 == num:
        line(line7[0], line7[1])
        line(line2[0], line2[1])
    elif 2 == num:
        line(line6[0], line6[1])
        line(line7[0], line7[1])
        line(line1[0], line1[1])
        line(line4[0], line4[1])
        line(line3[0], line3[1])
    elif 3 == num:
        line(line6[0], line6[1])
        line(line7[0], line7[1])
        line(line1[0], line1[1])
        line(line2[0], line2[1])
        line(line3[0], line3[1])
    elif 4 == num:
        line(line5[0], line5[1])
        line(line1[0], line1[1])
        line(line7[0], line7[1])
        line(line2[0], line2[1])
    elif 5 == num:
        line(line6[0], line6[1])
        line(line5[0], line5[1])
        line(line1[0], line1[1])
        line(line2[0], line2[1])
        line(line3[1], line3[0])
    elif 6 == num:
        line(line6[0], line6[1])
        line(line5[0], line5[1])
        line(line4[0], line4[1])
        line(line3[0], line3[1])
        line(line2[0], line2[1])
        line(line1[1], line1[0])
    elif 7 == num:
        line(line6[0], line6[1])
        line(line7[0], line7[1])
        line(line2[0], line2[1])
    elif 8 == num:
        line(line6[0], line6[1])
        line(line5[0], line5[1])
        line(line4[0], line4[1])
        line(line1[0], line1[1])
        line(line3[0], line3[1])
        line(line7[0], line7[1])
        line(line2[0], line2[1])
    elif 9 == num:
        line(line6[0], line6[1])
        line(line5[0], line5[1])
        line(line1[0], line1[1])
        line(line7[0], line7[1])
        line(line2[0], line2[1])
        line(line3[1], line3[0])
    else:
        line(line6[0], line6[1])
        line(line5[0], line5[1])
        line(line4[0], line4[1])
        line(line7[0], line7[1])
        line(line2[0], line2[1])
        line(line3[0], line3[1])

# print
def printTime():
    now = time.time()
    strnow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
    print(strnow)
    for i in range(4):
        changeX(i)
        if i == 0:
            number(eval(strnow[-5]))
        elif i == 1:
            number(eval(strnow[-4]))
        elif i == 2:
            number(eval(strnow[-2]))
        else:
            number(eval(strnow[-1]))

if __name__ == '__main__':
    for i in range(1000):
        printTime()
        time.sleep(0.5)
        t.clear()

#-------------draft------------
# # t.seth(10)
# print("0", t.pos())
#
# for i in range(2):
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.goto(100, 0)
#     print("1", t.pos())
#
# t.rt(90)
# t.fd(100)
# # t.goto(100,100)
# print("2", t.pos())
#
# t.rt(90)
# t.fd(100)
# print("3", t.pos())
#
# t.rt(90)
# t.fd(100)
# print("4", t.pos())
#
# # t.rt(90)
# t.fd(100)
# print("5", t.pos())
#
# t.rt(90)
# t.fd(100)
# print("6", t.pos())
#
# t.rt(90)
# t.fd(100)
# print("7", t.pos())
t.done()