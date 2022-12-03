# 1. 提示用户输入登录系统的用户名和密码
# 2. 校验用户名和密码是否正确（正确的用户名：admin、密码：123456）
# 3. 如果用户名和密码都正确，打印“登录成功！”，并结束程序
# 4. 如果用户名或密码错误，打印“用户名或密码错误！”，提示用户继续输入用户名和密码登录
# 5. 如果用户输入的用户名为“exit”，则退出程序

# while 可以实现死循环     for in 不容易出现死循环
while True:
    # pass 占位 不报语法错误
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "admin" and password == "123456":
        print("正确")
        break
    elif username == "exit":
        print("退出")
        break
    else:
        print("错误")