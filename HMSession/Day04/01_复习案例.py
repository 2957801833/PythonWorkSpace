# 其他语言里 列表 叫做 数组 C
# 列表 嵌套 列表
data_list = [
    [  "13800000001","123456","8888" ],
    [ "1380000000","123456","8888"],
    [ "13800000001","123456a","8888"]
]
# [  [],[],[] ]
# 以一定的格式输出 ： 用户名是：xx 密码是：xxx 验证码是:xxx
# 格式化  f"{变量名}"             1
# 遍历 for 临时变量 in 容器         2
# 获取列表的指定数据  列表变量名[索引] 3
for item in data_list:
    # item 临时变量
    # print(item)
    print(  f" 用户名是：{item[0]} 密码是：{item[1]} 验证码是:{item[2]} " )


# 字典数据  {key不能重复}  [{},{},{}]
# 必用的东西
data_dict = [
    {"name":"13800000001","password":"123456","code":"8888"},
    {"name":"1380000000","password":"123456","code":"8888"},
    {"name":"13800000001","password":"123456a","code":"8888"}
]
print(20*"~")
# {"name":"13800000001","password":"123456","code":"8888"}
# 以一定的格式输出 ： 用户名是：xx 密码是：xxx 验证码是:xxx
# for 临时变量 in 容器：
# 获取字典的指定数据：  字典是根据key来获取value的   字典变量名.get("key")  字典变量名["key"]
for item in data_dict:
    # item 是字典
    # print(item)
    # 引号 嵌套的问题
    print( f"用户名是：{item.get('name')} 密码是：{item['password']} 验证码是:{item.get('code')}" )