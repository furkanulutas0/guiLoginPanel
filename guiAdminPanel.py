from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import guiAdminFuncs


import time

def regBtn():
    registerBtn = Button(frameLogin, text='Register', font='Calbri 11 bold', padx=10, pady=10)
    registerBtn.place(relx=0.11, rely=0.65, relwidth=0.30, relheight=0.05)
    registerBtn.config(command=guiAdminFuncs.plsReg)

def authGet():
    username = usernameEntry.get()
    password = passEntry.get()
    if username == 'Furkan' or username == 'Muhammed':
        if password == '123':
            logMsg.config(foreground='green')
            logMsg.config(text='Giriş Başarılı')
            print('LOG: {} user giriş yaptı.'.format(username))
            messagebox.showinfo("Login Successfull", "Welcome")
        else:
            logMsg.config(foreground='red')
            logMsg.config(text='Password hatalı!')
            print('LOG: {} user force login.'.format(username))
    else:
        logMsg.config(foreground='red')
        logMsg.config(text='User not found')
        regBtn()
        print('LOG: Kayıtsız kullanıcı giriş denemesi.')
    usernameEntry.delete(0, END)
    passEntry.delete(0, END)


window = Tk()
window.title("MF Society Admin Panel")
window.geometry("600x800")

mainCanvas = Canvas(window, height=600, width=600 )
mainCanvas.pack()

frameBG = Frame(window, bg='#3c3f41')
frameBG.place(relx=0, rely=0, relwidth=1, relheight=1 )

border_clr = Frame(frameBG, bg='#eff249')
border_clr.place(relx=0.199, rely=0.199, relwidth=0.6028, relheight=0.6028)
frameLogin = Frame(frameBG, bg='#313335')
frameLogin.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

usernameFrame = Frame(frameLogin, bg='white')
usernameFrame.place(relx=0.1, rely=0.5, relwidth=0.797, relheight=0.05)

passFrame = Frame(frameLogin, bg='white')
passFrame.place(relx=0.1, rely=0.57, relwidth=0.797, relheight=0.05)

usernameLabel = Label(usernameFrame, text='Username', bg='white', font='trebuchetms 11 bold ')
usernameLabel.pack(side=LEFT)

usernameEntry = Entry(usernameFrame, bd=2, font='Calbri 8 bold')
usernameEntry.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

passLabel = Label(passFrame, text='Password', bg='white', font='trebuchetms 11 bold ')
passLabel.pack(side=LEFT)

passEntry = Entry(passFrame, bd=2, font='Calbri 8 bold')
passEntry.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

loginBtn = Button(frameLogin, text='Login', font='Calbri 11 bold', padx=10, pady=10, command= authGet)
loginBtn.place(relx=0.44, rely=0.65, relwidth=0.35, relheight=0.05)


logMsg = Label(frameBG, text='', bg='#313335', font='Calbri 10 bold', foreground='red')
logMsg.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.05)

image1 = Image.open("mf.png")
image2 = ImageTk.PhotoImage(image1)

labelimg= Label(image=image2,border=0, bg='#313335', justify=CENTER)
labelimg.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.2)



window.mainloop()
