# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:GitWang
# datetime:2019/7/31 20:57
# software: PyCharm

# 导入模块，使用导入模块的函数时语法是： 模块名.函数名()
from LearnPythonGrammar.BaseGrammar import Function as Func
# 导入模块中指定函数，函数可以使用逗号分割从而导入多个函数，语法：函数名（）
# 可以通过as给导入函数重新命名
from LearnPythonGrammar.BaseGrammar.Function import make_shirt as ms, modify_users as mu

c = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
b = [2, 3, 4]
for item in b:
	b[0] = 1
	print(b[0])
for item in c:
	if item == '1':
		print(item + 'st')
	elif item == '2':
		print(item + 'nd')
	elif item == '3':
		print(item + 'rd')
	else:
		print(item + 'th')

# 调用模块使用模块中指定的函数
Func.make_shirt('M', 'Nike')
ms('s', 'add')
username = ['wh', 'dd', 'zz']
newList = []
mu(username, newList)
