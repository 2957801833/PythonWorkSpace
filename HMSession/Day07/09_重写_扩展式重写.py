"""
重写： 当父类的方法不能满足子类需要的时候
重写： 覆盖式重写和扩展式重写

我们以后经常接触的就是 扩展式重写
扩展式重写一般是在 初始化方法 里使用到
"""
# 1. 动物类
class Animal(object):
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("sleep")
# 2. 人类 继承自 动物
# 属性： 不仅仅有名字，还有年龄
class Person(Animal):
    # 也是写和父类一样的方法名
    def __init__(self,name,age):
        # 父类 animal 已经把初始化的 name设置好了
        # 所以 我们一般不采用 覆盖式重写
        # 而是 采用扩展式重写
        # 一般扩展式重写的代码 是在方法的最上边
        # super() 可以理解为 父类
        super().__init__(name)
        # 或者
        # super(Person, self).__init__(name)
        # 再写其他的代码
        self.age=age
    # 打印对象的时候  是地址信息，所以实现 str方法
    def __str__(self):
        return f"{self.name} {self.age}"
# 创建对象
zhangsan = Person("张三",20)
print(zhangsan)