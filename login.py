import tkinter as tk
from tkinter import StringVar, ttk

win = tk.Tk()
win.geometry("400x500+450+50")
win.title("Login Form")
win.wm_iconbitmap(r"G:\icon\vscode.ico")

def submit(event=None):
    var1 = name_entry.get()
    var2 =passowrd_entry.get()
    if var1=='' or var2=='':
        print("pleas enter alphbat",var2,var1)
    else:
        with open('text.txt','a') as f:
            f.write(f'Name : {var1} And Passowrd : {var2} \n')
        f.close()
        name_entry.set('')
        passowrd_entry.set('')
 
login_form = ttk.Label(win,text='Login Form',font='arial 20')
user_name = ttk.Label(win,text='User Name',font='arial 10')
name_entry=StringVar()
user_name_entry = ttk.Entry(win,textvariable=name_entry)
user_name_entry.focus()
user_passowrd = ttk.Label(win,text='User Passowrd',font='arial 10')
passowrd_entry=StringVar()
user_passowrd_entry = ttk.Entry(win,textvariable=passowrd_entry)
submit = ttk.Button(win,text='SUBMIT',command=submit)

login_form.pack()
user_name.pack()
user_name_entry.pack()
user_passowrd.pack()
user_passowrd_entry.pack()
submit.pack(pady=5)


win.mainloop()