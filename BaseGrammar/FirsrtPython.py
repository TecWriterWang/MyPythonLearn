
"""
多行注释

"""
# 导入海龟绘图
# import turtle
# t = turtle.Pen()
# for x in range(360):
#     t.left(90)
#     t.forward(x)

# python中int型数据支持二进制0b、八进制0o、十六进制0x
print(0b100)
print(0o100)
print(100)
print(0x100)

# 浮点数float，支持科学记数法1.2e3
print(1.2122e3)

# 字符串型str
print("""11122323212331313414aasdsd")""")

# 布尔型数据只有True和False
print(10 > 11)

# 复数型，虚部单位是j
print(4+3j)

# 用占位符(d%)格式化输出的字符串
print('%d + %d = %d' % (1, 2, 1 + 2))

# 使用type()或者isinstance() 检测数据类型
print(type(1))
print(type(True))
print(type("ssss"))
print(isinstance("a", int))

# 将一个数值或字符串转换成整数，可以指定进制。
int()
print(int(0x10))
# 将一个字符串转换成浮点数。
float()

# 将指定的对象转换成字符串形式，可以指定编码。
str()

# 将整数转换成该编码对应的字符串（一个字符）。
print(chr(97))
# 将字符串（一个字符）转换成对应的编码（整数）
print(ord("a"))

# 指数乘方表示: **
print(2**3)
# 整除(只保留整数部分)：//
print(3//2)


age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)
print("\tPython")  # 制表符
print(message)
print(message.lstrip())  # strip删除拉两端的空白，rstrip删除末尾的空白，lstrip删除开头的空白
print(message.title())  # title()函数将单词首字母大写，单词其他有大写的转化为小写
print(message.lower())  # lower()函数将所有单词字母小写，upper()函数相反
print(message.upper())  # "\t"是制表符，当输入制表符"\t"，换行符"\n" 或者空格" "或其他空字符时需要前后输入空格
print("a\n\tC\n V")  # 字符串中空格直接敲就好
print(' ' + 'V')  # 非字符串时输出空格需要加引号,使用"+"连接前后
print(3 ** 3)  # 两个**表示乘方运算


# if else 紧凑形式
print("Hello")if True else print("world")
