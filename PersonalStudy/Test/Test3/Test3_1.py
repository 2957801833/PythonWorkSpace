#编写程序，提示用户输入五边形顶点到中心点的距离，从而求出五边形的面积

#导包
import math
#提示用户输入
r = eval(input("请在此输入半径r的长度（例如：3）:"))
#根据公式计算五边形的边长
s = 2*r*math.sin( math.pi/5 )
#计算五边形面积
Area = 5*s*s / 4 * math.tan( math.pi/5 )
#输出结果
print("顶点到中心点的距离为：",r ,"边长为：",s ,"面积为：",Area )