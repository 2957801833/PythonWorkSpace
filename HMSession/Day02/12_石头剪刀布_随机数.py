'''
1. 规则是： 石头（1）／剪刀（2）／布（3）
2. 我们出一个：  input("输入石头（1）／剪刀（2）／布（3）")
3. 电脑出一个：  电脑随机出一个（1,2,3）
4. 比较结果
胜  ①我们出 石头1  电脑出 剪刀2   ② 我们出 剪刀  电脑出 布
    ③我们出 布    电脑出 石头
平       相等
负
'''
# 1. 输入我们要出的数字
# input 获取的是字符串，我们进行比较的是整数 所以要进行类型转换
num = int(  input("输入石头（1）／剪刀（2）／布（3）") )
# 2. 电脑出数字
# ① 导入 工具包
import random
# ② 用一个变量来接收 生成的随机整数
computer = random.randint(1,3)
print(computer)
# 3. 进行判断
if (num==1 and computer==2)or(num==2 and computer==3)or(num==3 and computer==1):
    print("我们赢了")
elif num == computer:
    # 2个等于号是比较
    print("平了")
else:
    print("我们输了")