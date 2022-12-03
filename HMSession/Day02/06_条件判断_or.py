"""
or 就是或者的意思

if 条件判断1 or 条件判断2 [or 条件判断3]:
    有一个条件成立[True] 则执行代码
条件判断1 or 条件判断2
1. 只要有一个条件判断成立[True]  整体 条件判断 就是成立的
2. 只有都不成立， 整体条件判断 才是假[False]
3. or 两边要有空格
"""
# 1. 定义两个整数变量python_score、c_score，编写代码判断成绩
# score 分数
python_score = 80
c_score = 50
# 2. 要求只要有一门成绩 > 60 分就算合格
if python_score > 60 or c_score > 60:
    print("合格")