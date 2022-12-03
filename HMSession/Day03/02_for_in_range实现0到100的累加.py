"""
使用for in range循环实现计算0~100所有数字的累加和结果
1. for in range 循环 实现 0~100的数字展示
2. 实现累加
"""

# 2.定义一个变量 来存储结果
result = 0
# 1. for in range 实现 0~100
# for item in range(循环次数) 默认是从0开始
# for item in range(开始，结束)
for item in range(101):
    # print(item)
    # 3. 累加
    result = result + item
    # 简写形式
    # result += item
print(result)