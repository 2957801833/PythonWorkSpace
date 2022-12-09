"""
面向对象的三个特征： 封装，继承和多态

继承： 进而可以避免反复编写相同逻辑的代码

语法：
class 子类(父类):
    pass
"""
# 我们所有的类的祖宗 就是 object
# 所有类都是 继承自 object 来的
# 动物类   父类      基类
# class Animal:
class Animal(object):
    def eat(self):
        print("吃")
    def sleep(self):
        print("睡")
# 使用继承必须这么写
# 狗类 继承自动物类   子类
class Dog(Animal):
    #子类继承了父类的所有属性和方法
    #子类还可以有自己特有的属性和方法
    def bark(self):
        print("叫")
class XiaoTianDog(Dog):
    def fly(self):
        print("飞")
##############################################
# 对象变量名 = 类名()
xtq = XiaoTianDog()
xtq.fly()
xtq.bark()
xtq.eat()
xtq.sleep()
print(20*"*")
# 猫类  继承自 动物类
class Cat(Animal):
    def catch(self):
        print("抓老鼠")
# 创建对象
tom = Cat()
tom.catch()
tom.eat()
tom.sleep()