# # 随机位数的密码
# import random
# def genpwd(length):
#     for i in range(length + 1):
#         ch = '%d'%random.randint(0, 10)
#         str += ch
#         return str
#
# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))

## 当前数之后产出5个质数
# import math
# cou = 0
# s = []
# def prime(m):
#     count = 0
#     for i in range(2, m+1):
#         if m % i == 0:
#             count += 1
#     return 1 if count == 1 else 0
#
# n = math.ceil(eval(input("输入：")))
# while True:
#     prime(n)
#     if prime(n) == 1:
#         cou += 1
#         s.append(str(n))
#         if cou == 5:
#             break
#     n += 1
# print(','.join(s))




# # 100以内的质数之和
# sum = 0
# for i in range(1, 100):
#     count = 0
#     for j in range(2, i+1):
#         if i % j == 0:
#             count += 1
#     if count == 1:
#         sum += i
# print(sum)

# # 4位玫瑰数
# import math
# for i in range(1000, 9999):
#     s = str(i)
#     for j in range(5):
#         r = math.pow(eval(s[0]), j) + math.pow(eval(s[1]), j) + math.pow(eval(s[2]), j) + math.pow(eval(s[3]), j)
#         if i == r:
#             print(i, j)

# # 切片
# s = eval(input("请输入数字："))
# r = "零一二三四五六七"
# print(r[s])

# a=input()
# r = pow(eval(a), 0.5)
# print("{:+>30.3f}".format(r))

# s = 'fkld'
# # for i in s:
# #     print(i)
# index = 0
# while 1:
#     print(s[index])
#     index += 1
#     if index == len(s):
#         break

# str2 = "[10, 20, 30]"
# strl = eval(str2)
# print(type(strl))
# # <class 'list'>
#
# str3 = "5"
# print(type(eval(str3)))
#

# eval(): 将字符串形式的数据，转换为原本的类型
# str1 = "3.14"
# print(type(eval(str1)))
# # <class 'float'>
#
# # print("Hello World");