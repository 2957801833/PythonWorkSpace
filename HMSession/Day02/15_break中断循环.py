"""
break 是中断 停止的意思
我们可以针对于 循环过程中的情况 停止循环

① 先实现 循环5次的代码
② 根据情况 吃完第三个苹果 停止循环
"""
# 1. 初始化一个计时器
n = 1
# 2. 进行while 循环判断
while n<=5:
    print("我吃的第 {} 个苹果".format(n))
    # 根据 条件 判断 是否停止循环
    if n == 3:
        break
    # break 是python关键字
    # 3. 修改计时器
    n = n + 1
print("富婆 60岁的富婆 和我说分手")