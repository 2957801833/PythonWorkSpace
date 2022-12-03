#根据提示在控制台输入多个值，并计算出平均值
number1 = eval(input("请输入第一个值："))
number2 = eval(input("请输入第二个值："))
number3 = eval(input("请输入第三个值："))

#求平均值并将值赋予一个变量
average = ( number1 + number2 + number3)/3

#输出结果
print("求出这三个数字",number1,number2,number3,"的平均值",average)
