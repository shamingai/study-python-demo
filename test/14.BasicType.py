# -*- coding: utf-8 -*- 
# @Time : 2020/7/13 11:39 PM 
# @Author : zhaotong 
# @File : 14.BasicType.py

# 集合类型
A = {"python", 123, ("python",123)} # 使用{}建立集合
print("A", A)
B = set("pypy123") # 使用set()建立集合
print("B", B)
C = {"python", 123, "python",123}
print("C", C)
print("A|B", A|B)
print("A-B", A-B)
print("B-A", B-A)
print("A&B", A&B)
print("A^B", A^B)
print("A<=B", A<=B)
print("A>=B", A>=B)
# print("A|=B", A|=B)
for item in A:
    print(item, end="")

# 序列类型 = 字符串类型 + 元组类型(可不加小括号) + 列表类型
D = ["p", "y", 123]
print("\nD[::-1]", D[::-1])
print(len(D))
# print(max(D[2]))
# 元组类型，创建后不可修改，没有特殊操作（继承序列类型通用操作）
E = "cat", "dog", "tiger", "human"
print("E[::-1]", E[::-1])

# 列表类型，序列，可以随意修改
F = ["cat", "dog", "tiger", 1024]
G = F
print("G", G)
del F[1]
print("F", F)
print("G", G)
H = F.copy()
del F[1]
print("F", F)
print("G", G)
print("H", H)
