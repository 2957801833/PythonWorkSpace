"""
列表 -- 增删改查
[]
list()
元组：   元组是不可以修改的列表

"""
# str       字符串
# list     列表
# tuple   元组
# 元组定义方式1 【最常用】
data_tuple = (15,15,15)
print( data_tuple, type(data_tuple) )
# 方式2 【了解】
# 空元组
data_tuple_2 = tuple()
# data_tuple_2 是空元组和 下边定义等价
data_tuple_3 = ()
print( data_tuple_2,data_tuple_3 )
# 注意事项：  如果元组中有一个数据，必须 必须  在这个数据的后边添加逗号
data_tuple_4 = ("张三",)
data = ("张三")   # 如果一个数据，没有添加逗号，系统就认为是一个 小括号优先级
print(  type(data_tuple_4),type(data) )
# 因为 元组 就是 不能修改的列表  所以 获取元组的方式和列表一致
# 变量名[索引]
data_tuple_5 = ("张三","李四","王五")
print(  data_tuple_5[1] )