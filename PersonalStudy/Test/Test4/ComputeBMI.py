#根据体重测量健康，实现方法：以千克为单位的体重 除以 以米为单位的身高

#提示用户在此输入体重
weight = eval(input("请再次输入体重，单位为斤："))
#提示用户在此输入身高
height = eval(input("请在此输入身高，单位为厘米："))
#设置体重单位转换，1斤为0.5千克
KILOGRAMS_PER = 0.5
#设置身高转换单位，1厘米为0.01米
METERS_PER = 0.01
#计算BMI指数
weightInKilograms = weight * KILOGRAMS_PER
heightInMeters = height * METERS_PER
bmi = weightInKilograms / (heightInMeters * heightInMeters)
#判断结果
print("BMI的结果为：",format(bmi,".2f"))
if bmi < 18.5:
    print("低于平均体重")
elif bmi < 25:
    print("体重标准")
elif bmi < 30:
    print("高于平均体重")
else:
    print("你真的该减肥了")