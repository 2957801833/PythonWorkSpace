#提示用户输入三角形三个点的坐标，然后显示三个角度

#导包
import math

#提示用户输入坐标
x1,y1,x2,y2,x3,y3=eval(input("请输入每个点的x、y坐标，请使用英文逗号对每个值进行分割(比如：x1,y1,x2,y2,x3,y3)："))

# #根据公式计算每条边的长度
# a = math.sqrt( (x2-x3)*(x2-x3) + (y2-y3)*(y2-y3) )
# b = math.sqrt( (x1-x3)*(x1-x3) + (y1-y3)*(y1-y3) )
# c = math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
a = math.sqrt( (x2-x3)**2 + (y2-y3)**2 )
b = math.sqrt( (x1-x3)**2 + (y1-y3)**2 )
c = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#根据边长求角度
A = math.degrees(math.acos( ( a*a - b*b - c*c ) / ( -2*b*c )))
B = math.degrees(math.acos( ( b*b - a*a - c*c ) / ( -2*a*c )))
C = math.degrees(math.acos( ( c*c - b*b - a*a ) / ( -2*a*b )))

#打印输出结果，并将结果转换为保存小数点后两位的数值
print("该三角形的三个角的坐标为：","(",x1,",",y1,")", "(",x2,",",y2,")", "(",x3,",",y3,")", "三个角的度数为：",round(A*100)/100, round(B*100)/100, round(C*100)/100 )