"""
类名： Cat
属性： name
方法： eat(),sleep()
1. 定义类
2. 创建对象
"""
# 1. 定义类
class Cat:
    #我们类中的属性一般是在 init方法中添加
    # 什么时候执行init方法？ 当创建对象的时候[ 类名后边写小括号 ] 就会调用
    def __init__(self):
        # 在类里边 通过  self.属性名=属性值
        self.name = "汤姆猫"
    def eat(self,food="鱼"):
        # 在类的里边，如果使用属性呢？？
        # self.属性名
        print(f" {self.name} 在吃{food}")
    def sleep(self):
        print("在睡觉")
# 2. 创建对象
tom=Cat()
# 在类的外边，如果使用属性呢？  对象变量名.属性名
print(tom.name)
# 在类外边，调用方法   对象变量名.方法名
tom.eat("猫粮")
print(20*"*")
rose = Cat()
# rose 的name使用了默认的 汤姆猫
# 我们在创建对象的时候，一般 属性值 都不一样
# 我们还得修改属性值
# 对象变量名.属性名 = 新值
rose.name = "肉丝"
rose.eat()