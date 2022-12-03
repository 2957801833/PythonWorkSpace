#加法练习程序page91

#导包
import random

#产生两个一位整数，number1和number2
number1 = random.randint(0,9)
number2 = random.randint(0,9)

#提示回答结果
answer = eval(input("这个算式：" + str(number1) + "+" + str(number2) + "结果是多少"))

#检测答案是否正确
print(number1 ,"+",number2,"=",answer,"是",number1 + number2 == answer)