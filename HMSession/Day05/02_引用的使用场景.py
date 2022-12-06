# 在Python中, 函数的 参数 和 返回值 传递都是引用信息
# 记住结论
# 我们通过代码来验证结论
# 形参和实参 是 引用    形参和实参 指向同一个地址
# 变量名 = 函数名()   函数内部的return 地址 和 变量名的地址是同一个地址

# 1. 定义一个函数
# 返回2个数的和
def get_2_sum(num1,num2):
    # print( id(num1) )
    result = num1 + num2
    print(  id(result) )
    return result
# 2. 调用函数
x = 10
y = 20
# print( id(x) )
r = get_2_sum(x,y)
print( id(r) )
print(r)
# 验证的第一个问题是：  x的地址 和  num1的地址应该是一样的
# 验证的第二个问题是：  result的地址 和  r的地址应该是一样的
