#使用format函数，来对结果进行格式化

#定义初始数据
amount = 12618.96

#定义利率
interestRate = 0.0013

#求出利息
interest = amount * interestRate

#打印结果并格式化
print("利率为：",format(interest,".2f"))