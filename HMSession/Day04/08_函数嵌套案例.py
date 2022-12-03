# 1. 定义名为 input_username 的函数, 获取用户输入的用户名
def input_username():
    # 字符串变量名=input(提示信息)
    name = input("请输入用户名:")
    # name 只能在这个函数内部使用，其他地方用不了
    return name
# 2. 定义名为 input_password 的函数, 获取用户输入的密码
def input_password():
    pwd = input("请输入密码:")
    return pwd
# 3. 定义名为 login 的函数, 判断获取的用户名和密码信息
def login():
    # 调用 第一个 函数 获取用户名
    username = input_username()
    # 调用 第二个 函数 获取密码
    password = input_password()
    print(username,password)
    if username == "admin" and password == "123456":
        print("登录成功")
    else:
        print("登录失败")
# 4. 要求当获取的用户名为:admin 并且密码为: 123456 时, 输出“登录成功!”，否则提示“用户名或
# 密码错误!”
login()