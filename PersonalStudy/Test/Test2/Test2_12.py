#如果今天是星期二，那么100天后是星期几

#提示输入
days=eval(input("请在此输入天数："))

#定义一周有几天
weekday = days // 7

#定义变量接收周几
someDay = days % 7

#输出结果
print(days,"天是第",weekday,"周星期",someDay)