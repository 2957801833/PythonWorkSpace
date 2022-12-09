"""
多态： 不同的子类调用相同的父类方法，提现的结果不一样
多态的前提： 继承和重写

1. 在 Dog 类中封装方法 game
– 普通狗只是简单的玩耍
2. 定义 XiaoTianDog 继承自 Dog，并且重写 game 方法
– 哮天犬需要在天上玩耍
3. 定义 Person 类，并且封装一个 和狗玩 的方法
– 在方法内部，直接让 狗对象 调用 game 方法
"""
# 1. 定义一个Dog类
class Dog(object):
    def game(self):
        print("凡间单身狗 陪你玩")
# 2. 定义一个XiaoTianDog 类 继承 Dog
class XiaoTianDog(Dog):
    def game(self):
        print("天上的狗狗 带你装逼带你飞")
# 3. 定义一个 Person类
class Person:
    def play(self,d):
        #d.game()  d 形参   d = tianyaun / xtq
        d.game()
if __name__ == '__main__':
    # 4. 创建一个普通的dog对象
    tianyuan = Dog()
    # 5. 创建一个哮天犬对象
    xtq = XiaoTianDog()
    # 6. 创建一个 Person对象
    zhangsan = Person()
    # 7. 让Person对象和谁玩
    zhangsan.play(tianyuan)