"""
使用 for in 循环10次 像 while 那样 怎么做？
for in range
语法：
for 临时变量 in range(循环次数):
    循环代码1
    循环代码2
"""
# for in range(循环次数)
# 是从0开始  到 循环次数-1
for item in range(10):
    print( "我错了 {} ".format(item) )

# 让字符串 重复 10次
print( 10 * "#" )
############################################
# range(开始，结束)  包含开始值，不包含结束值
for item in range(1,11):
    print("我错了 {} ".format(item))