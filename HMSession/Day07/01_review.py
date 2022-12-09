
# 1. 定义一个类
class Person:
    def __init__(self,name):
        self.name = name
    def eat(self,food="食物"):
        # self.name 是属性
        # food 是参数
        print(f"{self.name}在吃 {food}")
    # 针对于测试使用的确实少，开发用的多，主要是调试 分析
    def __str__(self):
        return self.name
# 2. 创建2个对象
zhangsan = Person('张三')
lisi = Person(name='李四')
# 如果你写的代码很多，或者这个类是别人定义的
print(zhangsan,lisi)