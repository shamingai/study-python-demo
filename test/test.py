# # print("Hello World");
#
# # eval(): 将字符串形式的数据，转换为原本的类型
# str1 = "3.14"
# print(type(eval(str1)))
# # <class 'float'>
#
# str2 = "[10, 20, 30]"
# strl = eval(str2)
# print(type(strl))
# # <class 'list'>
#
# str3 = "5"
# print(type(eval(str3)))

s = 'fkld'
# for i in s:
#     print(i)
index = 0
while 1:
    print(s[index])
    index += 1
    if index == len(s):
        break