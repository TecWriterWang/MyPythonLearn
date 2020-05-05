from functools import reduce

# lambda函数 是一个匿名函数，没有函数名，lambda返回值就是函数名,它是函数的紧凑形式
# 一般格式 返回值 = lambda 参数：表达式,意思就是对给定的参数，进行表达式的计算，并将结果返回

f = lambda x, y: x + y
print(f(1, 5))
# map(函数， 可迭代序列对象)，把函数作用于序列对象的每一个元素
a = list(map(abs, [-1, -2, -3]))
print(a)

c = list(map(lambda x: x % 2, range(10)))
print('zheshi%s:' % c)
d = list(filter(lambda x: x % 2, range(10)))
print('zheshid%s' % d)


# reduce(函数，序列对象)把函数(函数必须有两个参数)的结果与序列对象的下一个元素作累积运算，适用于求和,使用时需要导入
def add(x, y):
    return x + y


b = reduce(add, [-1, -2, 3, 4])
print(b)


# 将字符串转化为整数。使用map()和reduce()
def add1(x, y):
    return x*10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


number = reduce(add1, map(char2num, '12345'))
print(number)


# filter(函数， 序列对象)，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1


a = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 递归法

# 汉罗塔 2^n -1
# count = 0
#
#
# def hanio(n, src, goal, mid):
#     global count
#     if n == 1:
#         print("{}:{}->{}".format(1, src, goal))
#         count += 1
#     else:
#         hanio(n-1, src, mid, goal)
#         print("{}:{}->{}".format(n, src, goal))
#         count += 1
#         hanio(n-1, mid, goal, src)
#
#
# hanio(10, 'A', 'B', 'C')
# print(count)
#
#
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
#
#
# print(fact(2))


def rvs(s):
    # 反转字符串

    if s == '':
        return s
    else:
        return rvs(s[1:])+s[0]


print(rvs("asd"))

# 全局变量和局部变量（函数内部），可使用global声明全局变量


def func_one(username, age=11):
    print("Hello!!! " + username.title() + ",你年龄是：" + str(age))
    print("Hello!!! " + username.rstrip())
    print("Hello!!! " + username.lstrip())
    print("Hello!!! " + username.strip())


func_one(username=" wh ")


def make_shirt(size='L', logo='I love Python', *para, **para_one):
    if not (para or para_one):
        print("This shirt size is " + size + ", and logo is " + logo)
    elif para and not para_one:
        print('任意数量的参数，其实就是将参数存储在元祖中 ', para)
    elif para and para_one:
        print('任意数量关键字参数，就是将参数键值对存储在字典中 ', para_one)


# 位置实参数
make_shirt('Small', 'NIKE')
# 关键字参数
make_shirt('Small', logo='NIKE')
# 默认参数
make_shirt()
make_shirt('M')
make_shirt(logo='Nike')
# 任意数量参数*para
make_shirt('Small', 'NIKE', '1', '2')
# 任意数量关键字参数**para
make_shirt('Small', 'NIKE', '1', '2', para1='one', para2='two', para3='three')


def des_city(city_name, country='America'):
    city_address = '"' + city_name.title() + ", " + country.title() + '"'
    return city_address


des = des_city('xian', 'china')
print(des)
des_city('weston')


def dict_one(name1, album1, album_number='', city=''):
    person = {'name': name1, 'album': album1, 'album_number': album_number,
              'city': city}
    if album_number == '':
        person['album_number'] = 'adding'
    if city == '':
        person['city'] = 'xian'
    return person


while True:
    name = input('please input the name:')
    if name == 'q':
        break
    album = input('please input the album:')
    if album == 'q':
        break
    person_one = dict_one(name, album, 1000)
    print(person_one)


# 传递列表
def modify_users(users, modify_user_item):
    print("this list isn't modify :", users)
    while users:
        current_item = users.pop(0)
        print('current item is ', current_item)
        print('The rest elements of list', users)
        modify_user_item.append(current_item)


def print_user(modify_user_item):
    print(modify_user_item)


username = ['wh', 'dd', 'zz']
modify_users_item = []
# 使用切片可以保证原始列表仍然可用
modify_users(username[:], modify_users_item)
print("this has modified ", username)
print_user(modify_users_item)

if __name__ == "__main__":
    print(1)