#在控制台输入营业额并接收数据
purchaseAmount = eval(input("请在此输入数据："))

#营业税是销售额的6%，以此计算出营业税税额并返回数据
tax = purchaseAmount * 0.06

#将营业税税额转换为两位小数所显示的数据，并打印到控制台
print("营业税为：",int(tax*100)/100.0)