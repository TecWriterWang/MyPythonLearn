import sys
import os
import time

list2 = ['hello'] * 5
print(list2)

f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

# 占用较大空间，节约时间
f = [x ** 2 for x in range(1, 100)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
# 列表生成式，不占用空间，耗费时间
f = (x ** 2 for x in range(1, 100))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()


def dayeffort(effort_para):
    effort = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            effort = effort * 0.99
        else:            effort = effort * (1 + effort_para)
    return effort


effort_para1 = 0.01
while dayeffort(effort_para1) < 37.78:
    effort_para1 += 0.001

print("每天至少需要努力: {:.3f}".format(effort_para1))
