# 函数
"""
把具有独立功能的代码块组织为一个小模块，在需要的时候进行调用
使用步骤：1、定义函数-封装独立的功能
        2、调用函数-享受封装的成果
        作用：对具备相同逻辑的代码进行封装，提高代码的编写效率，实现对代码的重用
"""
from unittest import result

from HMSession.Day04 import common

# 定义函数
"""
语法格式：def函数名():
            函数封装代码
            ......
    说明：
        1、def是英文define的缩写
        2、函数名最好能够表达函数内部封装的代码的功能，方便后续的获取调用（见名知义）
        3、函数名命名遵循标识符命名规则：字母、数字、下划线，不能以数字开头，不能使用系统关键字
"""
# def sum_data():
#     a = 1
#     b = 2
#     result = a + b
#     print(result)

# 调用函数
"""
语法格式：函数名()
    说明：1、只定义函数，不调用函数，函数永远不会被执行
         2、不能将函数调用放在函数定义的上方，否则报错
"""

# 案例
"""
需求：
1. 编写一个打招呼 say_hello 的函数，封装三行打招呼的代码
2. 在函数下方调用打招呼的代码
"""
# def say_hello():
#     print("Hello")
#     print("Hello")
#     print("Hello")
# say_hello()

"""
函数定义语法格式：def函数名(形参1，形参2，。。。):
            函数封装代码
            ......
函数调用语法格式：函数名(实参1，实参2，。。。)
"""
# def get_2_sum(x,y):
#     print(x+y)
# # get_2_sum(2,2)
# # get_2_sum(2,y=2)
# get_2_sum(x=2,y=2)
#
# def get_money():
#     # print("借15k")
#     return float(input("请输入金额"))
# m = get_money()
# print(m,m-1)
#
# def get2_max(num1,num2):
#     if num1 >= num2:
#         return num1
#     else:
#         return num2
# # n = get2_max(6,8)
# n = get2_max(int(input("请输入数字：")) , int(input("请输入数字：")))
# print(n * 10)

# def demo1():
#     print("aaaa")
#
# def demo2():
#     print("---------------start-----------------")
#     demo1()
#     print("bbbb")
#     print("----------------end-----------------")
# demo2()


# def username_input():
#     name = input("请输入用户名：")
#     return name
# def password_input():
#     pwd = input("请输入密码：")
#     return pwd
# def login():
#     usename = username_input()
#     password = password_input()
#     if usename == "admin" and password == "123456":
#         print("登录成功！")
#     else:
#         print("登陆失败!")
# login()

# import  random
# random.randint(1,10)
#
# import  common
# result = common.get_2_sum(1,1)
# print(result)
# print(common.num)

# from common import get_2_sum
# r = get_2_sum(2,2)
# print(r)
#
# from common import get_2_sum as aaa
# print(aaa(1,3))

# print(__name__)
# if True:
#     print("aaaa")
# if __name__ == "__main__":
#     print("入口")

# info_list = [{'name': 'mike', 'pwd': '123321'}, {'name': 'rock', 'pwd': 'abccba'}, {'name':'tom', 'pwd':'h321'}]
# 遍历列表，打印信息，打印格式如下：
# 用户名为：mike, 密码为：123321
# 用户名为：rock, 密码为：abccba
# 用户名为：tom, 密码为：h321
# info_list = [
#     {'name': 'mike', 'pwd': '123321'},
#     {'name': 'rock', 'pwd': 'abccba'},
#     {'name':'tom', 'pwd':'h321'}
# ]
# for item in info_list:
#     print(f"用户名为：{item['name']},密码为：{item['pwd']}")

# 需求：封装一个函数，统计形参str_data中有几个空格' '
# 1. 统计的空格数需要返回
# 2. 调用函数，测试函数的调用情况
# def sapce_data(str_data):
#     i = 0
#     for n in str_data:
#         if str(n) == " ":
#             i += 1
#             print(i)
#     return str_data
# print(sapce_data("a   b  ssg gss     s"))

# 需求：封装一个函数，判断year是不是润年
# 1. year是形参
# 2. 闰年判断程序(闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)
# 3. 如果是闰年返回True，如果不是返回False
# 4. 调用函数，测试函数的调用情况
# def year_runnian(year):
#     if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
#         return True
#     else:
#         return  False
# print(year_runnian(2001))

# 需求:
# 1. 定义一个函数 sum_numbers， 可以接收的 任意多个整数
# 2. 功能要求： 将传递的 所有数字累加 并且返回累加结果
# *args可以接受任意多的参数，并将其打包为一个元组传入函数内部进行计算
# def sum_numbers(*args):
#     # 定义变量num用于存放求和结果
#     num = 0
#     # args是一个元组，那就可以通过循环的方式遍历其中的每一个元素，
#     # 通过将每个元素与上一步得到的sum_相加就可以得到所有参数的求和结果
#     for i in args:
#         num += i
#     return num
# print(sum_numbers(1,22,2))