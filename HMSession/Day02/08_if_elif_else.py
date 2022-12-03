"""
if elif else
语法：

if 条件判断1：
    条件1成立 执行代码
elif 条件判断2：
    条件2成立 执行代码
elif 条件判断3:
    条件3成立 执行代码
...
else:
    其他情况 执行代码

1. elif 要配合 if使用。 【不能单独使用】 elif 是Python关键字
2. 只要 有一个条件成立，会执行这个条件满足的代码，其他的就不再判断了
"""
# 1. 定义 score 变量记录考试分数
score = 90
# 2. 如果分数是 大于等于 90分 显示 优
if score >= 90:
    print("优")
# 3. 如果分数是 大于等于 80分 并且 小于 90分 显示 良
elif score >= 80 and score < 90 :
    print("良")
# 4. 如果分数是 大于等于 70分 并且 小于 80分 显示 中
elif score >= 70 and score < 80:
    print("中")
# 5. 如果分数是 大于等于 60分 并且 小于 70分 显示 差
elif score >= 60 and score < 70:
    print("差")
# 6. 其它分数显示 不及格
else:
    print("不合格")