import turtle, time

# n = int(input())
# str_one = 'Hello World'
# if n == 0:
#     print("Hello World")
#     # TODO: write code...
# elif n > 0:
#     for i in range(1, len(str_one)+1):
#         print(str_one[i-1], end='')
#         if i % 2 == 0:
#             print()
# else:
#     for i in range(len(str_one)):
#         print(str_one[i])


# str_one = input()
# # eval()函数只能处理数字形式的字符串
# print(eval(str_one[0:-1]))
# op = ['+', '-', '*', '/']
# i = 1
# while str_one[i] not in op:
#     i += 1
# else:
#     print(str_one[0:i])
#     print(str_one[i+1:])
#     # eval()函数将数字形式字符串的引号去掉，（只保留数字,空格也删除）
#     first_number = eval(str_one[0:i])
#     last_number = eval(str_one[i+1:])
#     print(first_number, last_number)
#
# if str_one[i] == op[0]:
#     result = first_number + last_number
# elif str_one[i] == op[1]:
#     result = first_number - last_number
# elif str_one[i] == op[2]:
#     result = first_number * last_number
# elif str_one[i] == op[3]:
#     result = first_number / last_number
# # 格式输出 "{:.保留小数位+类型}".format()
# print("{:.2f}".format(result))


# print(round(10.29, 1), 0b0101, 0xA, 0o111)
# # 商余
# a, b = divmod(10, 3)
# print(a, b)

# 绘制7段数码管
# 绘制函数


def drawGap():
    # 每条线之间加上间距

    turtle.up()
    turtle.fd(5)


def drawLine(draw):
    # 绘制线
    turtle.pensize(3)
    turtle.speed(5)
    drawGap()
    turtle.down() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigit(digit):
    # 绘制第1条线的数字
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    # 绘制第2条线数字
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    # 绘制第3条线的数字
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    # 绘制第4条线数字
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    # 绘制第5条线数字
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    # 绘制第6条线的数字
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    # 绘制第7条线的数字
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.up()
    # 绘制多个数字 调整绘制方向，移动间距
    turtle.left(180)
    turtle.fd(20)


def drawDate(date):
    print(date)
    for item in date:
        if item == "-":
            turtle.write("年", font=("Arial", 18, "normal"))
            turtle.color("green")
            turtle.fd(40)
        elif item == "=":
            turtle.write("月", font=("Arial", 18, "normal"))
            turtle.color("blue")
            turtle.fd(40)
        elif item == "+":
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(item))


def main():
    turtle.setup(1000, 600)
    turtle.up()
    turtle.ht()
    turtle.goto(-200, 0)
    turtle.title("七段数码管")
    drawDate(time.strftime("%Y-%m=%d+", time.gmtime()))
    turtle.reset()


main()

turtle.setup(400, 300)
turtle.title("倒计时")
turtle.ht()

drawDate("10")
for i in range(10, -1, -1):
    if i <= 5:
        turtle.color("red")
    # turtle.write(i, move=True, align="center", font=("黑体", 100, "normal"))
    drawDigit(i)
    # turtle.delay(1)
    # turtle.update()
    turtle.reset()

turtle.write("发射", move=True, align="center", font=("Arial", 30, "normal"))
turtle.exitonclick()
a = "1,1,2"
b = []
for i in a:
    b.append(list(map(eval, i.split(","))))
