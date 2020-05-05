
# 绝对路径
# windows使用"\",但在python中“\”是转移字符，所以使用"/"来代替，或者使用“\\”,或者在前面加r
file_path1 = r'H:\PythonWorkSpace\PythonCode\File_Test\one.txt'
file_path2 = "H:\\PythonWorkSpace\\LearnPythonBaseCode\\File_Test\\one.txt"
file_path3 = "H:/PythonWorkSpace/LearnPythonBaseCode/File_Test/one.txt"

# 相对路径，
# 文件与程序代码所在同一个大文件夹中，可以是用"../文件路径"
file_path4 = r"H:\PythonWorkSpace\PythonCode\File_Test\file.txt"
# 若直接在源文件的文件夹中直接使用文件名即可。
file_path5 = r'H:\PythonWorkSpace\PythonCode\File_Test\test.json'
t2 = open(file_path5).read()
print(t2)
ls = t2.split()
print(ls)
file_path6 = r"H:\PythonWorkSpace\PythonCode\File_Test\Chinese.txt"
txt = open(file_path1, "rb")
print(txt.readline())
# tc = txt.read()
txt.close()


# open(文件路径, 打开方式)打开文件，打开文件
# 读取方式：
# r,只读文件，不能写,文件不存在返回FileNotFoundError
# w,只写文件，会将原来存在覆盖掉，文件不存在就创建文件,只能写,不能读
# x，创建写文件，不存在就创建文件，存在就返回FileExistsError,只能写不能读
# a，追加写模式，只能写,不能读在源文件的基础上再最后添加
# 附加
# b, 以二进制方式打开文件,如果打开不是文本文件而是代码源文件一定要使用b
# t, 以文本方式打开文件,若不指定打开方式就以t作为默认值,
# +, 与r/w/x/a一起使用,在原功能基础上可增加读写功能
t = open(file_path1, "r+", encoding="utf-8")
# for line in t:
#     # 此处直接使用文件名，就是直接将文件按行处理
#     print(line)

# # 读文件
# # read(size)读取文件全部内容，若指定长度size，就读取文件前size长度。
# print(t.read())
# # # readline(size)读取文件一行内容，若指定长度size，就读取该行前size长度。
# print(t.readline())
# # readlines(hint)读取文件所有行内容，并以每行元素形成列表，若指定长度hint，就读取前hint行。
# print(t.readlines())
# t.close()
# t.seek(offset, 位置) 移动指针位置，offset为正为结束方向移动，位置（0开始，1当前位置，2结束）
# t.tell() 返回指针位置
# t.name 返回文件名


# 写文件
# .write(s)向文件写入一个字符串或字节流
t1 = open(file_path4, "r+", encoding="utf-8")
with open(file_path4, "r+", encoding="utf-8") as f:

    print(f.name)

# t1.seek(offset)修改文件指针位置 0开头 1当前位置 2结尾
# 当写入文件后，指针将在写入的最后面，此时要读取文件内容，会读取指针之后的内容，
# 但是指针之后是空的，就不会返回任何值，使用seek即可解决
t1.write("china1 ")
t1.seek(0)
print(t1.readline())
# .writelines(lines)向文件写入一个全为字符串的列表,写入时将列表元素拼接写入
ls = ['new', ' China\n']
t1.writelines(ls)
t1.seek(0)
print(t1.readlines())


t1.close()

with open('Bilinili.jpg', 'rb') as r:
    with open('Bilinili_copy.jpg', 'wb') as w:
        w.write(r.read())

# with在不是该文件后将其自动关闭，文件.close()也可以关闭

with open(file_path2, 'r', encoding="utf-8") as operate_file:
    # 将文件的每行内容存储在列表中，readlines()读取文件每行将其存储在列表中
    lines = operate_file.readlines()
    n = 0
    for content_line in operate_file:
        n += 1
        print('This is the', n, 'line: ', end='')
        print(content_line.rstrip())

    # read()方法读文件是会在结尾返回一个空字符串，会导致文件多一个空行
    # content = operate_file.read()
    # print(content)
    # 按行读取文件内容
print(lines[:6])
for line in lines:
    print(line.rstrip())

# 文件中写入数据 w，会将原来的文本全部覆盖掉，只能写入字符串，不能直接写入整形数据
with open(file_path2, 'w') as operate_file:
    operate_file.write('this is a ceshi\n')
    operate_file.write('this is a ceshi again\n')

# 文件中添加内容 a，仍然使用write写入内容
with open(file_path2, 'a') as operate_file:
    new_content = input('please input new content: ')
    operate_file.write('add new content\n')
    operate_file.write('add new content\n')
    operate_file.write(new_content + '\n')








