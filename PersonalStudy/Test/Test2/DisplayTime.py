# 输入秒转换为分钟


seconds = eval(input("请在此输入一个整数："))

# 定义分钟有多少秒
minutes = seconds // 60

remainningSeconds = seconds % 60

print(seconds, "秒为：", minutes, "分钟", remainningSeconds, "秒")
