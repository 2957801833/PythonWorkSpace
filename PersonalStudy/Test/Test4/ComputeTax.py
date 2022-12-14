#单身税款解决方案（美国）page105

#导包
import sys
#请用户输入相应数字对应自身婚嫁状态
status = eval(input("0-单身报税人, 1-已婚合并申报人,\n"+
                    "2-已婚分开申报人, 3-户主\n"+
                    "请在此输入您的状态码："
                    ))
#提示用户输入应纳税所得额
income = eval(input("请在此输入应纳税所得额："))
#初始化征税标准
tax = 0
#计算单个报税人的税额
if status == 0:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 +\
              (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
              (372950 - 171550) * 0.33 + (income - 372950) * 0.35;
#已婚档案共同计税
elif status == 1:
    print("已婚档案共同计税")
#单独计算已婚人士的税额
elif status == 2 :
    print("单独计算已婚人士的税额")
#计算户主税金
elif status == 3 :
    print("计算户主税额")
else:
    print("输入错误：无效状态")
    #退出系统
    sys.exit()
#展示结果
print("税额为：",format(tax,".2f"))