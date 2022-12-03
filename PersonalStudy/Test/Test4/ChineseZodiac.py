#判断给定的年份属于哪一个生肖

#让用户在控制台输入年份
year = eval(input("请在此输入年份："))

#初始化生肖年
zodiacYear = year % 12

#判断输入的年份对应的生肖是哪一个
if zodiacYear == 0:
    print("申猴")
elif zodiacYear == 1:
    print("酉鸡")
elif zodiacYear == 2:
    print("戌狗")
elif zodiacYear == 3:
    print("亥猪")
elif zodiacYear == 4:
    print("子鼠")
elif zodiacYear == 5:
    print("丑牛")
elif zodiacYear == 6:
    print("寅虎")
elif zodiacYear == 7:
    print("卯兔")
elif zodiacYear == 8:
    print("辰龙")
elif zodiacYear == 9:
    print("巳蛇")
elif zodiacYear == 10:
    print("午马")
else:
    print("未羊")
