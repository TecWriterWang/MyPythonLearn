

class Salary:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("输入有误")


sl = Salary('x', 20000)
print(sl.salary)
# 在类中传入参数时必须使用方法，但是使用装饰器后可以直接把它当成属性使用
sl.salary = 10000
print(sl.salary)
