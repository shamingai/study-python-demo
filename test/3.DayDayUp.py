def dayDAYUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01) # 如果是工作日，则退步1%
        else:
            dayup = dayup*(1+df)
    return dayup # tab靠后了，cpu炸了
dayfactor = 0.01
while dayDAYUp(dayfactor) < 37.78:
    dayfactor += 0.001
print("{:.3f}".format(dayfactor))
