#使用input提示用户输入相应的值，使用eval接收用户在控制台输入的值,eval同时可以接收算法并计算出结果后进行返回
radius = eval(input("请在此输入半径值："))

#计算面积
area = radius * radius * 3.14159

#输出值
print("圆的半径为：",radius,"面积为：",area)