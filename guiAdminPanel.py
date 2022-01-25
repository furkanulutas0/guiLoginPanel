import string
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import socket
from datetime import datetime
import random
import guiAdminFuncs
an = datetime.now()
tarih = str(datetime.ctime(an)) # LOG SAAT

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name) # IP ADRESS

def sendEmail():
    global emailSent
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    sender_email = "mailadresiniz@gmail.com"
    receiver_email = f"{receiverEmail}"
    senderPassword = "mailsifreniz"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Şifre Sıfırlama Talebi!"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""Merhaba,\nSıfırlama talebini aldık; Şifreni sıfırlamak için kullanacağın güvenlik kodunu aşağıda bıraktık.\n\n{securityCode}\n"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, senderPassword)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    emailSent = True

def authGet():
    username = usernameEntry.get()
    password = passEntry.get()
    db = open("users.txt", "r")
    u = []
    p = []
    e = []
    for k in db:
        a, b, c = k.split("#")
        b = b.strip()
        c = c.strip()
        u.append(a)
        p.append(b)
        e.append(c)
    data = dict(zip(u, (zip(p, e))))
    if len(u) == 0:
        print("Databasede kayıtlı kullanıcı yok!")
        logMsg.config(text="Bir Hata Oluştu\nPROGRAMDAN ÇIKILIYOR...")
        messagebox.showerror('ERROR', "Database'de kayıtlı kullanıcı yok.\nAdminle iletişime geçin!\nPROGRAMDAN ÇIKILIYOR...")
        window.destroy()
    else:
        Loginned = False
        userFound = True
        passTrue = True
        for i in range(len(u)):
            if username == u[i]:
                if password == p[i]:
                    border_clr.config(bg='green')
                    logMsg.config(foreground='green')
                    logMsg.config(text='Giriş Başarılı')
                    messagebox.showinfo("Başarıyla Giriş Yapıldı", "{}, Welcome".format(username))
                    Loginned = True
                    break
                elif password == '':
                    border_clr.config(bg='#eff249')
                    logMsg.config(foreground='red')
                    logMsg.config(text='Password boş olur mu hiç?')
                    passTrue = False
                    break
                else:
                    border_clr.config(bg='red')
                    logMsg.config(foreground='red')
                    logMsg.config(text='Şifre Hatalı!')
                    passEntry.delete(0, END)
                    passTrue = False
                    break
            elif username == '':
                border_clr.config(bg='#eff249')
                logMsg.config(foreground='red')
                logMsg.config(text='Kullanıcı adı boş olur mu hiç?')
                break
            else:
                border_clr.config(bg='red')
                logMsg.config(foreground='red')
                logMsg.config(text='Kullanıcı Adı Hatalı')
                usernameEntry.delete(0, END)
                userFound = False

            i + 1

        if Loginned == True:
            log = open('log.txt', 'a')
            log.write(f'LoginLOG: [{tarih}] {username} giriş yaptı LOGCODExS0\n')
            log.close()
            print(f'LoginLOG: [{tarih}] {username} giriş yaptı LOGCODExS0')
        elif passTrue == False:
            log = open('log.txt', 'a')
            log.write(f'LoginLOG: [{tarih}] {username} şifreyi hatalı girdi. Girilen şifre: {password}, Doğru şifre: LOGCODExP1\n')
            log.close()
            print(f'LoginLOG: [{tarih}] {username} şifreyi hatalı girdi. Girilen şifre: {password}, Doğru şifre: LOGCODExP1 ')
        elif userFound == False:
            log = open('log.txt', 'a')
            log.write(f'LoginLOG:[{tarih}] [{host_ip}] Kayıtsız kullanıcı adı girildi. LOGCODExU1\n')
            log.close()
            print(f'LoginLOG:[{tarih}] [{host_ip}] Kayıtsız kullanıcı adı girildi. LOGCODExU1')

def regAuth(): # REGİSTER MODULE
    global registerName
    global regPass1
    global regPass2
    global regEmail
    registerName = usernameEntry.get()
    regPass1 = passEntryR1.get()
    regPass2 = passEntryR2.get()
    regEmail = emailEntry.get()

    db = open("users.txt", 'r')
    uR = []
    pR = []
    eR = []
    for q in db:
        a, b, c = q.split("#")
        b = b.strip()
        c = c.strip()
        uR.append(a)
        pR.append(b)
        eR.append(c)
    data = dict(zip(uR,(zip(pR,eR))))
    if regPass1 != regPass2:
        log = open('log.txt', 'a')
        log.write(f"RegisterLOG:[{tarih}] [{host_ip}] Girilen şifreler uyuşmadı. #REGCODExR0\n")
        log.close()
        print(f"RegisterLOG:[{tarih}] [{host_ip}] Girilen şifreler uyuşmadı. #REGCODExR0")
        logMsgR.config(foreground='red')
        logMsgR.config(text='Şifreler uyuşmadı')
    else:
        if len(regPass1) < 6:
            log = open('log.txt', 'a')
            log.write(f"RegisterLOG:[{tarih}] [{host_ip}] Şifre 6 karakterden daha az. #REGCODExR1\n")
            log.close()
            print(f"RegisterLOG:[{tarih}] [{host_ip}] Şifre 6 karakterden daha az. #REGCODExR1")
            logMsgR.config(foreground='red')
            logMsgR.config(text='Şifre 6 karakterden az\nolamaz!')
            passEntryR1.delete(0, END)
            passEntryR2.delete(0, END)
        elif registerName in uR:
            log = open('log.txt', 'a')
            log.write(f"RegisterLOG:[{tarih}] [{host_ip}] Girilen kullanıcı adı zaten mevcut. #REGCODExR2\n")
            log.close()
            print(f"RegisterLOG:[{tarih}] [{host_ip}] Girilen kullanıcı adı zaten mevcut. #REGCODExR2")
            logMsgR.config(foreground='red')
            logMsgR.config(text='Bu kullanıcı zaten mevcut!')
            usernameEntry.delete(0, END)
        elif regEmail in eR:
            log = open('log.txt', 'a')
            log.write(f"RegisterLOG:[{tarih}] [{host_ip}] Girilen mail adresi zaten kullanımda #REGCODExR3\n")
            log.close()
            print(f"RegisterLOG:[{tarih}] [{host_ip}] Girilen mail adresi zaten kullanımda #REGCODExR3")
            logMsgR.config(foreground='red')
            logMsgR.config(text='Mail adresi zaten kullanımda!')
            emailEntry.delete(0, END)
        else:
            log = open('log.txt', 'a')
            log.write(f"RegisterLOG:[{tarih}] [{host_ip}], ({registerName}) adıyla kayıt oldu. #REGCODExS0\n")
            log.close()
            print(f"RegisterLOG:[{tarih}] [{host_ip}], ({registerName}) adıyla kayıt oldu. #REGCODExS0")
            db = open('users.txt', 'a')
            db.write(registerName+"#"+regPass1+"#"+regEmail+"\n")
            db.close()
            messagebox.showinfo('Kayıt Olundu', f'Başarıyla Kayıt Oldunuz.\nKullanıcı adınız: {registerName}\nŞifreniz: {regPass1}')
            register.destroy()
            loginScreen()

def forgotBtn():
    global securityCode
    global receiverEmail
    db = open("users.txt", "r")
    u = []
    p = []
    e = []
    for k in db:
        a, b, c = k.split("#")
        b = b.strip()
        c = c.strip()
        u.append(a)
        p.append(b)
        e.append(c)
    data = dict(zip(u, (zip(p, e))))
    receiverEmail = emailEntryF.get()
    fgtUsername = usernameEntryF.get()

    if receiverEmail in e and fgtUsername in u:
        pin = random.randint(99999,999999)
        letter1 = random.choice(string.ascii_letters)
        letter2 = random.choice(string.ascii_letters)
        letter3 = random.choice(string.ascii_letters)
        securityCode = letter1+str(pin)+letter2+letter3
        print(securityCode)
        sendEmail()
        if emailSent == True:
            reset.destroy()
            passResetAuth()
        else:
            print("Bir hata oluştu.")
    else:
        print("Bulunamadı")

def resetBtn():
    resetPassword1 = resPass1Entry.get()
    resetPassword2 = resPass2Entry.get()
    db = open("users.txt", "r")
    u = []
    p = []
    e = []
    for k in db:
        a, b, c = k.split("#")
        b = b.strip()
        c = c.strip()
        u.append(a)
        p.append(b)
        e.append(c)
    if securityCode == codeEntry.get():
        if resetPassword1 == resetPassword2:
            if usernameEntryF.get() in db:
                open('users.txt', '')


#EKRAN FONKSİYONLARI V

def registerScreen():  # REGISTER SCREEN MODULE
    global usernameEntry
    global passEntryR1
    global passEntryR2
    global emailEntry
    global logMsgR
    global RegBtn
    global register
    register = Tk()
    register.title("MF Society Register")
    register.geometry("600x800")
    mainCanvas = Canvas(register, height=600, width=600 )
    mainCanvas.pack()

    frameBGr = Frame(register, bg='#3c3f41')
    frameBGr.place(relx=0, rely=0, relwidth=1, relheight=1 )

    border_clr = Frame(frameBGr, bg='#eff249')
    border_clr.place(relx=0.199, rely=0.199, relwidth=0.6028, relheight=0.6028)

    frameReg = Frame(frameBGr, bg='#313335')
    frameReg.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

    usernameFrameR = Frame(frameReg, bg='white')
    usernameFrameR.place(relx=0.1, rely=0.4, relwidth=0.797, relheight=0.05)

    passFrameR = Frame(frameReg, bg='white')
    passFrameR.place(relx=0.1, rely=0.47, relwidth=0.797, relheight=0.05)

    passFrame2R = Frame(frameReg, bg='white')
    passFrame2R.place(relx=0.1, rely=0.54, relwidth=0.797, relheight=0.05)

    emailFrame = Frame(frameReg, bg='white')
    emailFrame.place(relx=0.1, rely=0.61, relwidth=0.797, relheight=0.05)

    usernameLabelR = Label(usernameFrameR, text='Username', bg='white', font='trebuchetms 11 bold ')
    usernameLabelR.pack(side=LEFT)

    usernameEntry = Entry(usernameFrameR, bd=2, font='Calbri 8 bold')
    usernameEntry.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

    passLabelR1 = Label(passFrameR, text='Password', bg='white', font='trebuchetms 11 bold ')
    passLabelR1.pack(side=LEFT)

    passEntryR1 = Entry(passFrameR,show='*', bd=2, font='Calbri 8 bold')
    passEntryR1.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

    passLabelR2 = Label(passFrame2R, text='Pass Again', bg='white', font='trebuchetms 11 bold ')
    passLabelR2.pack(side=LEFT)

    passEntryR2 = Entry(passFrame2R,show='*', bd=2, font='Calbri 8 bold')
    passEntryR2.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

    emailLabel = Label(emailFrame, text='e-Mail', bg='white', font='trebuchetms 11 bold')
    emailLabel.pack(side=LEFT)

    emailEntry = Entry(emailFrame, bd=2, font='Calbri 8 bold')
    emailEntry.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

    RegBtn = Button(frameReg, text='Register', font='Calbri 11 bold', padx=10, pady=10, command=lambda:(regAuth()))
    RegBtn.place(relx=0.548, rely=0.68, relwidth=0.35, relheight=0.05)

    logMsgR = Label(frameBGr, text='', bg='#313335', font='Calbri 10 bold', foreground='red')
    logMsgR.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.05)

def loginScreen():
    global usernameEntry
    global passEntry
    global logMsg
    global window
    global border_clr
    window = Tk()
    window.title("MF Society Admin Panel")
    window.geometry("600x800")

    mainCanvas = Canvas(window, height=600, width=600)
    mainCanvas.pack()

    frameBG = Frame(window, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

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

    passEntry = Entry(passFrame, bd=2, font='Calbri 12 bold', show='*')
    passEntry.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

    loginBtn = Button(frameLogin, text='Login', font='Calbri 11 bold', padx=10, pady=10, command=authGet)
    loginBtn.place(relx=0.41, rely=0.65, relwidth=0.35, relheight=0.05)

    registerBtn = Button(frameLogin, text='Register', font='Calbri 11 bold', padx=10, pady=10, command=lambda: [registerScreen(), window.destroy()])
    registerBtn.place(relx=0.10, rely=0.65, relwidth=0.30, relheight=0.05)

    logMsg = Label(frameBG, text='', bg='#313335', font='Calbri 10 bold', foreground='red')
    logMsg.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.05)

    image1 = Image.open("mf.png")
    image2 = ImageTk.PhotoImage(image1)

    labelimg = Label(image=image2, border=0, bg='#313335', justify=CENTER)
    labelimg.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.2)

    forgotPassBtn = Button(frameLogin, text='?', font='Calbri 12 bold', padx=10, pady=10, command=lambda :[passReset(), window.destroy()])
    forgotPassBtn.place(relx=0.77, rely=0.65, relwidth=0.128, relheight=0.05)

    window.mainloop()

def passReset():
    global reset
    global emailEntryF
    global usernameEntryF
    reset = Tk()
    reset.title("MF Password Reset Panel")
    reset.geometry("600x800")

    mainCanvas = Canvas(reset, height=600, width=600)
    mainCanvas.pack()

    frameBG = Frame(reset, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    border_clr = Frame(frameBG, bg='#eff249')
    border_clr.place(relx=0.199, rely=0.199, relwidth=0.6028, relheight=0.6028)
    frameLogin = Frame(frameBG, bg='#313335')
    frameLogin.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

    usernameFrame = Frame(frameLogin, bg='white')
    usernameFrame.place(relx=0.1, rely=0.5, relwidth=0.797, relheight=0.05)

    emailFrame = Frame(frameLogin, bg='white')
    emailFrame.place(relx=0.1, rely=0.57, relwidth=0.797, relheight=0.05)

    usernameLabel = Label(usernameFrame, text='Username', bg='white', font='trebuchetms 11 bold ')
    usernameLabel.pack(side=LEFT)

    usernameEntryF = Entry(usernameFrame, bd=2, font='Calbri 8 bold')
    usernameEntryF.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

    emailLabel = Label(emailFrame, text='eMail', bg='white', font='trebuchetms 11 bold ')
    emailLabel.pack(side=LEFT)

    emailEntryF = Entry(emailFrame, bd=2, font='Calbri 12 bold')
    emailEntryF.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.69)

    loginBtn = Button(frameLogin, text='Sumbit', font='Calbri 11 bold', padx=10, pady=10, command=forgotBtn)
    loginBtn.place(relx=0.41, rely=0.65, relwidth=0.35, relheight=0.05)

def passResetAuth():
    global resPass1Entry
    global resPass2Entry
    global codeEntry
    resetAuth = Tk()
    resetAuth.title("MF Password Reset Panel")
    resetAuth.geometry("600x800")

    mainCanvas = Canvas(resetAuth, height=600, width=600)
    mainCanvas.pack()

    frameBG = Frame(resetAuth, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    border_clr = Frame(frameBG, bg='#eff249')
    border_clr.place(relx=0.199, rely=0.199, relwidth=0.6028, relheight=0.6028)

    frameLogin = Frame(frameBG, bg='#313335')
    frameLogin.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

    resPass1 = Frame(frameLogin, bg='white')
    resPass1.place(relx=0.1, rely=0.5, relwidth=0.797, relheight=0.05)

    resPass2 = Frame(frameLogin, bg='white')
    resPass2.place(relx=0.1, rely=0.57, relwidth=0.797, relheight=0.05)

    codeFrame = Frame(frameLogin, bg='white')
    codeFrame.place(relx=0.1, rely=0.43, relwidth=0.797, relheight=0.05)

    resPass1Label = Label(resPass1, text='New Password', bg='white', font='trebuchetms 10 bold ')
    resPass1Label.pack(side=LEFT)

    resPass1Entry = Entry(resPass1, bd=2, font='Calbri 8 bold')
    resPass1Entry.place(relx=0.42, rely=0.1, relheight=0.8, relwidth=0.57)

    resPass2Label = Label(resPass2, text='Confrim Password', bg='white', font='trebuchetms 10 bold ')
    resPass2Label.pack(side=LEFT)

    resPass2Entry = Entry(resPass2, bd=2, font='Calbri 12 bold')
    resPass2Entry.place(relx=0.42, rely=0.1, relheight=0.8, relwidth=0.57)

    codeLabel = Label(codeFrame, text='Security Code', bg='white', font='Calbri 10 bold')
    codeLabel.pack(side=LEFT)

    codeEntry = Entry(codeFrame, bd=2, font='Calbri 12 bold')
    codeEntry.place(relx=0.42, rely=0.1, relheight=0.8, relwidth=0.57)

    sumbitBtn = Button(frameLogin, text='Sumbit', font='Calbri 11 bold', padx=10, pady=10)
    sumbitBtn.place(relx=0.41, rely=0.65, relwidth=0.35, relheight=0.05)

loginScreen()
