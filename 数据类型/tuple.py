import sys

# 元祖一旦生成，内部的元素值就不可以直接修改（例如tl[1]=1,是错误的），内部数据类型可不相同
# 但可以修改元祖变量的值，直接对元祖变量重新赋值即可，元祖可以嵌套元祖
print('这是空的元祖描述方法： ' + 'dimension1 = ()')
# 使用()初始化元祖
dimension = (20, 100, 200)
# 使用()初始化元祖
tl = ('20', '100', '200', ('300', "400"), 1)
print("tl", tl[-2][1])
for item in dimension:
    print(item, end=",")
print()
print(dimension[0])
print(dimension[1])
print(dimension[2])


# 修改元祖变量的值
dimension = (20, 30, 40, 50)
for item in dimension:
    print(item)
print(dimension[0])
print(dimension[1])
print(dimension[2])

# 元祖可以转换为列表
tuple_convert_list_ = list(dimension)
print(tuple_convert_list_)
# 元祖比列表占用内存小
print(sys.getsizeof(tuple_convert_list_))
# 列表转换为元祖
list_convert_tuple = tuple(tuple_convert_list_)
print(list_convert_tuple)
print(sys.getsizeof(list_convert_tuple))


