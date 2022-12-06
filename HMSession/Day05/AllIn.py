# # 查看变量地址值
# a = 1
# b = 1
# print(id(a))
# print(id(b))
# c = b
# print(id(c))

# 在Python中，西数的参数和返回值传递都是引用信息
# 形参和实参指向同一个地址
# #形参和实参是引用
# 交量名=西数名()西数内部的return地址和变量名的地址是同一个地址
# 1.定义一个函数
# 返回2个数的和
# def get_2_sum(num1,num2):
#     print(id(num1))
#     result = num1 + num2
#     return result
# # 2.调用函数
# x = 10
# y = 20
# r = get_2_sum(x,y)
# print(id(r))
# print(r)
# data_dict_1 = {"name": "如花"}
# print(id(data_dict_1))
# data_dict_1["age"] = 20
# print(id(data_dict_1))

# def login_front():
#     username = "admin"
#     password = "123456"
#     code = "8888"
#     print(f"用户名为：{username},密码为：{password},验证码为：{code}")
# login_front()
#
# def login_back():
#     username = "admin"
#     password = "admin"
#     code = "9999"
#     print(f"用户名为：{username},密码为：{password},验证码为：{code}")
# login_back()

# def record_info(name,sex="man",address="北京"):
#     print(f"姓名：{name}，性别：{sex}，地址：{address}")
# record_info("张三")

# 需求：计算1~100所有数字的累加和，1 + 2 + 3 …… 100
# 要求：通过 for 循环配合 range() 方法实现
# def sum_num(number):
#     num = 0
#     for i in number:
#         num += i
#     return num
# print(sum_num(range(0,101)))

# 需求：封装一个函数，实现start~end(包含start、end)之间所有数的累加，返回累加的结果
# 1. start、end为形参，默认值分别为1和100
# 2. 返回累加的结果
# 3. 调用函数，传递参数，测试函数的调用情况
# def sum_numbers(start=1,end=100):
#     sum = 0
#     for i in range(start,end+1):
#         sum += i
#     return sum
# sunall = sum_numbers()
# print(sunall)

"""
1. 学生信息如下
user_list = [{'name': '张三', 'age': 18}, {'name': '李四', 'age': 19}]
2. 封装打印学生信息的函数show_stu_info， 格式要求如下图：
	-----学生列表信息-----
    1 张三 18
    2 李四 19
    ----------------------
3. 调用函数，验证结果
"""
# user_list = [{'name': '张三', 'age': 18}, {'name': '李四', 'age': 19}]
# def show_stu_info():
#     print("-----------学生信息-------------")
#     n = 1
#     for i in user_list:
#         print(f"{n}\t\t{i['name']}\t\t{i['age']}")
#         n += 1
#     print("--------------------------------")
# show_stu_info()

"""
类名：Cat
属性：name
方法：
    __init__(): 添加属性，属性内容为'猫'
    eat(): 打印xx爱吃鱼， xx替换为具体的属性

# 1. 按要求设计类
# 2. 实例化对象，调用方法，验证结果
"""
# class Cat:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('%s 爱吃鱼'%self.name)
# c = Cat('猫')
# c.eat()

# # 创建动物类
# class Animals:
#     # 构建方法
#     def __init__(self):
#         print("我是动物类")
# # 猫类的实例
# catAnimals1 = Animals()
# catAnimals1.name_1 = "猫"
# catAnimals1.eat_1 = "爱吃鱼"
# print(catAnimals1.name_1 + catAnimals1.eat_1)