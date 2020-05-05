str_one = 1234.456
str_two = str(123)
str_three = " english Mooc2222222  "
print("{1}+++{2}+++{0}".format(str_one, 123, 'rrrr'))
print("{0:->10,.2f}{2:-^20.10}{1}".format(str_one, 123, str_three))
# 当字符串最大输出宽度小于槽位设定宽度，才会填充字符，
print('''{参数编号:填充字符+对其方式+槽位设定宽度+数字千分位，+精度（.浮点小数位数/字符串最大输出长度）+类型(b,c,d,o,x,X)}''')
# 整数输出补零
print('%010d' % 123)
