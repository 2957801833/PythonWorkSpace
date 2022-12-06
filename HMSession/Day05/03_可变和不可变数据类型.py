"""
不可变类型：  是内存中的数据不可变
    int,float,bool,str,tuple
可变类型：   是内存中的数据可以改变
    dict,list
"""
a = 1
print( id(a) )
a = 2
print( id(a) )
# 问题1：  第一个打印 和 第二个打印地址 A一样  B不一样
# B
print(30*"~")
data_dict = {"name":"如花"}
print( id(data_dict) )
#新增数据
# 字典变量名["key"] = value
data_dict["age"]=20
print( id(data_dict) )
# 问题2： data_dict 第一个打印 和 第二个打印地址
# A一样  B不一样
# A