#初始化生日日期
day = 0

#提示用户回答第一个问题
question1 = "你的生日是在第一个表么？\n" + \
    "1 3 5 7\n" + \
    "9 11 13 15\n" + \
    "17 19 21 23\n" + \
    "25 27 29 31" + \
    "\n输入0为否1为是："
answer = eval(input(question1))
if answer == 1:
    day += 1

#提示用户回答第二个问题
question2 = "你的生日是在第二个表么？\n" + \
    "2 3 6 7\n" + \
    "10 11 14 15\n" + \
    "18 19 22 23\n" + \
    "26 27 30 31" + \
    "\n输入0为否1为是："
answer = eval(input(question2))
if answer == 1:
    day += 2

#提示用户回答第三个问题
question3 = "你的生日是在第三个表么？ \n" + \
    "4 5 6 7\n" + \
    "12 13 14 15\n" + \
    "18 19 22 23\n" + \
    "26 27 30 31" +\
    "\n输入0为否1为是："
answer = eval(input(question3))
if answer == 1:
    day += 4

#提示用户回答第四个问题
question4 = "你的生日是在第四个表么？ \n" + \
    "8 9 10 11\n" + \
    "12 13 14 15\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\n输入0为否1为是："
answer = eval(input(question4))
if answer == 1:
    day += 8

#提示用户回答第五个问题
question5 = "你的生日是在第五个表么？ \n" + \
    "16 17 18 19\n" + \
    "20 21 22 23\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\n输入0为否1为是："
answer = eval(input(question5))
if answer == 1:
    day += 16

#打印结果
print("\n你的生日是" + str(day) + "日")