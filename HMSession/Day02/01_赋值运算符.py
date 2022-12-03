'''
赋值运算符：  赋值 给值 =
变量语法：    变量名=数据值    含义：把数据值 赋值给 变量名
'''
'''
徐畅 15K 工作想借钱15K
我第一个月 借了徐畅 15K
我第二个月 借了徐畅 15K
我第三个月 借了徐畅 15K
'''
# # 钱 money
# # 变量
# # 开始没有借钱
# money = 0
# # 变量名=数据值
# #赋值运算符 先计算等号右边
# money = money + 15
# #money = 0+15
# print(money)
# money = money +15
# print(money)
# #money = money + 15 有简单书写形式     固定书写形式 +=
# money += 15
# print(money)







year = input("请输入年份：")
if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")