#绘制五个不同的图形page83

#导入模块
import turtle
#设置笔的粗细为3个像素点
turtle.pensize(3)
#将笔向上拉，这样就可以改变接下来点的位置
turtle.penup
turtle.goto(-200,-50)
#将笔拉下
turtle.pendown()

#turtle对象调用radius为40和阶数为3的circle方法绘制出一个三角形
#绘制一个三角形
turtle.circle(40,steps=3)

#绘制一个正方形
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.circle(40, steps=4)

#绘制一个五边形
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(40,steps=5)

#绘制一个六边形
turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.circle(40,steps=6)

#绘制一个圆
turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.circle(40)

#显示图形化界面
turtle.done()