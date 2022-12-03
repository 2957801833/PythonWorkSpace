"""
列表 = [元素1,元素2,...]
元组 = (元素1,元素2,...)
字典 = { key:value, name:"张三", }
"""
# dict 是字典
# ① 字典是使用 大括号
# ② 字典的数据是 键值对   key: value
# ③ key 是字符串  见名知意
# ④ :  有冒号
# ⑤ value 可以是任意数据类型
# 一个键值对 属于一个元素
# { key1:value1 , key2: value2 ,... }
# 字典的定义
data_dict = {  "name":"张三" , "age":20 ,"address":"北京"  }
print( type(data_dict) )
# 方式2 【了解】
data_dict_2 = dict()
# 空字典
# 等价于
data_dict_3 = {}
print( type(data_dict_2) )
######################字典获取指定数据##############################
print(20*"!")
data_dict_4 = {  "like":"60岁女朋友","age":20,"address":"北京" }
# 我们获取 字典的数据是 根据 key值 获取value值
# 语法： 字典变量名["key"]
# 不推荐  如果你的key写错了  系统就报错了
print(  data_dict_4['like']  )
# 推荐 第二种方式
# 语法： 字典变量名.get("key")
# print(  data_dict_4.get("address") )
# None  如果key值写错或者字典没有key 不会报错
print(  data_dict_4.get("addres") )

######################字典增加或修改数据##############################
print(20*"~")
# 字典的新增和修改语法是一样的： 字典变量名["key"] = value
# 如果字典中 不存在 key ，则是新增
# 如果字典中 存在 key ，则是修改
data_dict_5 = {"name":"itcast"}
# 新增字典数据：  字典变量名["key"] = value
data_dict_5["age"]=20
print(data_dict_5)
#修改字典数据： 字典变量名["key"] = value
data_dict_5["name"]="itheima"
print(data_dict_5)
######################字典删除数据##############################
print(20*"#")
data_dict_6 = {  "name":"张三","age":20 }
# 删除语法： 字典变量名.pop("key")
data_dict_6.pop("age")
print(data_dict_6)