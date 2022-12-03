"""
if else 语法：

if 条件判断 :
    条件判断为真[True] 执行代码1
    条件判断为真[True] 执行代码2
    ...
else:
    条件判断为假[False] 执行代码1
    条件判断为假[False] 执行代码2
    ...
1. else 和 if配合使用。它不能单独使用
2. else 是Python关键字。后边要有冒号
3. 有冒号就要换行缩进 【1个缩进 按一次Tab键】
"""
# 1.输入一个年龄【把年龄转换为整形数据】
# 变量名 = input(提示信息)
# 类型转换
# 变量名 = int( input(提示信息)   )
age = int(  input("请输入年龄:")  )
# 2.如果年龄大于18岁 可以去网吧
if age>18:
    print("开心消消乐")
    print("happy")
# 3. 否则 在家好好学习
else:
    print("学习使我快乐")
    print("else 否则")
print("1111  和if没有关系了")
