"""
需求： 求 几个数的和
2   get_sum(num1,num2)
3   get_sum(n1,n2,n3)
5
9

args   arguments
如果对于我们传递的参数 不确定个数的情况下，可以采用 不定参数[多值参数]
*args 就表示 用于接收 不确定的哪些参数
args 是习惯的写法 表示 参数的意思
"""
def get_sum(num,*args):
    #使用的时候 就不要添加 * 号了 直接使用 args
    # print( args, type(args) )
    # args 接收到的是 元组
    # 思路？ (2,3,4,5)  遍历
    # 定义一个变量 来接收最终的 累加结果
    # 先把第一个值 相当于加起来了
    result = num
    # for in 遍历
    for item in args:
        # 累加
        result = result + item
    #return 在for循环外
    return result
# 调用
r = get_sum(1,2,3,4,5,10,100)
print(r)
