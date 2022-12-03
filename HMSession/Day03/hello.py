# 字典
# data_dictaaa = { "name": "张三", "age":33,"height": 188}
# print(type(data_dictaaa))
# print(data_dictaaa["name"])
# print(data_dictaaa.get("height"))
# 添加键值对
# data_dictaaa["weight"] =200
# print(data_dictaaa)
# 删除键值对
# data_dictaaa.pop("age")
# print(data_dictaaa)
# 遍历key
# for key in data_dictaaa.keys():
#     print(key)
# 遍历 value
# for value in data_dictaaa.values():
#     print(value)
# print(data_dictaaa.values())
# 循环拿到每个键和值
# for k,v in data_dictaaa.items():
#     print(f"key={k},value={v}")


# 切片
# name = "abcdefg"
# print(name[0:3]) #abc
# print(name[3:6:2]) #df
# print(name[:]) #abcdefg
# print(name[-1:]) #g
# print(name[::-1]) #gfedcba
# name_list = [1,2,3,4,5,6,7,8,9]
# print(name_list[::]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# name_tuple = (1,2,3,4,5,6,7,8,9)
# print(name_tuple[0:6:2]) #(1, 3, 5)

# 获取元素个数
# str_data = "hello world"
# print(len(str_data)) #11 包含空格
# list_data = ["hello world","ocean"]
# print(len(list_data)) #2 列表中元素个数
# tuple_data = ("tuple",3,4,5,"sea",7,8,9)
# print(len(tuple_data)) #8 元组内元素个数
# dict_data ={
#     "name": "abcdefg",
#     "age": 33
# }
# print(len(dict_data)) #2 字典内键值对个数

# my_list = ["hello", "python", "hello", "itcast", "hello"]
# ① 增: 列表末尾增加"heima",
# ② 删: 删除上一步增加的元素'heima'
# ③ 改: 修改列表中最后一个数据为"chuanzhi"
# ④ 查: 1) 取出'python'，再打印 2) 统计'hello'有多少个 3) 统计列表元素个数
# my_list = ["hello", "python", "hello", "itcast", "hello"]
# my_list.append("heima")
# print(my_list)
# my_list.pop(5)
# print(my_list)
# my_list[4] = "chuanzhi"
# print(my_list)
# print(my_list[1])
# print(my_list.count("hello"))
# print(len(my_list))


# info = {'name':'mike', 'age':35, 'city':'sz'}
# ① 增: 字典增加'sex':'man'
# ② 删: 删除上一步增加的元素
# ③ 改: 把年龄修改为18
# # ④ 查: 取出姓名，再打印
# info = {'name':'mike', 'age':35, 'city':'sz'}
# info["sex"] = "man"
# print(info)
# info.pop("sex")
# print(info)
# info.update({"sex": 18})
# print(info)
# for k,v in info.items():
#     print(k,v)

# for 循环计算字符串 'a-bc-12----3' 中有多少个字符'-'
#1. 定义变量 来统计 - 的数据
#2. 循环遍历
#3. 什么情况 计数+1
# str_data = 'a-bc-12----3'
# # print(str_data.count('-'))
# i = 0
# for n in str_data:
#     if n == "-":
#         i += 1
#     print(i)

# 需求：封装一个函数，实现2数相加
# 1. 这两个数字，需要作为参数传递过来
# 2. 需要将相加结果返回
# 3. 调用函数，测试函数的调用情况
# def count_test():
#     num1 = 1
#     num2 = 2
#     result = num1 + num2
#     print(f"{num1}+{num2}={result}")
# count_test()
# def count_test2(num3,num4):
#     result2 = num3 + num4
#     print(result2)
# count_test2(4,1)



# # 表 嵌套 列表
# data_list = [
#     ["133 1111 2222","123456","8888"],
#     ["133 1111 2223","123456","8888"],
#     ["133 1111 2222","123456a","8888"]
# ]
# # 以一定的格式输出 : 用户名是: XX 密码是: XXX 验证码是:xxx
# # 格式化 f{变量名}"
# # 遍历 for 临时变 in 容器
# # 获取列表的指定数 列表变量名[ 索引]
# for item in data_list:
#     print(f"用户名：{item[0]},密码：{item[1]},验证码：{item[2]}")

# 字典数据 {key不能重复} [{}，{}，{}]
data_dict = [
    {"name":"133 1111 2222","password":"123456","code":"8888"},
    {"name":"133 1111 2221","password":"123456","code":"8888"},
    {"name":"133 1111 2222","password":"123456a","code":"8888"}
]
# 以一定的格式输出 : 用户名是: XX 码是:Xxx 验证码是:xxx
# for 临时交量 in 容器:
# 获取字典的指定数据: 字典是根据key来获取value的 获取方式：字典变量名.get(key)
for item in data_dict:
    print(f"用户名：{item.get('name')},密码：{item.get('password')},验证码：{item.get('code')}")