"""
重写： 父类的方法 不能满足子类的需要
重写： 覆盖式 和 扩展式
"""
# 1. 动物类
class Animal(object):
    def eat(self):
        print("吃东西")
    def sleep(self):
        print("睡觉")
# 2. 狗狗类
class Dog(Animal):
    def bark(self):
        print("叫")
# 3. 哮天犬
class XiaoTianDog(Dog):
    def fly(self):
        print("飞")
    # 覆盖式重写
    # 就是使用和父类一样的方法名，代码重新写
    def eat(self):
        print("我是天上的狗狗")
        print("我吃天上的狗粮")
# 哮天犬这个子类 针对于 父类的方法 不想用父类的方法了
xtq = XiaoTianDog()
xtq.eat()