
# 1. 定义类
class Cat:
    def __init__(self,username="汤姆猫"):
        # 类的内部 添加属性
        # self.属性名 = 数据值
        self.name = username
    def eat(self):
        print(f"{self.name} 在吃饭")
# 2. 创建对象
# 只要创建对象就要调用 init方法
tom = Cat()                 # 默认参数
tom.eat()
print(20*"*")
rose = Cat("肉丝")           #位置传参
rose.eat()
print(20*"~")
jack = Cat(username="杰克")  #关键字传参
jack.eat()