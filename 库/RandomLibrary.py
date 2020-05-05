import random
# from time import perf_counter
#
# # 设置种子，保证随机数可以复现，没有设置种子就以系统时间为准
# random.seed()
# # 生成（0，1）之间的随机浮点数
# random.random()
#
# print(random.random()*10)
# # 生成a到b的随机整数random.randint(a, b)
# print(random.randint(1, 10))
# # 生成a到b，步长为n的随机整数random.randint(a, b, n)
# print(random.randrange(1, 10, 3))
# # 生成一个K比特长的随机整数random.getrandbits(10)
# print(random.getrandbits(10))
# # 生成（a,b）的随机小数random.uniform(10, 100))
# print(random.uniform(10, 100))
# # 从序列中选取一个数random.choice(seq)
# s = [1, 3, 10, 100, 90]
# print(random.choice(s))
# # 将序列中的元素随机排列，并返回打乱后的序列random.shuffle(seq)
# random.shuffle(s)
# print(s)
#
# darts = 1000 * 100
# hits = 1.0
# start = perf_counter()
# for i in range(1, darts+1):
#     x, y = random.random(), random.random()
#     dist = pow(x ** 2 + y ** 2, 0.5)
#     if dist <= 1.0:
#         hits += 1
# pi = 4 * (hits/darts)
# print("Pi的值是：{}".format(pi))
# print("计算耗时：{:.5f}s".format(perf_counter() - start))
# for i in range(1000, 10000):
#     number_copy = i
#     Sum = 0
#     while i >= 1:
#         j = i % 10
#         Sum += j ** 4
#         i //= 10
#     if number_copy == Sum:
#         print(number_copy)


# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# sum0 = 0
# for i in range(2, 100):
#     if is_prime(i):
#         sum0 += i
# print(sum0)


def genpwd(length):
    a = 10**(length-1)
    b = 10**length - 1
    return "{}".format(random.randint(a, b))


length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))


def prime(m):
    isprime = True
    for i in range(2, m):
        if m % i == 0:
            isprime = False
            break
    return isprime


n = int(eval(input()))
print(n)
count = 5
while count > 0:
    if prime(n):
        if count > 1:
            print(n, end=",")
        else:
            print(n, end="")
        count -= 1
    n += 1


