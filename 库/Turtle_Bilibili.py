import turtle

# 设置窗口标题
turtle.title("Bilibili")

# 先将color切换为rgb模式
turtle.colormode(255)
# 画布默认大小，默认大小(400, 300)
turtle.screensize()
# 设置画布大小
turtle.screensize(800, 600, 'white')

# 调整画笔方向
turtle.left(90)

# 设置窗口大小为
turtle.setup(width=800, height=800, startx=100, starty=100)
turtle.setup(width=800, height=800)

turtle.home()  # 回到起点
turtle.clear()  # 清屏

# 显示画笔st   turtle.showturtle()
# 隐藏画笔ht     turtle.hideturtle()
turtle.ht()

# 画笔落下pendown(pd)/抬起penup(up/pu)
turtle.pd()
turtle.penup()
# 设置画笔的宽度
turtle.width()
turtle.pensize()

# 设置画笔颜色
turtle.pencolor((55, 191, 243))

# 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。
turtle.speed(5)

# 书写指定字符,arg 指定的字符串 - 到当前海龟位置，align 指定对齐方式 ("left", "center" 或 right")，
# font 指定字体。如果 move 为 True，画笔会移动到文本的右下角。默认 move 为 False,在右上角
# turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
turtle.write()

turtle.shape("circle")
# 设置海龟形状为 name 指定的形状名,多边形的形状初始时有以下几种:
"arrow", "turtle", "circle", "square", "triangle", "classic"


# turtle.circle(radius, extent)

# radius为正时，圆心在当前位置左侧（如下图）；radius为负时，圆心在当前位置右侧；
# extent为正时，顺画笔当前方向绘制，extent为负时，逆画笔当前方向绘制


# 绘制电视框架
turtle.up()
turtle.goto(-200, 150)
turtle.pd()
turtle.pensize(10)
turtle.goto(200, 150)
turtle.goto(200, -150)
turtle.goto(-200, -150)
turtle.goto(-200, 150)

# 绘制两个小角
turtle.up()
turtle.goto(-50, 150)
turtle.pensize(7)
turtle.pd()
turtle.goto(-100, 200)
turtle.penup()
turtle.goto(50, 150)
turtle.pendown()
turtle.goto(100, 200)

# 绘制电视里面眉毛
turtle.penup()
turtle.goto(-45, 100)
turtle.pensize(10)
turtle.pendown()
turtle.goto(-145, 70)
turtle.penup()
turtle.goto(45, 100)
turtle.pendown()
turtle.goto(145, 70)
#
# 绘制嘴巴
turtle.penup()
turtle.goto(0, -20)
turtle.pensize(7)
turtle.pendown()
turtle.left(90)
turtle.circle(20, -180)
turtle.up()
turtle.goto(0, -20)
turtle.pendown()
turtle.circle(20, 180)

# # 绘制脚
turtle.speed(10)
turtle.up()
turtle.goto(-50, -150)
turtle.pensize(10)
turtle.pd()
for i in range(31):
    turtle.circle(i, -180)
    turtle.goto(-70, -150)
    turtle.left(180)

turtle.up()
turtle.goto(50, -150)
turtle.left(180)

turtle.pd()
for i in range(31):
    turtle.circle(i, 180)
    turtle.goto(70, -150)
    turtle.left(180)

turtle.exitonclick()

# 画一条蛇
# turtle.goto(-300, 0)
# turtle.pd()
# turtle.speed(1)
# turtle.pensize(25)
# turtle.colormode(255)
# turtle.pencolor((0, 255, 0))
#
# turtle.seth(45)
# for i in range(4):
#     turtle.circle(-40, 80)
#     turtle.circle(40, 80)
# turtle.circle(40, 40)
#
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40 * 2/3)


# 画一个z
# # seth始终以最初的位置旋转方向
# # turtle.seth(-90)
# # turtle.fd(300)
# # turtle.seth(45)
# # turtle.fd(150)
#
# # turtle.exitonclick()
#
# turtle.done()

# 画一个八角形
# turtle.pensize(2)
# for i in range(8):
#     turtle.fd(150)
#     turtle.left(135)
