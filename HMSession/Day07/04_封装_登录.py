"""
面向对象的3个特征： 封装、继承和多态
封装： 把属性和方法写在类里
类名： LoginPage
属性： username,password,code
方法： login(), init()
"""
# 1. 定义类
# class LoginPage: 最经常写的
class LoginPage():      #认识
    def __init__(self,username,password,code="8888"):
        self.username=username
        self.password=password
        self.code=code
    # 模拟登录
    def login(self):
        # 在自己类的内部使用属性： self.属性名
        print("用户名是{}".format(self.username))
        print(f"密码是{self.password}")
        print("验证码是",self.code)
# 2. 创建对象
# 对象变量名 = 类名() ① 类名后边必须跟小括号 ② 小括号的参数 参照init方法参数[self不算]
tpshop = LoginPage("13800000002","123456")
# 调用方法
tpshop.login()