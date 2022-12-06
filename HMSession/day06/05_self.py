"""
1. 定义类
    方法
    属性
2. 创建对象
"""
# 1. 定义类
class Cat():
    # self 是 哪个对象变量名调用了这个方法 self就是谁
    def eat(self,food="鱼"):
        # self=tom
        # tom.name = self.name
        print(f" {self.name} 在吃{food}")
    def sleep(self):
        print("睡觉")
# 2. 创建对象
tom = Cat()  # 对象变量名=类名()
# 如果给对象添加属性呢？？
# 在类的外部，可以通过 对象变量名.属性=值 来添加属性
# 这样添加的属性，只是给这个对象添加了 其他对象没有这个属性
# 这种方式 主要是为了讲一下 self  不推荐这样写
tom.name = "汤姆"
tom.eat()  # 调用方法
#创建另外一个对象，直接调用这个对象的eat方法
rose = Cat()
rose.eat()
