from collections import OrderedDict

# 类的访问限制
'''
__属性/方法__  属性/方法 前后都有两个_            代表类的特殊属性/方法 特殊变量是可以直接访问的

__属性/方法    属性/方法 前有两个_    代表类的私有属性/方法，
类外部不可直接访问，必须使用getter或setter才能修改/获取类属性。

类外部若要直接访问可以使用 实例._类名__属属性

_属性/方法     也表示私有属性/方法，但是可以从类外部访问。
当你看到这样的语法时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
'''


class Dog:
    """"这是注释"""
    # 这是实例属性
    size = 'small'

    # self代表实例, 一般内部创建实例时会先使用 __new__() 方法创建实例对象， __init__() 用于初始化实例对象属性
    def __init__(self, name, age):
        # 类属性
        self.name = name
        # 私有属性
        self.__age = age
    """析构方法一般不需要单独写，系统会自动处理"""
    # __del__()析构方法， 使用垃圾回收机制（当对象不在被调用时）销毁对象，使用（del 实例对象） 调用此方法
    # 一般都不需要写出这个方法，调用类时会自动运行垃圾回收
    def __del__(self):
        print('析构方法——销毁{}对象'.format(self))

    # __call__() 调用方法，直接使用 类() 就可以调用，类相当于函数
    def __call__(self, *args, **kwargs):
        print("直接调用类调用类-call", *args)

    # 实例的方法
    def sit(self):
        print(self.name.title(), 'is sitting!')

    def roll_over(self):
        print(self.name.title(), 'This dog is rolling over')
    # 类方法和静态方法中无法使用实例的属性以及方法
    @classmethod
    def print_classmethod(cls):
        print("这是类方法,直接可以使用类.方法()调用,类方法中不可调用实例的属性即方法")

    # 静态方法,就是与类无关的方法，但不属于实例方法
    @staticmethod
    def print_staticmethod():
        print("这是静态方法，直接可以使用类.方法()调用,类方法中不可调用实例的属性即方法")


# 调用类方法，直接使用类加方法
Dog.print_classmethod()
# 调用类的静态方法，直接使用类加方法
Dog.print_staticmethod()
# 类的实例
dog1 = Dog('xx', 10)
dog2 = Dog('xx', 10)
dog1.print_classmethod()
dog1.print_staticmethod()
dog1(100)

# 类外部使用类的私有属性或方法, 实例._类对象__属性
print(dog2._Dog__age)
# 使用del调用销毁方法，删除实例化对象，当对象不在使用时会自动销毁
del dog1
print("程序结束")


print(dir(object))  # 函数返回参数所有的方法和属性


# 继承
class AmericaDog(Dog):

    # 初始化子类实例
    def __init__(self, name, age, size):
        self.size = size
        # py3.0及以上
        # 子类继承父类的属性
        super().__init__(name, age)

    def sit(self):
        print('重写父类方法')

        # py2.7
        # super(AmericaDog, self).__init__()


dog_one = Dog('hanhan', 8)
print('The dog name is ', dog_one.name.title(), 'it has', dog_one._Dog__age)
dog_one.sit()
dog_two = AmericaDog('tiehanhan', 1, 'big')
print(
    'The dog name is', dog_two.name.title() + ', it has',
    dog_two._Dog__age, 'year old, it size is', dog_two.size)
# 查看类的继承内部层次对象
print(AmericaDog.mro())


class Restaurant:

    # _init_()初始化类，相当于java中new操作。
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 添加默认属性
        self.restaurant_price = 500
        self.number_served = 0

    def des_restaurant(self):
        return self.restaurant_name

    def open_restaurant(self):
        return self.cuisine_type

    def update_para(self, new_para, price):
        self.restaurant_name = new_para
        if price > 0:
            self.restaurant_price += price
        else:
            print('no have cheap')
        # return self.restaurant_name


restaurant_one = Restaurant('xinxin', '****')
# 直接修改类的属性值
restaurant_one.restaurant_name = 'beijing'
print(restaurant_one.des_restaurant())
print(restaurant_one.open_restaurant())
print('The restaurant price is ', restaurant_one.restaurant_price)
print('How many people cost the restaurant ', restaurant_one.number_served)

# 使用方法修改属性的值
restaurant_one.update_para('heibei', -10)
print(restaurant_one.des_restaurant())
print(restaurant_one.open_restaurant())


class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        user_name = self.first_name + self.last_name
        print("The user name is  ", user_name)

    def increment_login_attempts(self, number):
        self.login_attempts += number
        print('You have login number is', self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


class Privileges:

    def __init__(
            self, privileges=
            ['can add post', 'can delete post', 'can ban user']):

        self.privileges = privileges

    def show_privileges(self):
        for item in self.privileges:
            print(item)


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()


new_user = User('W', 'h')
new_user.describe_user()
new_user.increment_login_attempts(2)
new_user.increment_login_attempts(3)
new_user.increment_login_attempts(4)
print(new_user.reset_login_attempts())
new_user1 = Admin('X', 'Z')
new_user1.privileges.show_privileges()




