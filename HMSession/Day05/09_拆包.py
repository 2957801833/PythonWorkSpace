"""
把刚才的多值参数代码再重新写一遍
"""
# 1. 定义函数
def get_sum(*args):
    # ① 定义一个变量 统计总和
    result = 0
    # ② 对 args进行遍历
    for i in args:
        # ③ 累加
        result += i   #  result = result + i
    #④ 返回
    return result
# 2. 调用函数
r = get_sum(1,2,3,4,5)
# 3. 模拟 我们从数据库中 查询数据出来 # select * from xxx;
# 结果查询的数据是一个元组
data = (1,2,3,4,5)
# 怎么办？ 拆包   *()   就把元组拆开了
r2 = get_sum(  *data  )
print(r2)