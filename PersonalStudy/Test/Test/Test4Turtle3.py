#使用turtle绘制奥林匹克标志
#导入模块
import turtle

#绘制第一个蓝色圆形，坐标为（-110，-25），半径为45
turtle.color("blue")
turtle.penup()
turtle.goto(-110,-25)
turtle.pendown()
turtle.circle(45)

#绘制第二个黑色圆形，坐标为（0，-25），半径为45
turtle.color("black")
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(45)

#绘制第三个红色圆形，坐标为（110，-25），半径为45
turtle.color("red")
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

#绘制第四个黄色圆形，坐标为（-55，-75），半径为45
turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

#绘制第五个绿色圆形，坐标为（55，-75），半径为45
turtle.color("green")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)

#给用户时间来查看图形
turtle.done()