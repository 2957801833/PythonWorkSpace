# 1. 定义函数 login_front 实现前台系统登录
# front 前
def login_front():
    username="13800000001"
    password="123456"
    print(f"用户名是{username} 密码是{password}")
# 2. 定义函数 login_back 实现后台登录
def login_back():
    username="admin"
    password="admin"
    print(f"用户名是{username} 密码是{password}")
# 3. 要求使用同样的变量名, 分别记录前后台登录信息中的账号和密码
login_front()
login_back()