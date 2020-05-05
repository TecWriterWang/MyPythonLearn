# coding=utf-8
import os

# 返回系统名
print(os.name)  # windows->nt linux->posix
# 返回系统分隔符
print(os.sep)

# 获取文件相关信息
print(os.stat('OS库.py'))

# 获取当前工作目录 os.getcwd()
print(os.getcwd())
# os.chdir()  修改当前目录
# os.mkdir(path) 创建path目录

# os.rmdir(path)  删除path目录，目录下有文件无法删除
# os.rmmove(file)  删除file文件

# os.makedirs(path1/path2) 创建多级目录
# os.removedirs(path1/path2) 删除多级目录
# os.rename('ordpath', 'newpath')

os.mkdir('test')
# os.rmdir('test1')
os.rename('test', 'test1')
# 列出当前目录下的一级目录或文件
print(os.listdir(r'H:\PythonWorkSpace\PythonCode\LearnPythonGrammar\库'))


# os.system(command)               # 执行程序或命令command,在Windows系统中，返回值为cmd的调用返回信息

os.system('notepad.exe')
os.system('ping www.google.com')

# 运行可执行程序
os.startfile(r"H:\VSCode\Microsoft VS Code\Code.exe")
os.system('cmd')

os.getlogin()                     # 获得当前系统登录用户名称
os.cpu_count()                 # 获得当前系统的CPU数量
os.urandom(10)                 # 获得n个字节长度的随机字符串，通常用于加解密运算

# 递归遍历所有文件和目录，返回三个元素的元祖(dirpath, dirnames,filenames)
# dirpath=指定目录的路径  dirnames=目录下的所有文件夹  filenames=目录下的所有文件
os.walk('path')

# os.path 操作目录相关的库

path = r'H:\PythonWorkSpace\PythonCode'
paths = r'H:\PythonWorkSpace\PythonCode\LearnPythonGrammar\BaseGrammar'

os.path.abspath(path)                # 返回path在当前系统中的绝对路径
os.path.normpath(r'D://testFile//test.txt')            # 归一化path的表示形式，统一用\\分隔路径
os.path.relpath(path)                # 返回当前程序与文件之间的相对路径 (relative path)
os.path.dirname(path)               # 返回path中的目录名称
os.path.basename(path)            # 返回path中最后的文件名称
os.path.join(path, *paths)          # 组合path与paths，返回一个路径字符串

# 判断文件路径
os.path.isabs(path)                  # 判断是否是绝对路径
os.path.exists(path)                   # 判断path对应文件或目录是否存在，返回True或False
os.path.isfile(path)                      # 判断path所对应是否为已存在的文件，返回True或False
os.path.isdir(path)                      # 判断path所对应是否为已存在的目录，返回True或False

# 返回文件相关修改属性

os.path.getatime(path)              # 返回path对应文件或目录上一次的访问时间
os.path.getmtime(path)            # 返回path对应文件或目录最近一次的修改时间
os.path.getctime(path)             # 返回path对应文件或目录的创建时间
os.path.getsize(path)                # 返回path对应文件的大小，以字节为单位



