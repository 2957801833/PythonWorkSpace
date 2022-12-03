# count 数量
data_list_1 = [  "Python","Java","C","Python" ]
# 变量名 = 数据
# 统计元素[数据] 的个数
print(  data_list_1.count("Python")  )
##############reverse 反转################################
# reverse  反转
data_list_2 = [1,2,3,4]
# 列表变量名.reverse()
# 原列表就发生变化了
data_list_2.reverse()
print(data_list_2)
########################################
# sort  排序
# 面试： 给你一个列表数据 你怎么排序
data_list_3 = [3,7,1,9,2,5]
# 列表变量名.sort()
# 原列表就发生了变化
# sort 默认是升序
# data_list_3.sort()
# reverse=True 降序
# reverse=False 升序序
data_list_3.sort(reverse=True)
print( data_list_3 )