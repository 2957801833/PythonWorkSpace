"""
data_dict = {
    "name":"张三",
    "age":20,
    "address":"北京"
}
"""
# 1.定义一个字典
data_dict = {
    "name":"张三",
    "age":20,
    "address":"北京"
}
# 2.只获取字典的value值
# 字典变量名.values()
# print(   data_dict.values()   )
# 3. 我们想 遍历 字典value的每一项
# 获取容器中的每一项 就是 遍历
for item in data_dict.values():
    print(item)
#############keys#################
print(20*"~")
for item in data_dict.keys():
    print(item)

################items#####################
print(20*"!!")
data_dict = {
    "name":"张三",
    "age":20,
    "address":"北京"
}
# 直接对字典进行遍历 会是什么样子
# 打印的都是key
# 我们期望的是 key value 一对
# for item in data_dict.items():
# for 临时变量key的意思,临时变量value的所以 in data_dict.items():
# for key,value in data_dict.items():
for k,v in data_dict.items():
    # ('name', '张三')
    # key,value = item
    # key,value = ('name', '张三')
    print(k,v)

