#coding='utf-8'
from tkinter import *
from tkinter import messagebox
'''
其他大型GUI库
# import wxPython
# import PyQt
'''

root = Tk()
root.title('GUI编程')
# 设置窗口的宽高 .geometry('wXh±x±y') ±x：距离左边+/右边- 距离
root.geometry('500x300+800+300')

'''widget组键'''

'''Button'''
# Button(窗口x) 窗口x中添加一个按钮
btn01 = Button(root)
# 设置按钮内容
btn01['text'] = '屠龙宝刀点击就送!!!'

'''Label'''
# Label() 添加标签，标签可以填写字符/图片，给内容设置字体，大小font=(fontname, size)，以及前景色fg/背景色bg，
label01 = Label(root, text='this is Label', width=20, font=('黑体', 30), bg='black', fg='white')

# 将图片放入Label中
# 此处需要声明photo为全局变量，否则不会显示图片
# 加载图片只支持gif格式，一般直接修改图片后缀名，并不能修改格式
global photo
photo = PhotoImage(file=r'H:\PythonWorkSpace\PythonCode\images\Bilibili.gif')

label02 = Label(root, image=photo)

# 将组建布局到容器中
btn01.pack()
label01.pack()
label02.pack()


def knife(e):
    messagebox.showinfo('Message', 'songdao')
    print('送你屠龙宝刀')


# 将按钮绑定到事件
btn01.bind('<Button-1>', knife)

# 始终循环窗口，刷新事件
root.mainloop()


# 登录界面
def login():

    # 创建一个主窗口
    bankClient = Tk()  # from tkinter import *
    # 设置标题
    bankClient.title("CMBK")
    # 主窗口大小
    bankClient.geometry('750x500+800+300')
    # 设置窗口背景
    canvas = Canvas(bankClient, height=500, width=750)
    imagefile = PhotoImage(
        file=r'H:\PythonWorkSpace\LearnPythonBaseCode\BasePrictice\ClassTest\sky.gif')
    canvas.create_image(0, 0, anchor='nw', image=imagefile)

    # text 代表组件内容， width代表组建宽度， font 代表组建内容的字体，fg代表前景色，可以修改内容字体的颜色，bg代表组建的背景色
    labeUser = Label(bankClient, text='账号', width=4,
                     font=('黑体', 13))  # , bg='black', fg='white')

    labePassword = Label(bankClient, text='密码', width=4,
                         font=('黑体', 13))  # , bg='black', fg='white')

    # 输入框
    var_usr_name = StringVar()
    entryuser = Entry(bankClient, textvariable=var_usr_name)

    var_password = StringVar()
    entrypassword = Entry(bankClient, textvariable=var_password, show='*')

    btnlogin = Button(bankClient, text='登陆', width=4, font=('黑体', 13),
                      command=login_user)
    btncreat_user = Button(bankClient, text='开户', width=4, font=('黑体', 13),
                           command=creat_user)

    # 绘制背景
    canvas.pack(side='top')
    # canvas.place(x=0, y=0)

    '''place显示小组件widget'''
    # 绘制标签第一种方法使用place精确定位
    labeUser.place(x=100, y=50)
    labePassword.place(x=100, y=100)
    entryuser.place(x=140, y=50)
    entrypassword.place(x=140, y=100)

    '''pack显示小组件widget'''
    # 第二种方法使用pack()按照默认位置定位
    # 同时pack要比place优先级高
    # labeUser.pack()
    # labePassword.pack()

    # 绘制按钮
    btnlogin.place(x=380, y=140)
    btncreat_user.place(x=380, y=180)

    bankClient.mainloop()

