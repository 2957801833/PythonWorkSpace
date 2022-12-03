"""

函数： 实现了特定功能的代码 需要使用的时候 调用

def get_money():
    pass
获取到钱之后，后续 可以花
"""
# 1. 定义一个函数 借钱
def get_money():
    print("借给你15K")
    # 空头支票 只是在控制台打印 pint()
    # return 就是返回  函数执行到这里 会携带 return 后边的数据
    return 15
    # 如果没有写 return 相当于 return None
# 2. 调用函数 获取 钱
# 变量名 = 数据值
# m 存储 借到的钱
# = 先执行 右边
m = get_money()
# None 就是空 没有
print(m)
# 3. 花钱
print( m - 1 )