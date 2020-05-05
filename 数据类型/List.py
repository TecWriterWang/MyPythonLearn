import  sys
# 初始化一个从0到99到列表
# 打印列表时不能与其他任何字符使用+连接
a = list(range(0, 100))
print('这是空列表的描述方法: ' + 'a1 = []')
# 指定列表元素
b = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
c = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
d = ['admin', 'eric', 'wh', 'jy', 'dd']
# 新生成一个空列表，会在内存中开辟一个空间存放列表d1
d1 = []
# 此处将列表b赋给d2，并没有新生成一个列表，而是将d2指向列表b的内存地址，d2和b都指向同一个内存，
d2 = b
# 列表切片
b1 = b[:]
b1[0:10:2] = c[0:10:2]
print(b1)
# 两个列表相加，将c增加到b的后面
b += c
print(b)
# 复制列表
d *= 2
print(d)
# index(x)返回列表中出现x的下标位置，x不存在会报错，
print(c.index('1'))
# count(x)出现x的次数统计
print(c.count("2"))
# max() min()比较序列中的最大值最小值，当比较类型不相同时报错
print(max(c), min(c))


for exist in d:
    print(d)
    if d1:
        if exist == 'admin':
            print("Hello " + exist + ", please check the service status")
    else:
        print("Hello " + exist + ", welcome log into our website")

print('one' in b)
print('one' not in b)

# 列表增加元素
#  .append()在列表末尾添加元素
b.append('lucas')
b += [100, 200]
print('使用append在列表元素最后添加元素: ', end='')
print(b)
# .insert(i, x)在列表指定位置i插入元素x
b.insert(2, 'lucas one')
print("insert:", b)

#  .pop(i)删除列表指定位置i的元素
a = b.pop(1)
# 该删除的元素可以继续使用但不在该列表中
print(b)
print("pop", a)

# 4. 删除任意指定位置元素，下标-1表示最后一个元素。
del b[-1]
# 该删除的元素不能再继续使用，注意和pop语法区别    a = b.pop(1)
print(b)

# remove(x) 删除列表中第一次出现的x
b.remove('three')
print(b)

# 清除列表元素
b.clear()

# 初始化一个空列表
listA = []

# 遍历列表
for item in b:
    print(item, end='')
print()
for value in range(2, 10, 2):
    listA.append(value ** 2)
print(listA)

# 列表解析-将代码简写
list1 = [value for value in range(3, 30, 3)]
print(list1)

# 列表切片
# 操作列表n1至n2的元素.语法：list[n1:n2],n1和n2必须有一个出现
print(b[-3:])
for item in b[0:]:
    print(item + ' ', end='')
print()
# 使用切片复制现有列表
b1 = b[:]
print('这是列表切片的复制b1：', end='')
print(b1)
b.append('2')
b1.append('1')
print(b)
print(b1)
b2 = b1
print(b2)


# 列表排序
lists = list(range(11))
print(lists)
print('最小值是', min(lists))
print('最大值是', max(lists))
print('求和', sum(lists))
print(sorted(c, reverse=True))  # sorted 排序不影响原列表本身顺序
c.sort(reverse=True)  # sort 排序影响原列表本身顺序
print(c)
# b.reverse()  # 颠倒列表元素
print(b)
length = len(b)
print(length)


# 列表生成式，占用较大空间，节约时间，能使用for语法的对象都是可迭代的。
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
# 列表生成器，不占用空间，耗费时间，每次使用时使用next切换下一个元素。
# 生成器（generator）都是迭代器（Iterator），使用iter()函数将list，dict，str可以变成迭代器
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式，生成器不占用存储数据的空间
print(f)

# 求列表统计值


def get_number():
    number = input()
    nums = []
    while number != "":
        nums.append(eval(number))
        number = input()
    return nums


def get_average(nums1):
    ave = 0.0
    for item1 in nums1:
        ave += item1
    ave /= len(nums1)
    return ave


def get_mean(nums2, ave2):
    sbin = 0.0
    for item2 in nums2:
        sbin += (item2 - ave2) ** 2
    return pow(sbin/(len(nums2)-1), 0.5)


def get_mid(nums3):
    nums3 = sorted(nums3)
    length3 = len(nums3)
    if length3 % 2 == 0:
        mid3 = (nums3[length3//2 - 1] + nums3[length3//2 + 1])
    else:
        mid3 = nums3[length3//2]
    return mid3


nums = get_number()
ave = get_average(nums)
mean = get_mean(nums, ave)
mid = get_mid(nums)
print("求和是：{0}, 平均数是：{1:.2f}, 方差是：{2:.2f}, 中位数是：{3}"
      .format(sum(nums), ave, mean, mid))
