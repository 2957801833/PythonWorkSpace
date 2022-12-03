"""
return  就是函数返回值
我们在调用函数的地方 需要 使用到 函数内部的数据，就需要借助于 return 实现
return 数据
"""
# 1.获取2个数的最大值
def get_2_max(num1,num2):
    if num1 >= num2:
        # 外边要用到最大值 就要使用 return
        return num1
    else:
        return num2
    # 一旦执行了return之后，函数内部的其他代码就不再执行了
    print("ooooooo")
# 2.对这个最大值再乘以一个10
n = get_2_max(9,4)

print( n * 10 )