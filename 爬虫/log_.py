# 导入tkinter模块
import tkinter as tk

# 创建tkinter窗口
root = tk.Tk()
root.title('登录界面')
root.geometry('300x200')

# 定义用户名和密码变量（StringVar类型）
username = tk.StringVar()
password = tk.StringVar()

# 创建用户名和密码输入框
username_label = tk.Label(root, text='用户名：')
username_label.pack()
username_entry = tk.Entry(root, textvariable=username)
username_entry.pack()

password_label = tk.Label(root, text='密  码：')
password_label.pack()
password_entry = tk.Entry(root, textvariable=password, show='*')
password_entry.pack()


# 定义登录按钮的回调函数
def login():
    if username.get() == 'admin' and password.get() == '123456':
        tk.messagebox.showinfo(title='登录成功', message='欢迎您！')
    else:
        tk.messagebox.showerror(title='登录失败', message='用户名或密码错误！')


# 创建登录按钮
login_button = tk.Button(root, text='登录', command=login)
login_button.pack()

# 进入消息循环
root.mainloop()