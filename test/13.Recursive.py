# -*- coding: utf-8 -*- 
# @Time : 2020/7/10 8:45 PM 
# @Author : zhaotong 
# @File : 13.Recursive.py

# # 字符串反转
# S = (1, 2, 3, 4)
# print(S)
# print(S[::-1])
#
# # 斐波那契数列：1、1、2、3、5、8、13、21、34
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(8))

# 汉诺塔问题：A搬到C，相当于A搬到n-1个盘到B
count = 0
def hannoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hannoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hannoi(n-1, mid, dst, src)
hannoi(4, "A", "B", "C")
print(count)