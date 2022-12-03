#导包
import turtle

#提示用户输入两个点的坐标
x1,y1=eval(input("请输入两个点的坐标（请使用英文逗号进行分割,例如：-50,50）："))
x2,y2=eval(input("请输入两个点的坐标（请使用英文逗号进行分割,例如：-50,50）："))

#计算距离
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

#显示两点和之间的连接线
turtle.penup()
#以(x1,y1)为起点划线
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("点1")
#向(x2,y2)开始划线
turtle.goto(x2,y2)
turtle.write("点2")

#移动到这条直线的中心点
turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.write(distance)

# 显示观测窗口
turtle.done()