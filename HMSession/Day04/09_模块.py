"""
1. 模块 通俗来说 就是 py结尾的 python文件
2. 我们把一些 常用的 代码 常用的函数 放到一个单独的模块里，方便使用

"""
import random
random.randint(1,10)

# 如何使用 我们定义的模块呢【工具包】
# import 模块名
import common
# 如何使用
# 模块名.函数名()
result = common.get_2_sum(1,1)
print(result)
# 模块名.变量名
print(common.num)

# import 模块
# imort 理解把模块的所有东西都导入过来
# from 模块名 import 函数1,函数2,变量1...
# from .. import .. 理解为 需要模块的某一个 函数变量
from common import get_2_sum
#直接使用 函数名 ，变量名
r = get_2_sum(10,10)
print(r)

# print(num)
##################起别名
# as 作为 起别名
# 1. 函数名，变量名 名字太长
# 2. 有可能名字重复
from common import get_2_sum as aaaa
print( aaaa(1,2) )