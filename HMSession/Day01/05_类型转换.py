"""

我们的需要是 通过程序 来输入一个数值
我们用一个变量接收这个数值，然后对数值进行类似于计算的操作
num = 5
print( 数量 * 价格 )
print( num * 10 )
print( 5 * 10 )  50
* 乘法的意思
"""
# ① input() 所获取的任意数据 都是字符串类型 和你输入什么没有关系
# 1. 借助于 input 获取用户要购买的数量 5
# 变量名 = input(提示信息字符串)
num = input("请输入购买数量:")
# 2. 打印 乘以的结果  数量 * 单价[10]
# * 乘法的意思
# num 不是 整形  是什么类型呢？？？
print(  type(num)  )
# ② 整数 乘以 字符串 系统会重复 整数次 字符串
# print(  "a" * 5 )
# ③ 我们需要 让 整数 和 整数 进行 乘法运算
# 所以需要把 字符串 转换为 整数
# 如何转呢？ 语法是：  要转换的类型(  数据  )
# 例如： 我们要转换为整数 int( "10" )
print(  int( num )  * 10  )
# 相当于 打印了 10次10
#10101010101010101010
# print(  10   * 10  )
# 100
