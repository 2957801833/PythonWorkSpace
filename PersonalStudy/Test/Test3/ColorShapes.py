#导包
import turtle
#设置笔的像素为3
turtle.pensize(3)
#抬起笔
turtle.penup()
#设置坐标
turtle.goto(-200,-50)
#放下笔
turtle.pendown()
#调用begin_fill方法在图形中填充颜色
turtle.begin_fill()
#设置图形所填充的颜色
turtle.color("red")
#绘制一个三角形
turtle.circle(40, steps=3 )
#结束填充
turtle.end_fill()

# #设置笔的像素为3
# turtle.pensize(3)
#抬起笔
turtle.penup()
#设置坐标
turtle.goto(-100,-50)
#放下笔
turtle.pendown()
#调用begin_fill方法在图形中填充颜色
turtle.begin_fill()
#设置图形所填充的颜色
turtle.color("blue")
#绘制一个四边形
turtle.circle(40, steps=4 )
#结束填充
turtle.end_fill()

# #设置笔的像素为3
# turtle.pensize(3)
#抬起笔
turtle.penup()
#设置坐标
turtle.goto(0,-50)
#放下笔
turtle.pendown()
#调用begin_fill方法在图形中填充颜色
turtle.begin_fill()
#设置图形所填充的颜色
turtle.color("green")
#绘制一个五边形
turtle.circle(40, steps=5 )
#结束填充
turtle.end_fill()

# #设置笔的像素为3
# turtle.pensize(3)
#抬起笔
turtle.penup()
#设置坐标
turtle.goto(100,-50)
#放下笔
turtle.pendown()
#调用begin_fill方法在图形中填充颜色
turtle.begin_fill()
#设置图形所填充的颜色
turtle.color("yellow")
#绘制一个圆形
turtle.circle(40, steps=6 )
#结束填充
turtle.end_fill()

# #设置笔的像素为3
# turtle.pensize(3)
#抬起笔
turtle.penup()
#设置坐标
turtle.goto(200,-50)
#放下笔
turtle.pendown()
#调用begin_fill方法在图形中填充颜色
turtle.begin_fill()
#设置图形所填充的颜色
turtle.color("pink")
#绘制一个圆形
turtle.circle(40)
#结束填充
turtle.end_fill()

turtle.color("green")
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.write("色彩缤纷的图形",
             font = ("Times", 18, "bold")
             )
turtle.hideturtle()

#显示图形化界面
turtle.done()