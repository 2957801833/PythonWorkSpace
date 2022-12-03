"""
死循环： 就是一直在运行循环里的代码
while True:
    print("死循环")

while 循环 三部曲

1. 定义一个计数器
2. 进行while 条件判断
3. 修改计数器
"""
n = 1
while n<=100:
    print(f"我错了 {n}")
# 修改计数器 没有缩进
# 没有缩进就和 while没有关系
n = n + 1
print("over")
