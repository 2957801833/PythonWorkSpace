"""
1.  数据类型[int,float,boolean,None,str,list,tuple,dict]
2. 根据变量在内存 可变 和不可变 来划分 【可变数据类型 和 不可变数据数据类型】

3. 根据变量是否在函数内部 来划分
    在函数内部定义的变量，只能在函数内部使用，我们称之为 局部变量
    在函数外部定义的变量，我们称之为 全局变量
"""
# 全局变量
# 先定义变量，再使用变量
name = "法外之徒--张三"
# 定义一个函数
def demo():
    print("函数内部")
    # num 是局部变量 只能在函数内部使用
    num = 15
    print(num)
    # 函数内部 可以使用全局变量
    print(name)
# 调用
demo()
# print(num)
# print(name)