'''
多行注释 三个引号
数据类型
变量的语法：
变量名 = 数据值
数据值是有类型约束的

针对于数据类型 其实还有很多，我们今天上午先 记住 整数，小数，字符串
整数          3               int
小数          3.14            float[double]
字符串        "iPhone"         str
布尔值         True/False      boolean
'''
# 定义3个变量 整数，小数，字符串
# 整数  单行注释
num = 3
# 变量名 遵循 字母 数字 下划线 不能以数字开头 变量名 = 数据值
# 价格 price# 小数
price = 3.14
# 字符串  必须添加引号【单引号或者双引号】
name = "iPhone"
# ② 如何 知道 这个变量 存储的数据值的类型？？？
# 我们借助于 type(数据值/变量名) 来知道
# 例如： type(1)    1 是数据值
# 例如： type(name)    name 没有引号 表示 变量名
# type(num)
# type() 确实可以知道数据的类型，必须配合 print() 来打印
print(   type(num)   )
print(   type(price) )
print(   type(name)  )