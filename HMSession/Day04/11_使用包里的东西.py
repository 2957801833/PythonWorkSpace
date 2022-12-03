# 方式1
# import 包名.模块名
import tpshop.utils
# 包名.模块名.函数名
print( tpshop.utils.get_2_max(1,2)  )
# 方式2
# from  包名 import 模块名
from tpshop import utils
#模块名.函数名
print( utils.get_2_max(3,6) )
# 方式3
# from 包名.模块名 import 函数名
from tpshop.utils import get_2_max
# 函数名
print( get_2_max(44,66) )