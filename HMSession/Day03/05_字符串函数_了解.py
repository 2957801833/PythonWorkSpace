# 字符串.find(要查找的字符串)
# find  查找
# 被查找字符是否存在于当前字符串中, 如果存在则返加开始下标, 不存在则返回 -1
# 1. 定义一个字符串变量
str1 = "爱你一万年"
# 爱你一万年
# 0 1 2 3 4
# 2. 查找指定的字符的位置
# position 位置
position=str1.find("二")
print(position)
##################replace 替换############################
# 最终字符串 = 字符串.replace(旧字符串，新字符串)
# replace 替换
# 爱你一万年  变成 爱你千万年
new_str2 = str1.replace("一","千")
print(new_str2)
####################split 分割 ####################
print(20*"!")
# 列表数据 = 字符串.split(分隔符)
# split 分割 可以对 规律性的数据 按照规律 分割
str3="keyword=手表&enc=utf-8&wq=手表"
# keyword=手表
# enc=utf-8
# wq=手表
# 数据变量名 = 数据值
data = str3.split("&")
print( data, type(data) )

####################join 拼接 ####################
print(20*"@")
# join 拼接
# 新字符串 = "拼接的标志".join( 列表 )
#  地址里 有 省市区 数据在列表中  列表一会儿就讲
# [] 就是列表   [  字符串1,字符串2,字符串3 ]
data_list = [  "河北省" ,  "保定市"  , "定兴县"   ]
# 河北省-保定市-定兴县
# "拼接的标志".join( 列表 )
str4 = "---".join( data_list )
print(str4)
