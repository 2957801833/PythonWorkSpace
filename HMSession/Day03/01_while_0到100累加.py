"""
使用while循环实现计算0~100所有数字的累加和结果
1. while 循环 实现 0~100的数字展示
2. 实现累加

变量： 存储计算的结果
result 结果的意思
# 存储的结果
result = 0

result = 0  + result             result = 0
result = 1  + result             result = 1
result = 2  + result             result = 3
result = 3  + result             result = 6
result = 4  + result             result = 10
result = 5  + result             result = 15

"""
# while 三部曲
# 4. 定义一个变量来存储结果 [初始化一个变量]
result = 0
# 1. 计数器
n = 0
# 2. while 条件判断
while n<=100:
    # print(n)
    # 5. 累加
    result = result + n
    # 3. 在while循环里修改计时器
    n = n + 1

print(result)