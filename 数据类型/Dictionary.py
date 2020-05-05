
scores = {'骆昊': 11, '白元芳': 78, '狄仁杰': 82}
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典进行遍历(遍历的其实是键再通过键取对应的值)
for elem in scores:
    print('%s\t--->\t%d' % (elem, scores[elem]))
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85, 武则天=99)
print(scores)
# 返回字典的长度，长度是指键值对对个数
print(len(scores))
# 判断是A键是否在字典B中
if '武则天' in scores:
    print(scores['武则天'])
# get(key, default) 键key存在返回key对应的值，不在则返回默认值
print(scores.get('武则天', -1))
# .pop(key, default)
# key在字典中，则从字典中弹出键key的值，弹出的值可以使用，key从字典中移除，弹出指定健key不存在则返回默认值default
print(scores.pop('骆昊', "不存在"))
print(scores)
# .popitem()从字典中随机获取一组键值对，以元组形式返回
print(scores.popitem())
print(scores)
# 清空字典
scores.clear()
print(scores)


# Dictionary
dictionary = {}
print('这是空的字典' + 'dictionary = {}')
dictionary['color'] = 'yellow'
dictionary['point'] = 9
print(dictionary['color'])
print(dictionary['point'])
dictionary['x_position'] = 90
dictionary['y_position'] = 0
print(dictionary)

# alien test
print('这是外星人字典！！！')
dictionary_alien = {'x_position': 0, 'y_position': 25,
                    'speed': 'fast', 'size': 'big'}
print('Origination x_position is: ' + str(dictionary_alien['x_position']))
if dictionary_alien['size'] == 'big'\
        or dictionary_alien['speed'] == 'slow':
    x_increment = 1
elif dictionary_alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 8
    x_increment = 10
    x_increment = 9
dictionary_alien['x_position'] = x_increment + dictionary_alien['x_position']
print('New x_position is: ' + str(dictionary_alien['x_position']))
print(dictionary_alien)
del dictionary_alien['size']
print(dictionary_alien)

print('这是练习！！！')
dictionary_family = {'first_name': 'wh', 'last_name': 'xx',
                     'age': '20', 'cityA': 'xian', 'cityB': 'xian'}
print(dictionary_family['first_name'] + ' ', end='')
print(dictionary_family['last_name'])
print(dictionary_family['age'])
print(dictionary_family['cityA'])
print(dictionary_family['cityB'])

# 遍历字典
# 1.返回字典的所有键-值对，使用 字典.items()
print('遍历键值对')
# items()方法就是将 字典 转化为 元素是 由键值对组成的元祖 的列表，
# for循环有两个变量参数
# 将字典转换为列表
lista = list(dictionary_family.items())
# 对列表排序，默认从小到大，
lista.sort(key=lambda x: x[1], reverse=True)
print("打印键值对：", lista)
word, count = lista[1]
print("{} {}".format(word, count))
for item, value in dictionary_family.items():
    print("只打印键{}".format(item), end=",")
    print("\n只打印值{}".format(value), end=",")

# 2.遍历字典的所有键， 使用 字典.keys()
print('只遍历键')
# keys()方法实际上是将 字典的健 转化为列表
print(dictionary_family.keys())
for options in dictionary_family.keys():
    print(options.title())
for options in dictionary_family:
    print(options)

# 3.遍历字典中值
# values()方法实际上是将 字典的值 转化为列表
# set()表示集合，和列表类似，但是他的所有元素都是唯一的，
# 绝不重复元素使用大括号{}括起来
print(dictionary_family.values())
for options in dictionary_family.values():
    print(options)
print(set(dictionary_family.values()))
lists = ['1', '3', '2', '2']
print(set(lists))
print(list(range(30)))

# 列表+字典 互相嵌套
# 1.列表中嵌套字典-当列表元素有多个属性时使用此嵌套
aliens_origin = [
    {'x_position': 20, 'color': 'red', 'speed': 'lower', 'size': 'small'},
    {'x_position': 90, 'color': 'yellow', 'speed': 'lower',  'size': 'small'},
    {'x_position': 20, 'color': 'green', 'speed': 'fast', 'size': 'big'}
]
for alien in aliens_origin[:3]:
    if alien['speed'] == 'fast' or alien['size'] == 'small':
        move_speed = 3
    else:
        move_speed = 2
    alien['x_position'] = alien['x_position'] + move_speed
    print(alien)
# 2.字典中嵌套列表 - 当字典元素有多个选项时使用此嵌套
noodles = {'size': 'big',  'tasty': ['cong', 'suan', 'la'],
           'temp': ['hot', 'cool']}
for pz in noodles['tasty']:
    print(pz + ': ')
    if 'cong' in pz:
        print('\t我需要加葱！！！')
    elif 'suan' in pz:
        print('\t我需要加蒜！！！')
    else:
        print('\t不要加东西，原味！！！')

# 3.字典嵌套字典
city = {
    'nanjing':
        {'temp': 'normal', 'food': ['duck', 'bread']},
    'shanghai':
        {'temp': "don't normal", 'food': ['sweet', 'tea']}
}
for ct, live in city.items():
    print('\nWelcome to ', ct.title(), end='')
    print(', today temp is ', live['temp'], end='')
    for fd in live['food']:
        # if fd == 'duck' or 'bread':
        print('. You can tasty the follows food :', fd, end='')







