# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 19:30
import json

dict_one = {'a': 14, 'b': 16,
            'c': 20}
a = ['sss', 20, 'www']


"""json.dumps(dict)将数据写入到文件中，保留数据的格式，若原来是字典，就以字典格式写入"""

with open('json.json', 'w+') as f:
    # 字典中增加键值对，直接使用 dict[key]=value
    # 字典中添加另一个字典update()
    dict_one.update({'eee': 3333, 'sss': 'ssss'})
    file1 = json.dumps(dict_one)
    f.write(file1)


"""json.load(文件内容)， 读取文件的数据，并保留数据格式"""
with open('json.json', 'r') as f1:

    file2 = f1.read()
    print('读取文件中的字典', json.loads(file2))