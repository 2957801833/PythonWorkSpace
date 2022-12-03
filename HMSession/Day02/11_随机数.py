# 系统有随机数的工具包 我们导入就可以用
# 导入 import
# 随机数 random
# 1. 导入随机数工具包
# ① import 是Python关键字 后边必须跟一个空格
# ② 作用就是 导入工具包
# ③ random.randint(开始值，结束值)
import random
# 2. 使用 工具包的 随机整数 来生成随机数
# 设置随机整数的范围  [开始整数值,结束整数值] 包含边界的
# 变量名 = 数据值
num = random.randint(1,10)
print(num)