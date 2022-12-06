"""
①参数的默认值  就是 给形参一个默认的数据值
如果 不给这个参数 传递数据，则使用默认值 【我们可以少写数据】
如果 给这个参数 传递数据，则使用传递的数据
② 注意事项：默认值的参数 必须放在 函数参数的最后边
"""
# record 记录   info
def record_info(name,sex="boy"):
    print(f"姓名是:{name},性别是{sex}")
#调用函数
# 位置参数
# record_info("张三","boy")
# record_info(name="王五",sex="boy")
# record_info(sex="boy",name="赵六")
record_info("张三")
record_info("李四")
record_info("白雪公主","girl")