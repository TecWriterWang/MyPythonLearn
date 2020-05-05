#coding=utf-8
from tkinter import *
from tkinter import messagebox

'''GUI面向对象写法'''


# Frame也是一个组键
class Application(Frame):

    def __init__(self, master=None):
        # 使用super().__init__()方法调用父类的构造方法，将子类和父类关联起来，让子类包含父类的所有属性和方法，super代表父类的定义，而不是父类对象
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):

        # 此处需要声明photo为全局变量，否则不会显示图片,图片必须是gif格式
        global photo
        photo = PhotoImage(file="Bilibili.jpg")
        '''Label标签框'''
        # Label() 添加标签，标签可以填写字符/图片，给内容设置字体，
        # 大小font=(fontname, size)，以及前景色fg/背景色bg，
        self.label01 = Label(self, text='this is Label', width=20, height=1,
                             font=('黑体', 20), bg='blue', fg='white')
        self.label01.pack()

        # 添加换行文本
        self.label03 = Label(self,
                             text='this is wrapp ling\nplease notice\nthank you'
                             , borderwidth=5, relief='solid', justify='left')
        self.label03.pack()

        # '''将图片放入Label中'''
        # self.label02 = Label(self, image=photo)
        # self.label02.pack()

        """Button按钮"""
        # Button(窗口x) 窗口x中添加一个按钮
        self.btnquit = Button(root, text='退出', command=root.destroy,
        activeforeground='red',
                              # activebackground='green',background='blue', )
                              )
        self.btnquit.pack()

        self.btn01 = Button(root, text='START GAME',
                            # image=photo,
                            borderwidth=6, relief=SOLID, command=self.playgame)  # state=DISABLED
        self.btn01.pack()

        """登陆界面设计"""

        '''Entry 单行文本框'''

        self.labelAccount = Label(root, text='账户')
        self.labelAccount.pack()

        # 输入账户名，绑定到输入值
        varAccount = StringVar()
        self.entryAccount = Entry(root, textvariable=varAccount)
        self.entryAccount.pack()
        varAccount.set('admin')

        self.labelPassword = Label(root, text='密码')
        self.labelPassword.pack()

        # 输入密码，
        varPassword = StringVar()
        self.entryPassword = Entry(root, textvariable=varPassword, show='*')
        self.entryPassword.pack()

        self.btnSubmit = Button(root, text='确认', command=self.login)
        self.btnSubmit.pack()

        '''多行文本Text'''
        # 遇到文本框边界会自动换行
        Text(root, width=40, height=10, bg='gray').pack()

        '''单选按钮RadioButton'''
        # 通过value值来控制单选，pack展示时通过side设置对齐
        Radiobutton(root, text='单选1', value='M').pack(side='left')
        Radiobutton(root, text='单选2', value='F').pack(side='left')

        '''多选按钮CheckButton'''
        Checkbutton(root, text='多选1').pack(side='left')
        Checkbutton(root, text='多选1').pack(side='left')

        '''canvas画布'''
        Canvas(root, width=200, height=50, bg='green').pack(side='right')

        '''布局管理器 pack(垂直水平排列)， Grid(网格排列)， place(位置排列，使用像素同HTML) '''
        # Canvas(self, width=10, height=10, bg='green').grid(row=1, column=1)

    def playgame(self):
        messagebox.showinfo('游戏', "登陆成功，你可以玩游戏了")

    def login(self):
        username = self.entryAccount.get()
        password = self.entryPassword.get()
        print('Your Account is :'+username)
        print('Your Password is :'+password)
        print('Verifying your account and password,please Hold on')
        if username == 'wh' and password == '111':
            messagebox.showinfo('login', 'Login Successful')
            print('Login Successful')
        else:
            messagebox.showinfo('login', 'Please verify your account and password')

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800+300+300')
    root.title('Widget')
    # 实例化一个Application对象，并把放入到窗口中
    app = Application(master=root)
    root.mainloop()
