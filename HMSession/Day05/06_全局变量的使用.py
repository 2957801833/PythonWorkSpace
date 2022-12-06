# 全局变量
num = 10
# 定义
def demo1():
    print(num)   # ① 在函数内部可以使用 全局变量
def demo2():
    # ②在函数内部 定义一个 和全局变量一样名字的局部变量
    # 优先使用 局部变量  # 就近原则
    # ③ 我其实是想 修改全局变量 怎么办？？？
    # 通过 变量名 = 新值 前 声明一下就可以
    # global 全局
    global num
    num = 666
    print(num)
if __name__ == '__main__':
    demo2()
    print(num)
