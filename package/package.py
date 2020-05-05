"""
1.包其实就是一个文件夹，但是必须有 __init__.py 文件，该文件就是包的标识，没有这个标识的化就时普通文件夹
2.一个包中可以有子包,只要是包就必须要有__init__.py文件,导入包就是执行__init__.py文件
3.通常__init__文件中存放一些简单的代码，可以将多个模块导入到包的__init__.py文件，只要在其他文件中调用子包就可以使用多个模块
4.一旦打开包中的__init__.py文件会发现名称会带包名，若是普通文件夹的py文件不会
"""

import LearnPythonGrammar as LPG  # 导入父包
import sys

from LearnPythonGrammar import add  # 导入子包中某个方法

a = LPG.math.pi
print(a)
# LPG.turtle.fd(10)
# LPG.turtle.done()
add()
print(sys.path)