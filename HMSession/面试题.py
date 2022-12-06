# 如何实现2个列表合并
data_list_1 = [1,2,3]
data_list_2 = [4,5,6]
# 方式1    +
print(  data_list_1 + data_list_2 )
# 方式2   拆包    *()   *[]
# 元组和列表 其实是一样的。只不过，元组不能修改
# print(  [ data_list_1,data_list_2 ]  )
print(  [ *data_list_1 , *data_list_2 ] )
# 方式3  extend
data_list_1.extend(data_list_2)
print(  data_list_1 )

#####################################################
# 如何实现2个字典的合并
data_dict_1 = {"name":"itheima"}
data_dict_2 = {"age":20}
# 方式1
# 拆包！    字典的拆包是2个 *     **
print(  {  **data_dict_1, **data_dict_2  }  )

# 方式2  update
data_dict_1.update(data_dict_2)
print( data_dict_1  )

################################################
# 列表和字典的区别
# 列表： 有顺序的
# 字典： 没有顺序的  key:value

# 列表和元组的区别
# 元组不能修改