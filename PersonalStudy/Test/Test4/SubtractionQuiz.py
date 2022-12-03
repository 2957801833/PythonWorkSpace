#减法练习page98

#导入产生随机数包
import random

#产生两个随机的一位整数 number1 和 number2
number1 = random.randint(0,9)
number2 = random.randint(0,9)

#如果number1<number2，将number2的值交换给number1
if number1<number2:
    number1,number2 = number2,number1

#提示学生回答“number1-number2”的结果
answer = eval(input(str(number1) + "-" + str(number2) + "的结果是："))

#检查答案是否正确，然后显示输出结果是否正确
if number1-number2 == answer:
    print("正确")
else:
    print("结果错误",number1 ,"-",number2,"的结果是",number1-number2 )