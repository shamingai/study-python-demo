C = input("请输入一个整数：")
tempStr = "Hello World"
if eval(C) == 0:
    print(tempStr)
elif eval(C) > 0:
    index = 0
    while 1:
        index += 1
        print(eval(tempStr[index,index+1]), end = "")
        if index == len(tempStr) - 1:
            break
else:
    index = 0
    while 1:
        print(tempStr[index])
        index += 1
        if index == len(tempStr):
            break