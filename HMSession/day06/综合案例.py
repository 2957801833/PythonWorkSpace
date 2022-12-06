"""
① [  ["张三",19],["李四",18], ["王五",22] ]
②  后续课程中 最常用的
[{“name”:"张三","age":19} , {“name”:"张三","age":19} ]

"""
#定义函数
# 第一步：录入学生信息
# 单个学生信息的函数，并返回学生的信息
def one_info():
    name = input("请输入姓名:")
    age = int( input("请输入年龄:") )
    #定义一个字典
    stu = {
        "name":name,
        "age":age
    }
    # 返回字典
    return stu
# 定义一个全局变量
students = []
# 用于录入学习信息
def record_student():
    # 循环三次 while  或者 for in range
    n = 1  # ① 循环计数器
    while n<=3:  # ② 循环条件的判断
        s = one_info()  # s 是一个字典
        # 给字典新增数据   字典变量名["key"]=value
        s["id"]=n
        students.append(s)  # 给列表追加数据
        n += 1  # ③ 循环计时器改变
# 第二步：展示学生列表信息
# [{'name': '张三', 'age': 19, 'id': 1}, {'name': '王五', 'age': 22, 'id': 2}]
def show_stu():
    print("------------学生信息列表--------------")
    # for in
    for item in students:
        # item 就是字典
        print(f"{item.get('id')}\t\t{item['name']}\t\t{item.get('age')}")
    print(30*"-")

# 第三步：统计学生总数     --- 统计列表的元素个数 [一级元素个数]
# [  [],[],[] ]
# [{“name”:"张三","age":19} , {“name”:"张三","age":19} ]
def stu_count():
    count = len(students)
    return count
# 第四步：查询学生信息
# [{“name”:"张三","age":19} , {“name”:"李四","age":19}, {“name”:"王五","age":19} ]
def select_stu():
    # 定义一个布尔值   真表示找到了   假表示没有找到
    is_find = False
    name = input("请输入要查询的学习姓名:")
    # 1. 每个元素 都要看看  -- 遍历 [获取容器中的每一个元素]
    for item in students:
        # item 是一个字典
        # 2. 获取字典的name 来进行比较
        if name == item.get("name"):
            print("找到了")
            is_find = True
            print("姓名:{} 年龄:{}".format(item.get("name"),item["age"]))
    # for 结束了 就算是没有找到呢？？？
    #print("没找到")
    if not is_find:
        print("没有找到")
if __name__ == '__main__':
    # 调用函数
    record_student()
    print(students)
    show_stu()
    # 统计学生数量
    print(  stu_count() )
    # 查询
    select_stu()

