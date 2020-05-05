import json
# import 导入python专有模块时，不能出现和模块同名py文件

number = [2, 3, 4, 5, 6, 7, 8]
test = "This is a test"
# 当文件不存在时，通过open w 操作可以自动创建一个该文件
filename = 'File_Test/test.json'
# with open(filename, 'w') as operate_json:
# #     # 数据写入到json， json.dump(写入的数据, 文件路径)
# #     json.dump(number, operate_json)
# #
# # with open(filename) as operate_json:
# #     # 读取json内容到指定文件, json.load(文件路径)
# #     numbers = json.load(operate_json)
# # print(numbers)


def greet_user():
    try:
        with open(filename, 'r') as operate_json:
            username = json.load(operate_json)
    except FileNotFoundError:
        print('No file be founded, you can creat this file by writing next.')
        name = input('Please input your name! ')
        with open(filename, 'w') as operate_json:
            json.dump(name, operate_json)
            print("We had remembered your name!")
    else:
        print("Hello", username, ", Welcome back!")


# 重构上述代码，让其不在同时写入和存储，将两个存储和写入分开
def stored_user():
    try:
        with open(filename, 'r') as operate_file:
            content = json.load(operate_file)
    except FileNotFoundError:
        return None
    else:
        return content


def new_user():
    name = input('Please input your name! ')
    with open(filename, 'w') as operate_file:
        json.dump(name, operate_file)
    return name


def greet_user():
    username = stored_user()
    if username:
        print("Please confirm your name, and input your name again")
        result = input(username + "is right?yes/no\n")
        # 用户验证
        if result == 'yes':
            print("Hello,", username)
        else:
            print("You are new user!")
            username = new_user()
            print(username, ", We had remembered your name!")

    else:
        username = new_user()
        print(username, ", We had remembered your name!")


greet_user()
