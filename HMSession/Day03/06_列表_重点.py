"""
列表 可以存储 很多的基本数据

"""
# 1. 列表的定义   [  数据，数据，数据 ]
# ① 中括号表示列表
# ② 数据和数据之间 一定要用 逗号分隔  【数据也可以称之为 元素】
# 变量名 = 数据
data_list = [  "张三","李四","王五" ]
print( type(data_list),data_list )
# 空列表
data_list_2 = []
# 列表定义方式二 【了解】
# 空列表  知道这种形式就可以 一般采用 上边的方法
data_list_3 = list()
print(  type(data_list_2),type(data_list_3) )
#####################获取列表中指定数据#######################
print(20*"!")
# 1. 定义一个列表
data_list_4 = ["张三",4,"王五",6]
# 2. 获取指定的数据
# 语法： 列表变量名[索引]     索引也可以称之为下标
# 索引是什么意思 索引 怎么来
# data_list_4[3]  获取的是  6  这个数据值
# 0  索引是从0开始
# ① 索引 不能超过 列表长度
# ② 索引支持负数 -1，-2 ，-3 【倒数第一个，倒数第二个...】
print(   data_list_4[3]  ,data_list_4[-4] )
#####################列表新增数据#######################
print(20*"@")
# 1. 定义一个空列表
data_list_5 = []
# 2. 新增数据
# 列表.append(数据)
# 列表的数据是有顺序的！！！！
# append 追加的意思  给列表后边顺序追加数据
data_list_5.append(1)
data_list_5.append("哦哦哦噢噢")
data_list_5.append([1,2,3,4])
print(data_list_5)
#####################列表修改数据#######################
print(20*"#")
# 语法：  列表变量名[索引] = 新值
# 1. 定义一个列表
data_list_6 = ["张三","李四"]
# 2. 修改数据
data_list_6[0]="钻石张三"
print(data_list_6)
#####################列表删除数据#######################
print(20*"$")
# 列表变量名.pop(索引)
data_list_7 = ["张三","李四"]
# data_list_7.pop(0)
# 列表变量名.pop() 如果不写索引 默认删除列表的最后一个
data_list_7.pop()
print(data_list_7)
