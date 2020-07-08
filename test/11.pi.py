# -*- coding: utf-8 -*- 
# @Time : 2020/7/8 9:54 PM 
# @Author : zhaotong 
# @File : 11.pi.py

# 近似公式计算法
k = 0
pi = 0
for k in range(20):
    pi += 1/pow(16, k) * (
        4/(8 * k + 1) - 2/(8 * k + 4) - 1/(8*k + 5) - 1/(8 * k + 6)
    )
print(pi)

# 蒙特卡罗法
from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter() - start))