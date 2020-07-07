# -*- coding: utf-8 -*- 
# @Time : 2020/7/7 9:39 PM 
# @Author : zhaotong 
# @File : 10.random.py
# 梅森旋转算法的伪随机序列

# 只要种子相同，产生的随机数关系，随机序列都是一样的
import random as r
r.seed(10)
print(r.random())
print(r.random())
r.seed(10)
print(r.random())
print(r.random())

s = [1,2,3,4,5,6]
r.shuffle(s) # 乱序
print(s)
print(r.choice(s)) # 随机选一个
print(r.choice(s))
print(r.randrange(10,100,10)) # 10到100之间，步长为10，随机生成一个