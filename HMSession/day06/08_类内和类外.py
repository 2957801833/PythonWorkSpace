"""
class 类名:
    def __init__(self,形参1，形参2，...):
        self.属性名1 = 形参1
        self.属性名2 = 形参2
        ...
    def 方法1(self):
        在类的内部使用自己的属性
        ①语法： self.属性名
    def 方法2(self):
        在类的内部使用自己的方法
        ②语法： self.方法名()
对象变量名=类名()  （）的参数 查看init方法的参数
在类的外部使用自己的属性
③对象变量名.属性名
在类的外部使用自己的方法
④对象变量名.方法名()
"""
# 1. 定义一个人类
# 类名： Person
# 属性： name,age
# 方法： eat(),sleep(),all()
class Person:
    # 初始化方法[init]
    def __init__(self,name,age):
        # 一般我们在定义初始化方法的时候，属性名和形参名一致
        self.name = name
        self.age = age
    def eat(self):
        print( f"{self.name}在吃" )
    def sleep(self):
        print(f"{self.name} 在睡觉")
    def all(self):
        #一气呵成
        self.eat()
        self.sleep()
zhangsan = Person("张三",age=20) #创建对象
print(zhangsan.age)
zhangsan.all()