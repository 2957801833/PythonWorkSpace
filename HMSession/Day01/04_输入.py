'''
我们需要的是 通过程序 来输入一个数值
我们要用一个变量接收这个数值
然后对数值进行类似于计算的操作
num = 5
print(数量 * 价格)
print(num * 10)
print(5 * 10)
'''
#方式一
# num1 = input("请输入数字：")
# num2 = input("请输入数字：")
# ji = int(num1) * int(num2)
# print(ji)
#方式二
num1,num2=eval(input("请输入两个数字（数字请用英文逗号隔开，例如：1,2）："))
ji = int(num1)*int(num2)
print(ji)
