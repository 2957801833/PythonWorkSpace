"""
必须把 变量[属性] 和 函数[方法] 写在类里

类的三要素
类名： Person
属性： name,weight
方法： run(),eat(n=1)
"""
# 1. 定义类
class Person:
    # 初始化方法。只要创建对象就会自动执行 init方法
    def __init__(self,name,weight=0):
        # self.属性名=数据值  一般形参名和属性名一致
        self.name=name
        self.weight=weight
    def run(self):
        #修改属性值  self.属性名=新值
        self.weight -= 0.5
    def eat(self,n=1):
        # 小括号优先级最高
        self.weight += (1*n)
    def __str__(self):
        return f"{self.name}的体重是{self.weight}"
# 2. 创建对象
# 对象变量名 = 类名()
xiaoming = Person("小明",weight=75)
#调用对象方法  对象变量名.方法名()
xiaoming.eat(2)   # 75 + 2
# 对象变量名.属性名
print(xiaoming.weight)
# 跑步
xiaoming.run()   # 76.5
# 打印对象 会调用 str方法
# 想方便查看信息可以实现str方法
print(xiaoming)

