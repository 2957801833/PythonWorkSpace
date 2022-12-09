"""
类名： Food
属性： 名字
方法： 暂无
~~~~~~~~~~~~~~~~~~~~~~~~
类名： Person
属性： user
方法： eat(食物对象)
~~~~~~~~~~~~~~~~~~~~~~~
人 吃 食物
"""
# 1. 定义食物类
class Food:
    def __init__(self,name):
        self.name=name
# 2. 定义人类
class Person:
    def __init__(self,user):
        # 为了不和食物的名字闹混，改为user
        self.user=user
    def eat(self,fd):
        # fd 和 egg 是引用关系
        # fd = egg
        # egg.name
        # fd="鸡蛋"
        print(f"{self.user}在吃 {fd.name}")
# 3. 创建食物对象[鸡蛋，包子，面包]
egg = Food("鸡蛋")
baozi = Food("包子")
bread = Food("面包")
# 4. 创建人对象
xiaozhang = Person("小张")
# 5. 人吃东西
# egg 是一个对象变量
xiaozhang.eat(egg)
# 这么写不对
# xiaozhang.eat("鸡蛋")