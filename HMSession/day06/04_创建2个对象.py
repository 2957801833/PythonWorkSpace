"""
类的设计三要素
类名： Cat
属性： 暂无
方法： eat(), sleep()
1. 定义类
2. 创建对象
"""
# 1. 定义类
class Cat:
# class Cat():   #使用比较少
# class Cat(object):  # 明天会重点讲解，这种是继承的写法
    # 方法  和 函数一样。方法的第一个参数要求是self
    def eat(self,food="鱼"):
        print(f"在吃 {food}")
    def sleep(self):
        print("睡觉")
# 2. 创建对象
# 对象变量名 = 类名()
tom = Cat()
# 在类的外边调用方法
# 对象变量名.方法名()
tom.eat()
tom.sleep()
#如何创建第二个对象呢？ 其他就是再写一遍 对象创建的代码
rose = Cat()
rose.sleep()
# tom 和rose是不同的对象
print(  id(tom), id(rose) )