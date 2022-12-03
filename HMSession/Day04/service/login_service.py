while True:
    def login_data(username,password,code):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        code = input("请输入验证码：")
        if username == "admin" and password == "123456" and code == "8888":
            print("登录成功")
        elif username != "admin" and password == "123456" and code == "8888":
            print("用户名错误！")
        elif username == "admin" and password != "123456" and code == "8888":
            print("密码错误！")
        else:
            print("验证码错误！")