############切片#########################
# 切片： 就是获取  列表、元组、字符串中的指定 部分数据
str1 = 'abcedfg'
# 变量名[数值]
# 变量名[开始:结束]
# 变量名[开始:结束:步长]
# 步长： 默认是 1  间隔1个索引
# print(  str1[3]  )
# # 试一试
# print(  str1[2:4] )
#
# print( str1[0:7:2])
##############特殊的写法#########
# print( str1[2:] ) # 从第3个开始      到结束
# print( str1[:2])  # 从开始     到第2个
# print( str1[::-1] ) # 反转 reverse
###########len#########################
print(20*"~")
# length  长度   len
# 容器  字符串，列表，元组，字典 个数
# len(  列表/元组/字典/字符串  )
print(  len(  "abc"     )              )
print(  len( [ 1,2,3]   )             )
print(  len(  {"name":"itcast"}   )   )

