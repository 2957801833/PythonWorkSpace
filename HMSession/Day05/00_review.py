
# 1. 定义变量 统计 - [空格] 的个数
# 函数的步骤：
#① 定义函数
def count_space(str_data):
    result = 0
    for item in str_data:
        if item == ' ':
            result = result + 1
    return result
#② 函数调用
str1 = "aaa   bbb  "
num  = count_space(str1)
print(num)