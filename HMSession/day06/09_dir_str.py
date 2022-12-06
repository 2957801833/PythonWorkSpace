# 1. 定义一个类
class Person:
    def __init__(self,name):
        #self.属性名=数据值
        self.name=name
    def eat(self):
        print(f"{self.name}在吃饭")
    # 可以通过 实现 __str__ 方法
    # 这个方法可以控制 控制台打印的信息
    # 这个方法 必须返回一个 字符串
    def __str__(self):
        return f"{self.name}"
# 2. 创建对象
zhangsan=Person("张三")
lisi = Person(name="李四")
print( zhangsan,lisi )
print(20*"*")
# 我是怎么知道 类中有一个 __str__ 方法呢？
# dir(对象) 配合 print 方法 可以查看 这个对象内部的方法 [了解] 给开发看的
print(  dir(zhangsan) )