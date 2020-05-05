s = "1123222222"
# s.join(x),使用s分割字符串x，在x的每个元素之间添加s,此时s为一个整体看待
s2 = s.join("aaa")
print(s2)
# s.center(width, fillchar) 字符串居中输出，指定s的宽度，以及填充字符
s1 = s.center(20, "-")
print(s1)
# 返回字符串中子串x的位置，find(x)不会报错，没有iu返回-1，index(x)报错
print(s.find('0'))
print(s.index('222222'))
# count(x)返回字符串中x出现的总次数
print(s.count('2'))
# 字符串替换
s = "sss12344"
print("123445444".replace("4", "1"))
print(s.replace('4', '1'))
# max(s)返回字符串中的最大值，min(s)返回字符串中的最小值，比较大小时先转化为ASCII码后在比较
# chr()将整数转化为字符,ord()将数字转化为字符

# s.lower()所有字符小写 .upper()所有字符大写 .capitalize()首字母大写
"sss123".upper()
s.capitalize()
str_one = 1234.456
str_two = str(123)
str_three = " english Mooc2222222  "
print("{1}+++{2}+++{0}".format(str_one, 123, 'rrrr'))
print("{0:->10,.2f}{2:-^20.10}{1}".format(str_one, 123, str_three))
# 当字符串最大输出宽度小于槽位设定宽度，才会填充字符，
print('''{参数编号:填充字符+对其方式+槽位设定宽度+数字千分位，+精度（.浮点小数位数/字符串最大输出长度）+类型(b,c,d,o,x,X)}''')
# upper 将所有字符大写
print(str_three.upper())
# lower 将所有字符小写
print(str_three.lower())
# title 将字符串首字母大写
print(str_three.title())
# split 通过指定字符将字符串分割成子串并存储到列表中
print(str_three.split(' '))
# strip 删除字符串中左右两边的指定字符
print(str_three.strip(" enoc "))
# 删除字符串最后边的指定字符
print(str_three.lstrip(' '))
# 删除字符串最前边的指定字符
print(str_three.rstrip(' '))
# str.join() 在字符串中每个字符后面添加的指定字符str
print('+'.join(str_three))
# replace(old, new) 将字符串中字符替换成指定字符
print(str_three.replace('Mooc', 'MOOC'))
# center 指定字符串宽度并居中，宽度不够时填充指定字符
print(str_three.center(20, '*'))
# chr()将整数转换成字符
print(chr(100))
# ord()将字符转换成整数
print(ord('d'))
# str()将整数变换字符串，添加引号
print(str(1234))
# eval()将字符串变换为数字，去掉引号
print(eval('1234'))
# 转化成十六进制
print(hex(111))
# 转化成十进制
print(oct(111))