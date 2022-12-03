#如果今天是星期二，那么一百天后是星期几

#提示用户输入
days = eval(input("请在此输入天数："))

#指定一周有几天
weekday = days // 7

#指定星期二
thu = 2

#定义变量接收时间
somDay = (thu+days)%7

#输出结果
print("今天是周二",days,"天后是第",weekday,"周星期",somDay)