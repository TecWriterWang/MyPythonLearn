# 这是包
import math
import turtle

print("多个导入模块倒入到包中")
print(id(math))


# 这是包中的子包
def add():
    print(10)