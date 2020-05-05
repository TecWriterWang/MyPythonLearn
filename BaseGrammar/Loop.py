# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:GitWang
# datetime:2019/8/6 22:53
# software: PyCharm

"""
for in 循环用于知道循环次数或者使用 迭代
不知道具体循环次数用while
"""

# 乘法表

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d * %d = %d" % (i, j, i*j), end='\t')
#     print()

# 最大公约数，最小公倍数

# x = int(input("i:"))
# y = int(input("j:"))
# if x > y:
#     x, y = y, x
# for n in range(x, 0, -1):
#     if (x % n == 0) and (y % n == 0):
#         print("%d和%d的最大公约数是%d" % (x, y, n))
#         print("%d和%d的最小公倍数是%d" % (x, y, x*y//n))
#     break


# 杨辉三角形

# n = int(input("n:"))
# for i in range(n):
#     for _ in range(i+1):
#         print("*", end='')
#     print()
# for i in range(n):
#     for _ in range(n):
#         if _ < n - i - 1:
#             print(" ", end='')
#         else:
#             print("*", end='')
#     print()
# for i in range(n):
#     for _ in range(n-i-1):
#         print(" ", end='')
#     for _ in range(2*i+1):
#         print("*", end='')
#     print()


# 水仙花数

# number = int(input("Please input the number(100=<number<1000):"))
# number_copy = number
# Sum = 0
# while number > 0:
#     j = number % 10
#     Sum += j*j*j
#     number //= 10
# if number_copy == Sum:
#     print("%d 是水仙花数。" % number_copy)
# else:
#     print("%d 不是水仙花数。" % number_copy)


# 完全数

# number = int(input("Please input the number(100=<number<1000):"))
# sum1 = 0
# # 检测某个数是不是完全数
# for i in range(1, number):
#     if number % i == 0:
#         sum1 += i
# if sum1 == number:
#     print("%d 是完数。" % number)
# else:
#     print("%d 不是完数。" % number)


# 输出number数以内的所有完全数

# number = int(input("Please input the number:"))
# a = list()
# for i in range(1, number):
#     sum2 = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum2 += j
#     if sum2 == i:
#         a.append(i)
# print(a)


# 百钱鸡

# for hen_male in range(100):
#     for hen_female in range(100-hen_male):
#         if hen_male*5 + hen_female*3 + (100-hen_male-hen_female)/3 == 100:
#             print("hen_male: %d 、 hen_female: %d 、hen_prototype: %d 。"
#                   % (hen_male, hen_female, 100-hen_male-hen_female))
#             print('公鸡{0}只，母鸡{1}只，雏鸡{2}只'
#                   .format(hen_male, hen_female, 100 - hen_male - hen_female))

# 斐波拉契数列
number = int(input("Please input the number:"))
a_list = []
a, b = 0, 1
for i in range(1, number):
    if i == a+b:
        a_list.append(i)
        a = b
        b = i

print(a_list)


def fib(n):
    x, y = 1, 1
    while y < n:
        print(x, end=' ')
        x, y = y, x + y


fib(number)  # 输出的是100以内的斐波那契数列


# 输入函数,默认输入的是字符串
# 一个字符串分两行输出 a += ""
a = "1111111111111111111111111111111111111111111111111111111111111111111111111"
a += "\n2222222222222222222"
print(a)
number = int(input())
while number <= 10:
    print(number)
    number += 1
print('Hello,' + a + '!')
unconfirmed_users = ['wh', 'cy', 'bb']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:" + current_user)
    confirmed_users.append(current_user)
print("All confirmed user:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 输入的值存入字典中
dict_one = {}
continue__ = True
while continue__:
    name = input()
    value = input()
    dict_one[name] = value
    repeat = input("continue? (yes / no) ")
    if repeat == 'no':
        continue__ = False
print(dict_one)
for name, value in dict_one.items():
    print(name + value)

