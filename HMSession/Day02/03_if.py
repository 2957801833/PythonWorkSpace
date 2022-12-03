"""
if 语法
if 条件判断：
    条件判断为真，执行的代码1
    代码2
    代码3
"""


#   案例
#   1、定义一个年龄变量
# age = eval(input("请输入你的年龄："))
# #   2、判断年龄是否大于18岁，如果大于18岁，则可以去网吧
# if age>=18 :
#     print('年龄大于18岁，可以去网吧')
# else:
#     print('未成年，赶紧回家！')

# age = eval(input("请输入你的年龄："))
# if age>=0 and age<=150 :
#     print('年龄正常')
# else:
#     print('老实交代，你是什么人！')

# employee =False
# if not employee:
#     print('')


# import random
# p1 = eval(input("请输入：1-石头，2-剪刀，3-布："))
# # c1 = eval(input("请输入：1-石头，2-剪刀，3-布："))
# c1 = random.randint(1,3)
# print(c1)
# if p1 == c1:
#     print('平局')
# elif (p1 == 1 and c1 == 2) or (p1 == 2 and c1 == 3) or (p1 == 3 and c1 == 1) :
#     print('恭喜，你赢了！')
# else:
#     print('很遗憾，你输了！')

# n = 0
# while n < 100:
#     n += 1
#     # print(f"赶紧回教室{n}")
#     print("赶紧回教室")

# name = "itcast"
# for item in name:
#     print(item)
#     # if  item == 's':
#     #     break

# for a in range(1,11):
#     print("aaa{}".format(a))

"""
需求:
提示用户输入登录系统的用户名和密码
校验用户名和密码是否正确 (正确的用户名: admin、密码: 123456)
如果用户名和密码都正确，打印“登录成功!”，并结束程序
如果用户名或密码错误，打印“用户名或密码错误!”，提示用户继续输入用户名和密码登录
如果用户输入的用户名为“exit”，则退出程序
"""
# while True:
#     name = input("请输入用户名或输入exit退出:")
#     if name == "exit":
#         break
#     pwd = input("请输入密码：")
#     if name == "admin" and pwd == "123456":
#         print("登陆成功")
#         break
#     else:
#         print("用户名或密码错误，请继续输入")

# 1. 闰年判断程序(闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)
# 2. 输入一个有效的年份，判断是不是闰年
# 3. 如果是闰年，则打印“xxxx年是闰年”；否则打印“xxxx年不是闰年”
#	如输入"2018"，将打印“2018年不是闰年”
# year = input("请输入年份：")
# if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")

# 1. 输入用户名
# 2. 验证用户名为 tom 以后, 再获取用户输入的年龄，如果不是tom，输出：输入用户名有误！
# 3. 如果年龄不满30岁，输出：tom为小鲜肉，如果满30岁，输出：tom为老腊肉
# while   True:
#     name = input("请输入用户名：")
#     if name != "tom":
#         print("输入用户名有误！")
#     age = input("请输入年龄：")
#     if  int(age) <30 :
#         print("tom为小鲜肉！")
#         break
#     else:
#         print("tom为老腊肉！")
#         break

# 猜数字游戏：电脑产生（1-100）的随机数，用户进行猜测，直到猜中为止
# 1. 电脑产生（1-100）的随机数
# 2. 死循环
# 3. 用户输入猜的数字
# 4. 如果猜中，输出：恭喜你猜中了，数字是 xx。退出循环
# 5. 如果猜的数字大，输出：猜测的数字太大了，继续加油
# 6. 如果猜测的数字小，输出：猜测的数字有点小，再来一次
# import random
# while True:
#     computer = random.randint(1,111)
#     person = input("请输入数字：")
#     if computer == int(person):
#         print("恭喜你猜中了,数字是{}".format(computer))
#         break
#     elif int(person) > int(computer):
#         print("猜测的数字太大了，继续加油,数字是{}".format(computer))
#     else:
#         print("猜测的数字有点小，再来一次,数字是{}".format(computer))

"""
说明: 在列表的末尾添加数据
语法: 列表.append(新增数据)
注意:
1. 方法执行是对原数据进行的修改, 故而需要打印查看原数据
2. 如果新增数据是一个容器类型(例如: 列表)数据, 则会将数据整体作为一个元素添加至末尾

#  需求1：["Web自动化", "UI自动化", "接口自动化"] 添加 "APP自动化"
# 需求2：["Web自动化", "UI自动化", "接口自动化"] 添加 [1, 2, 3]
"""
# a_list = ["Web自动化", "UI自动化", "接口自动化"]
# a_list.append("APP自动化")
# b_list = ["Web自动化", "UI自动化", "接口自动化"]
# b_list.append("1")
# b_list.append("2")
# b_list.append("3")
# print(a_list,b_list)



