import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("400x500+450+50")
win.title("Login Form")
win.wm_iconbitmap(r"G:\icon\vscode.ico")

login_form = ttk.Label(win,text='Login Form',font='arial 20')
user_name = ttk.Label(win,text='User Name',font='arial 10')
user_name_entry = ttk.Entry(win)
user_passowrd = ttk.Label(win,text='User Passowrd',font='arial 10')
user_passowrd_entry = ttk.Entry(win)
submit = ttk.Button(win,text='SUBMIT')


login_form.pack()
user_name.pack()
user_name_entry.pack()
user_passowrd.pack()
user_passowrd_entry.pack()
submit.pack(pady=5)


win.mainloop()