"""
for in 可以实现循环
语法：
for 临时变量 in 容器：
    循环代码1
    循环代码2
    ...
① for 是Python关键字。后边有空格
② 临时变量 起什么名字都可以 一般用 i,item【每一项】
③ in 是Python关键字。 两边有空格
④ 容器 今天就知道 字符串是容器就可以 后边会讲
容器：  字符串 "itcast"
for in 循环容器 理解为 获取容器中的每一个元素
i   t   c   a    s  t
循环遍历  获取容器中的每一个元素
"""
# 1. 定义字符串
name = "itcast"
# 2. 对字符串进行循环遍历
for item in name:
    print( item )
    # 当元素是a的时候 停止循环
    if item == 'a':
        break