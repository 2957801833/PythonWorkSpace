"""
主要是为了 掌握 匿名函数 的语法

"""
# 列表的数据排序
# data_list = [1,8,3,5,2]
# data_list.sort()
# print(data_list)
# 排序 肯定是 把列表中的每一个数据 至少遍历1次

# 对字典列表的数据进行排序
# [  {},{},{} ]
data = [
    {"name":"迪丽热巴","age":20},
    {"name":"幂幂","age":30},
    {"name":"凯凯","age":22}
]
# {"name":"迪丽热巴","age":20}   字典变量名.get("age")     20
# 默认情况下 不能对字典数据进行排序， 应该是对字典的某一个key对应的value排序
# data.sort(key=匿名函数)
# 匿名函数 用于实现  通过字典的key值来获取value值 从而实现排序
# lambda 参数:表达式
# lambda 列表的每一个元素: 表达式可以用参数
# lambda num1,num2 : num1 + num2
data.sort(key= lambda item: item.get("age") )
# 不要纠结于 它到底是怎么排序的 ，你要掌握的是 匿名函数的写法
print(data)