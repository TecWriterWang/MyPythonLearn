import import_test
import Class

# 每个函数都是一个对象，每个函数对象都是有一个__doc__的属性
# 函数语句中，如果第一个表达式是一个string，这个函数的__doc__就是这个string，否则__doc__是None。
print(Class.__doc__)

print(import_test.__doc__)
print(import_test.add.__doc__)


# 工厂模式 就是将创建者和调用者分离


class CarFactory():

    def creat_car(self, brand):
        if brand == '奥迪':
            return Audi()
        if brand == '宝马':
            return BMW()
        if brand == '奔驰':
            return Benz()
        else:
            return '未知品牌，无法创建'


class Audi():
    pass


class BMW():
    pass


class Benz():
    pass


factory = CarFactory()
c1 = factory.creat_car('奥迪')
print(c1)


# 单例模式 一个类只允许创建一个是实例，如果同时创建类多个类，则这几个类都指向同一个实例
# 单例模式需要重写__new__()方法，以及对初始化方法作对应处理

class Singalation():

    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        """ 重写__new__()方法"""

        if cls.__obj is None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        # 判断创建对象数量
        if Singalation.__init_flag:
            print('init.......')
            self.name = name
            Singalation.__init_flag = False


a = Singalation(1)
b = Singalation(11)
print(a)
print(b)


