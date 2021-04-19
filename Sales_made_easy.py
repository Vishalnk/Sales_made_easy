from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
import tkinter as tk
import mysql
from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
# import twilio
import random
from twilio.rest import Client

#code for sending OTP to registered number
def otps(otpp, phhno):
    account_sid = 'ACe0aeffa83a63021c8658c5820a5df82e'
    auth_token = '56144cb7d9411359eb409eef522ac8ab'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='your OTP:' + str(otpp),
        from_='+13345090288',
        to='+91' + str(phhno)
    )

#code for cutomers portal
def customer():
    root.withdraw()
    customer=Tk()
    customer.geometry('500x500+100+100')
    customer.title("Customer login")
    customer.config(bg="#00b3b3")
    title = Label(customer, text="Customer Login", width=15, background="#00b3b3", font=("bold", 25))
    title.place(x=130, y=33)
    username = Label(customer, text="USER NAME",background="#00b3b3",foreground="#b35900", compound=LEFT, font=10).place(x=100, y=120)
    uentry = Entry(customer)
    uentry.place(x=250, y=123)
    password = Label(customer, text="PASSWORD",background="#00b3b3",foreground="#b35900", compound=LEFT, font=10).place(x=100, y=160)
    passentry = Entry(customer, show="*")
    passentry.place(x=250, y=163)

    #Login function for customer to valididate the credentials
    def login():
        if uentry.get()=="" or passentry.get()=="":
            messagebox.showerror("Error","Enter necessary Credentials")
        else:
            dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999", database="project")
            cur = dbms.cursor()
            sql = "select * from customer where username=%s and password=%s"
            cur.execute(sql, (uentry.get(), passentry.get()))
            res = cur.fetchall()
            na="select username from customer where username=%s and password=%s"
            cur.execute(na, (uentry.get(), passentry.get()))
            nares = cur.fetchone()
            if res:
                for i in res:
                    uentry.delete(0,END)
                    passentry.delete(0,END)
                    messagebox.showinfo("Login", "Login successful")
                    customer.withdraw()
                    cuspage = Tk()
                    cuspage.geometry("730x430+0+0")
                    cuspage.config(background="#00b3b3")
                    cuspage.title("Customer portal")
                    wel = Label(cuspage,
                                text="Welcome back, "+nares[0]+ " !!!\nContinue shopping and"
                                " have a look at the new trend of mobiles :)",
                                foreground="#802b00", background="#00b3b3", font=("bold", 12))
                    wel.place(x=5, y=5)
                    pro = LabelFrame(cuspage, text="Shopping section", borderwidth=2, background="#b3b3ff",
                                     foreground="#ff0000", relief="solid")
                    pro.place(x=2, y=55, width=700, height=200)
                    col = ('NAME', 'BRAND', 'RAM', 'STORAGE', 'COLOUR', 'PRICE', 'DATE')
                    dis = ttk.Treeview(pro, height=5, show='headings', columns=col)
                    dis.column('NAME', width=100, anchor=CENTER)
                    dis.column('BRAND', width=100, anchor=CENTER)
                    dis.column('RAM', width=50, anchor=CENTER)
                    dis.column('STORAGE', width=50, anchor=CENTER)
                    dis.column('COLOUR', width=50, anchor=CENTER)
                    dis.column('PRICE', width=100, anchor=CENTER)
                    dis.column('DATE', width=100, anchor=CENTER)
                    dis.heading('NAME', text="NAME")
                    dis.heading('BRAND', text="BRAND")
                    dis.heading('RAM', text="RAM")
                    dis.heading('STORAGE', text="STORAGE")
                    dis.heading('COLOUR', text="COLOUR")
                    dis.heading('PRICE', text="PRICE")
                    dis.heading('DATE', text="DATE OF RELEASE")
                    dis.pack(side=TOP, fill=BOTH)

                    # Function to list all the lastest mobiles registered
                    def latest():
                        dis.delete(*dis.get_children())
                        dbms = mysql.connector.connect(host="localhost", user="root",
                        passwd="Josephite1999",database="project")
                        curu = dbms.cursor()
                        sql = "select * from mobile order by date DESC"
                        curu.execute(sql)
                        latestres = curu.fetchall()
                        for i in latestres:
                            dis.insert('', 'end', values=i)
                    latest = Button(pro, text="Latest", font=("bold", 13), command=latest)
                    latest.place(x=5, y=140)

                    # Function to list mobiles in increasing order of price
                    def price():
                        dbms = mysql.connector.connect(host="localhost", user="root",
                        passwd="Josephite1999",database="project")
                        curu = dbms.cursor()
                        dis.delete(*dis.get_children())
                        pricesql = "select * from mobile order by price ASC"
                        curu.execute(pricesql)
                        priceres = curu.fetchall()
                        for i in priceres:
                            dis.insert('', 'end', values=i)
                    price = Button(pro, text="Price:(low-high)", font=("bold", 13), command=price)
                    price.place(x=70, y=140)

                    # Function to list mobiles with RAM 4GB
                    def gb4():
                        dbms = mysql.connector.connect(host="localhost", user="root",
                        passwd="Josephite1999",database="project")
                        curu = dbms.cursor()
                        dis.delete(*dis.get_children())
                        gb4sql = "select * from mobile where ram=4"
                        curu.execute(gb4sql)
                        gb4res = curu.fetchall()
                        for i in gb4res:
                            dis.insert('', 'end', values=i)
                    gb4 = Button(pro, text="4GB RAM", font=("bold", 13), command=gb4)
                    gb4.place(x=210, y=140)

                    # Function to list mobiles with RAM 6GB
                    def gb6():
                        dbms = mysql.connector.connect(host="localhost", user="root",
                        passwd="Josephite1999",database="project")
                        curu = dbms.cursor()
                        dis.delete(*dis.get_children())
                        gb6sql = "select * from mobile where ram=6"
                        curu.execute(gb6sql)
                        gb6res = curu.fetchall()
                        for i in gb6res:
                            dis.insert('', 'end', values=i)
                    gb6 = Button(pro, text="6GB RAM", font=("bold", 13), command=gb6)
                    gb6.place(x=305, y=140)

                    # Function to recommend the most bought mobiles to the customer
                    def recommend():
                        dbms = mysql.connector.connect(host="localhost", user="root"
                        , passwd="Josephite1999",database="project")
                        curu = dbms.cursor()
                        dis.delete(*dis.get_children())
                        recommendsql = "select * from mobile where mobile_name in " \
                        "(select mobile_name from mobilecount where count=(select max(count) from mobilecount));"
                        curu.execute(recommendsql)
                        recommendres = curu.fetchall()
                        for i in recommendres:
                            dis.insert('', 'end', values=i)
                    bought = Button(pro, text="MOST BOUGHT", font=("bold", 13), command=recommend)
                    bought.place(x=400, y=140)

                    # Function to display the bill page and further transaction
                    def bill():
                        diss.delete(*diss.get_children())
                        item = dis.selection()
                        for j in item:
                            k = dis.item(j, 'values')
                            diss.insert('', 'end', values=k)

                    proceed = Button(pro, text="Proceed to bill", font=("bold", 13), background="#ffb84d",foreground="#006600", command=bill)
                    proceed.place(x=550, y=140)
                    bill = LabelFrame(cuspage, text="Billing section", borderwidth=2, background="#b3b3ff",foreground="#ff0000", relief="solid")
                    bill.place(x=2, y=270, width=700, height=150)
                    col = ('NAME', 'BRAND', 'RAM', 'STORAGE', 'COLOUR', 'PRICE', 'DATE')
                    diss = ttk.Treeview(bill, height=1, show='headings', columns=col)
                    diss.column('NAME', width=100, anchor=CENTER)
                    diss.column('BRAND', width=100, anchor=CENTER)
                    diss.column('RAM', width=50, anchor=CENTER)
                    diss.column('STORAGE', width=50, anchor=CENTER)
                    diss.column('COLOUR', width=50, anchor=CENTER)
                    diss.column('PRICE', width=100, anchor=CENTER)
                    diss.column('DATE', width=100, anchor=CENTER)
                    diss.heading('NAME', text="NAME")
                    diss.heading('BRAND', text="BRAND")
                    diss.heading('RAM', text="RAM")
                    diss.heading('STORAGE', text="STORAGE")
                    diss.heading('COLOUR', text="COLOUR")
                    diss.heading('PRICE', text="PRICE")
                    diss.heading('DATE', text="DATE OF RELEASE")
                    diss.pack(side=TOP, fill=BOTH)
                    def purchase():
                        item = dis.selection()
                        if item:
                            for l in item:
                                ans = dis.item(l, 'values')[0]
                        dbmss = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                        cur = dbmss.cursor()
                        sql="select * from purchase where username=%s and mobile_name=%s"
                        cur.execute(sql,(nares[0],ans))
                        result=cur.fetchall()
                        if result:
                            answer=messagebox.askquestion("WARNING!","You have already purchased the selected mobile!\n\nDo you want to but it again?")
                            if answer=="yes":
                                item = dis.selection()
                                if item:
                                    for l in item:
                                        k = dis.item(l, 'values')[0]
                                    dbms = mysql.connector.connect(host="localhost", user="root",
                                                                   passwd="Josephite1999", database="project")
                                    cu = dbms.cursor()
                                    insert = "insert into purchase values(%s,%s)"
                                    cu.execute(insert, (nares[0], k))
                                    dbms.commit()
                                    up = "update mobilecount set count=count+1 where mobile_name=%s"
                                    cu.execute(up, [(k)])
                                    dbms.commit()
                                    down = "update mobilecount set quant=quant-1 where mobile_name=%s"
                                    cu.execute(down, [(k)])
                                    dbms.commit()
                                    messagebox.showinfo("Successfull","Successfully purchased your mobile\nContinue to shop!!")
                                    diss.delete(*diss.get_children())
                                    dis.delete(*dis.get_children())
                                else:
                                    messagebox.showerror("Error", "Select a product")
                            elif answer=="no":
                                diss.delete(*diss.get_children())
                                dis.delete(*dis.get_children())
                        else:
                            item = dis.selection()
                            if item:
                                for l in item:
                                    k = dis.item(l, 'values')[0]
                                dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                                cu = dbms.cursor()
                                insert = "insert into purchase values(%s,%s)"
                                cu.execute(insert, (nares[0],k))
                                dbms.commit()
                                up="update mobilecount set count=count+1 where mobile_name=%s"
                                cu.execute(up, [(k)])
                                dbms.commit()
                                down="update mobilecount set quant=quant-1 where mobile_name=%s"
                                cu.execute(down, [(k)])
                                dbms.commit()
                                messagebox.showinfo("Successfull", "Successfully purchased your mobile\nContinue to shop!!")
                                diss.delete(*diss.get_children())
                                dis.delete(*dis.get_children())
                            else:
                                messagebox.showerror("Error","Select a product")
                    confirm = Button(bill, text="Confirm purchase", font=("bold", 13), background="#ffb84d",foreground="#006600", command=purchase)
                    confirm.place(x=250, y=80)
                    def history():
                        cuspage.withdraw()
                        history=Tk()
                        history.geometry("700x500+0+0")
                        history.title("Customer portal")
                        history.config(background="#00b3b3")
                        title = Label(history, text="Your purchase history,", width=25,foreground="#ff3300", background="#00b3b3",font=("bold", 20))
                        title.place(x=5, y=5)
                        his = LabelFrame(history, text="", borderwidth=0, background="#00b3b3",foreground="#ff0000", relief="solid")
                        his.place(x=3, y=60, width=680, height=130)
                        o = IntVar()
                        feedback=LabelFrame(history, text="Ratings", borderwidth=2, background="#b3b3ff",foreground="#ff0000", relief="solid")
                        feedback.place(x=3, y=200, width=680, height=180)
                        tet=Label(feedback, text="How was your expereince with the mobile/mobiles you purchased?\nYour feedback is much appreciated!",
                        width=80,background="#b3b3ff",foreground="#802000",font=("bold", 10))
                        tet.place(x=5, y=5)
                        nott=Label(feedback,text="Note** select a mobile from above display and rate it according to your satisfaction from 1 to 5!",
                        width=80, background="#b3b3ff", foreground="#802000", font=("bold", 10))
                        nott.place(x=5, y=45)
                        ent=Entry(feedback,width=10)
                        ent.place(x=2,y=80)
                        def rate():
                            dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                            cor = dbms.cursor()
                            item = diss.selection()
                            if item:
                                for l in item:
                                    k = diss.item(l, 'values')[0]
                                sqll="select * from rating where username=%s and mobile_name=%s"
                                cor.execute(sqll,(nares[0],k))
                                res=cor.fetchall()
                                if res:
                                    ent.delete(0, END)
                                    messagebox.showinfo("Done","You have already given feedback for this product!")
                                elif ent.get()!="":
                                    print(nares[0],k,ent.get())
                                    sql="insert into rating values(%s,%s,%s)"
                                    cor.execute(sql,(nares[0],k,ent.get()))
                                    dbms.commit()
                                    messagebox.showinfo("Thankyou","Thanks for the feedback!")
                                    ent.delete(0,END)
                                else:
                                    messagebox.showerror("Error", "Enter star rating")
                            else:
                                messagebox.showerror("Error","Invalid Entry")
                                ent.delete(0, END)
                        confirm=Button(feedback, text="Submit", font=("bold", 13),background="#ffb84d",foreground="#006600", command=rate)
                        confirm.place(x=40, y=120)
                        col = ('NAME', 'BRAND', 'RAM', 'STORAGE', 'COLOUR', 'PRICE', 'DATE')
                        diss = ttk.Treeview(his, height=5, show='headings', columns=col)
                        diss.column('NAME', width=100, anchor=CENTER)
                        diss.column('BRAND', width=100, anchor=CENTER)
                        diss.column('RAM', width=50, anchor=CENTER)
                        diss.column('STORAGE', width=50, anchor=CENTER)
                        diss.column('COLOUR', width=50, anchor=CENTER)
                        diss.column('PRICE', width=100, anchor=CENTER)
                        diss.column('DATE', width=100, anchor=CENTER)
                        diss.heading('NAME', text="NAME")
                        diss.heading('BRAND', text="BRAND")
                        diss.heading('RAM', text="RAM")
                        diss.heading('STORAGE', text="STORAGE")
                        diss.heading('COLOUR', text="COLOUR")
                        diss.heading('PRICE', text="PRICE")
                        diss.heading('DATE', text="DATE OF RELEASE")
                        diss.pack(side=TOP, fill=BOTH)
                        dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                        c = dbms.cursor()
                        sql="select * from mobile where mobile_name in (select mobile_name from purchase where username=%s);"
                        c.execute(sql,[(nares[0])])
                        hs = c.fetchall()
                        if hs:
                            for i in hs:
                                diss.insert('', 'end', values=i)
                        else:
                            messagebox.showinfo("","No purchases yet! Start to shop")
                        def back():
                            history.withdraw()
                            cuspage.deiconify()
                        back = Button(history, text="BACK", font=("bold", 13), background="#6666ff",foreground="#ff9900", command=back)
                        back.place(x=450, y=440)
                        def lout():
                            history.withdraw()
                            customer.deiconify()
                            messagebox.showinfo("Logged out","Successfully logged out!")
                        lout = Button(history, text="LOG OUT", font=("bold", 13), background="#6666ff",foreground="#ff9900", command=lout)
                        lout.place(x=550, y=440)
                    cart= Button(cuspage, text="SHOPPING HISTORY", font=("bold", 13), background="#6666ff",foreground="#ff9900", command=history)
                    cart.place(x=520, y=8)
            else:
                messagebox.showerror("Login error","Details not found!\nSignUp and proceed.")
                uentry.delete(0,END)
                passentry.delete(0, END)

    button = Button(customer, text="Login", font=10,command=login).place(x=220, y=210)
    space = Label(customer, text="", background="sky blue")

    def new_user():
        customer.withdraw()
        global root2
        root2 = Tk()
        root2.geometry('500x500+100+100')
        root2.title("Customer Signup")
        root2.config(bg="#00b3b3")
        title = Label(root2, text="Customer SignUp", width=15, background="#00b3b3", font=("bold", 25))
        title.place(x=130, y=33)
        newusername = Label(root2, text="USER NAME", compound=LEFT,background="#00b3b3",foreground="#b35900", font=10).place(x=100, y=120)
        newuentry = Entry(root2)
        newuentry.place(x=280, y=123)
        newpassword = Label(root2, text="PASSWORD", compound=LEFT,background="#00b3b3",foreground="#b35900", font=10).place(x=100, y=160)
        newpassentry = Entry(root2, show="*")
        newpassentry.place(x=280, y=163)
        newphone = Label(root2, text="PHONE NUMBER",background="#00b3b3",foreground="#b35900", compound=LEFT, font=10).place(x=100, y=200)
        newphoneentry = Entry(root2)
        newphoneentry.insert(0,"10-digits")
        newphoneentry.place(x=280, y=200)
        def register():
            name=newuentry.get().islower()
            name1=newuentry.get().isupper()
            name2 = len(newuentry.get()) > 6
            passs1=newpassentry.get().islower()
            passs2=newpassentry.get().isupper()
            passs3 = len(newpassentry.get()) > 7
            phno = newphoneentry.get().isdigit()
            phno1 = len(newphoneentry.get()) == 10
            dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999", database="project")
            cur = dbms.cursor()
            sqll = "select username from customer where username=%s"
            cur.execute(sqll, [(newuentry.get())])
            ress = cur.fetchone()
            sql = "select phno from customer where phno=%s"
            cur.execute(sql, [(newphoneentry.get())])
            res = cur.fetchone()
            if newphoneentry.get()=="9380103347":
                la=Label(root2, text="Enter OTP:", compound=LEFT,background="#00b3b3",foreground="#b35900", font=10).place(x=20, y=340)
                laentry=IntVar()
                laentry=Entry(root2)
                laentry.place(x=150, y=340)
                otp = random.randint(1000, 5000)
                phno = 9380103347
                s=str(otp)
                otps(otp, phno)
                def check():
                    if laentry.get()==s:
                        dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                        cur = dbms.cursor()
                        insert = "insert into customer values(%s,%s,%s)"
                        cur.execute(insert, (newuentry.get(), newpassentry.get(), newphoneentry.get()))
                        dbms.commit()
                        messagebox.showinfo("Success!", "Registered!!\n Continue to Login")
                        root2.withdraw()
                        customer.deiconify()
                    else:
                        messagebox.showerror("Error","OTP incorrect!")
                        laentry.delete(0,END)
                        newphoneentry.delete(0, END)
                        newuentry.delete(0, END)
                        newpassentry.delete(0, END)
                con=Button(root2, text="Confirm",command=check, font=10)
                con.place(x=250, y=400)
            elif res:
                for i in res:
                    newphoneentry.delete(0, END)
                    newuentry.delete(0, END)
                    newpassentry.delete(0, END)
                    messagebox.showerror("Error","Phone number  already exist!")
            elif ress:
                for i in ress:
                    newphoneentry.delete(0, END)
                    newuentry.delete(0, END)
                    newpassentry.delete(0, END)
                    messagebox.showerror("Error", "Username already exist!")
            elif newphoneentry.get()!="" and phno and phno1 and newuentry.get()!="" and newpassentry.get()!="" and name2 and passs3 and name==False and name1==False and passs1==False and passs2==False :
                dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                cur = dbms.cursor()
                insert = "insert into customer values(%s,%s,%s)"
                cur.execute(insert, (newuentry.get(), newpassentry.get(), newphoneentry.get()))
                dbms.commit()
                messagebox.showinfo("Success!","Registered!!\n Continue to Login")
                root2.withdraw()
                customer.deiconify()
            else:
                messagebox.showerror("Error","Invalid details")
                newphoneentry.delete(0,END)
                newuentry.delete(0, END)
                newpassentry.delete(0, END)
                newphoneentry.insert(0, "10-digits")
        newbutton = Button(root2, text="REGISTER",command=register, font=10)
        newbutton.place(x=200, y=240)

    newuser = Button(customer, text="New user",command=new_user,background="#00b3b3", font=("arial", 14, "underline"), border=0,foreground="#660033").place(x=130, y=270)
    def back():
        customer.withdraw()
        root.deiconify()
    newuser = Button(customer, text="Back", command=back, background="#00b3b3", font=("arial", 14, "underline"),border=0, foreground="#660033").place(x=280, y=270)

#code for admin portal
def admin():
    root.withdraw()
    admin=Tk()
    admin.geometry("600x400+100+100")
    admin.title("Admin page")
    admin.config(bg="#00b3b3")
    title = Label(admin, text="Admin Login", width=10,background="#00b3b3", font=("bold", 30))
    title.place(x=180, y=33)
    a = StringVar()
    b = StringVar()
    adminname=Label(admin,text="Username",foreground="#b35900",background="#00b3b3",font=("bold", 15)).place(x=150,y=150)
    nameentry=Entry(admin,width=20,textvariable=a)
    nameentry.place(x=300,y=150)
    adminpass = Label(admin, text="Password",background="#00b3b3",foreground="#b35900", font=("bold", 15)).place(x=150, y=200)
    passentry = Entry(admin,width=20,show="*",textvariable=b)
    passentry.place(x=300, y=200)

    # this fucntion checks for login credentials of ADMIN
    def admincheck():
        if nameentry.get()=="" or passentry.get()=="":
            messagebox.showerror("Error","Enter necessary Credentials")
        else:
            dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999", database="project")
            cur = dbms.cursor()
            sql = "select * from admin where admin_name=%s and password=%s"
            cur.execute(sql, (nameentry.get(), passentry.get()))
            res = cur.fetchall()
            if res:
                for i in res:
                    messagebox.showinfo("Login", "Login successful")
                    admin.withdraw()
                    admin1 = Tk()
                    admin1.geometry("720x500+0+0")
                    admin1.config(background="#00b3b3")
                    admin1.title("Admin portal")
                    adminframe = LabelFrame(admin1, text="Admin section", borderwidth=2, background="#b3b3ff",foreground="#ff0000", relief="solid")
                    adminframe.place(x=5, y=5, width=300, height=490)
                    heading = Label(adminframe, text="CHANGE USERNAME", font=("Helvetica", 13), background="#b3b3ff",foreground="#802000")
                    heading.place(x=45, y=1)
                    uname1 = Label(adminframe, text="Old Username", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    uname1.place(x=10, y=35)
                    unameentry1 = Entry(adminframe, width=20)
                    unameentry1.place(x=120, y=35)
                    unewname1 = Label(adminframe, text="New Username", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    unewname1.place(x=10, y=60)
                    unewnameentry1 = Entry(adminframe, width=20)
                    unewnameentry1.place(x=120, y=65)
                    upass1 = Label(adminframe, text="Password", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    upass1.place(x=10, y=90)
                    upassentry1 = Entry(adminframe, width=20, show="*")
                    upassentry1.place(x=120, y=95)

                    # This fucntion works on updating the username of ADMIN
                    def changeuname():
                        dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",
                                                       database="project")
                        cur = dbms.cursor()
                        sql = "select * from admin where admin_name=%s and password=%s"
                        cur.execute(sql, (unameentry1.get(), upassentry1.get()))
                        res = cur.fetchall()
                        if res:
                            for i in res:
                                sql1 = "update admin set admin_name=%s where password=%s"
                                cur.execute(sql1, (unewnameentry1.get(), upassentry1.get()))
                                dbms.commit()
                                messagebox.showinfo("Success", "Username changed successfully!")
                                unameentry1.delete(0, END)
                                upassentry1.delete(0, END)
                                unewnameentry1.delete(0, END)
                        else:
                            messagebox.showerror("Error", "Details Not found")
                            unameentry1.delete(0, END)
                            upassentry1.delete(0, END)
                            unewnameentry1.delete(0, END)
                    but = Button(adminframe, text="Update Username", font=("Helvetica", 11), command=changeuname)
                    but.place(x=80, y=135)
                    heading1 = Label(adminframe, text="CHANGE PASSWORD", font=("Helvetica", 13), background="#b3b3ff",foreground="#802000")
                    heading1.place(x=45, y=200)
                    uname2 = Label(adminframe, text="Username", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    uname2.place(x=10, y=235)
                    unameentry2 = Entry(adminframe, width=20)
                    unameentry2.place(x=120, y=235)
                    unewname2 = Label(adminframe, text="Old Password", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    unewname2.place(x=10, y=260)
                    uoldpasentry2 = Entry(adminframe, width=20)
                    uoldpasentry2.place(x=120, y=265)
                    upass2 = Label(adminframe, text="New Password", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    upass2.place(x=10, y=290)
                    unewpassentry2 = Entry(adminframe, width=20, show="*")
                    unewpassentry2.place(x=120, y=295)

                    # This fucntion works on updating the password of ADMIN
                    def changepass():
                        dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",
                                                       database="project")
                        cur = dbms.cursor()
                        sql = "select * from admin where admin_name=%s and password=%s"
                        cur.execute(sql, (unameentry2.get(), uoldpasentry2.get()))
                        res = cur.fetchall()
                        if res:
                            for i in res:
                                sql1 = "update admin set password=%s where admin_name=%s"
                                cur.execute(sql1, (unewpassentry2.get(), unameentry2.get()))
                                dbms.commit()
                                messagebox.showinfo("Success", "Username changed successfully!")
                                unameentry2.delete(0, END)
                                uoldpasentry2.delete(0, END)
                                unewpassentry2.delete(0, END)
                        else:
                            messagebox.showerror("Error", "Details Not found")
                            unameentry2.delete(0, END)
                            uoldpasentry2.delete(0, END)
                            unewpassentry2.delete(0, END)
                    but = Button(adminframe, text="Update Password", font=("Helvetica", 11), command=changepass)
                    but.place(x=80, y=335)
                    employeeframe=LabelFrame(admin1, text="Employee section", borderwidth=2, background="#b3b3ff",foreground="#ff0000", relief="solid")
                    employeeframe.place(x=315, y=5, width=400, height=490)
                    heading1 = Label(employeeframe, text="ADD EMPLOYEE", font=("Helvetica", 13), background="#b3b3ff",foreground="#802000")
                    heading1.place(x=45, y=1)
                    ename1 = Label(employeeframe, text="Employee name", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    ename1.place(x=10, y=35)
                    enameentry1 = Entry(employeeframe, width=20)
                    enameentry1.place(x=130, y=35)
                    edept1 = Label(employeeframe, text="Department", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    edept1.place(x=10, y=60)
                    edeptentry1 = Entry(employeeframe, width=20)
                    edeptentry1.place(x=130, y=65)
                    esal1 = Label(employeeframe, text="Salary", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    esal1.place(x=10, y=90)
                    esalentry1 = Entry(employeeframe, width=20)
                    esalentry1.place(x=130, y=95)
                    eout1 = Label(employeeframe, text="ESSN generated", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    eout1.place(x=10, y=120)
                    eoutentry1=Entry(employeeframe, width=20)
                    eoutentry1.place(x=130, y=125)
                    note=Label(employeeframe,text="**Employee ESSN will be auto-generated!",background="#b3b3ff")
                    note.place(x=2,y=145)
                    eoutentry1.configure(state=tk.DISABLED)

                    # This function works on adding a new employee
                    def new_employee():
                        if enameentry1.get()=="" or edeptentry1.get()=="" or esalentry1.get()=="":
                            messagebox.showerror("Error","Enter valid details")
                            enameentry1.delete(0, END)
                            edeptentry1.delete(0, END)
                            esalentry1.delete(0, END)
                        else:
                            dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                            cur = dbms.cursor()
                            sql="select name,department ,salary from employee where name=%s and department=%s and salary=%s"
                            cur.execute(sql, (enameentry1.get(), edeptentry1.get(),esalentry1.get()))
                            res = cur.fetchall()
                            if res:
                                messagebox.showerror("Error","Employee already registered")
                                enameentry1.delete(0, END)
                                edeptentry1.delete(0, END)
                                esalentry1.delete(0, END)
                            else:
                                sql1 = "Select count from employeecount"
                                cur.execute(sql1)
                                res1 = cur.fetchone()
                                a = 1 + res1[0]
                                sql2 = "update employeecount set count=%s where count=%s"
                                cur.execute(sql2, (a, a - 1))
                                dbms.commit()
                                sql3 = "insert into employee values(%s,%s,%s,%s)"
                                cur.execute(sql3, (a, enameentry1.get(), edeptentry1.get(), esalentry1.get()))
                                dbms.commit()
                                enameentry1.delete(0, END)
                                edeptentry1.delete(0, END)
                                esalentry1.delete(0, END)
                                eoutentry1.configure(state=tk.NORMAL)
                                eoutentry1.delete(0, END)
                                eoutentry1.insert(0, a)
                                eoutentry1.configure(state=tk.DISABLED)
                                messagebox.showinfo("Success", "Employee added!")
                    eadd=Button(employeeframe,text="Add",font=("bold", 13),command=new_employee)
                    eadd.place(x=80, y=170)
                    heading2 = Label(employeeframe, text="DELETE EMPLOYEE", font=("Helvetica", 13), background="#b3b3ff",foreground="#802000")
                    heading2.place(x=45, y=250)
                    essn2 = Label(employeeframe, text="Employee ESSN ", font=("Helvetica", 11), background="#b3b3ff",foreground="#802000")
                    essn2.place(x=10, y=290)
                    essnentry2=Entry(employeeframe,width=20)
                    essnentry2.place(x=130,y=290)

                    # This fucntion works on deleting an employee
                    def del_employee():
                        if essnentry2.get()=="":
                            messagebox.showerror("Error","Enter valid essn")
                        else:
                            dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                            cur = dbms.cursor()
                            sqll = "select essn from employee where essn=%s"
                            cur.execute(sqll, [(essnentry2.get())])
                            res = cur.fetchall()
                            if res:
                                for i in res:
                                    sql11 = "delete from employee where essn=%s"
                                    cur.execute(sql11, [(essnentry2.get())])
                                    dbms.commit()
                                    messagebox.showinfo("Success", "Employee details deleted")
                                    essnentry2.delete(0, END)
                            else:
                                messagebox.showerror("Error", "Employee detail not in database")
                                essnentry2.delete(0, END)
                    edel=Button(employeeframe,text="Delete",font=("bold", 13),command=del_employee)
                    edel.place(x=80, y=330)

                    # This fucntion redirectes the page to mobile_section of admin after clicking the NEXT button
                    def next():
                        next=Tk()
                        admin1.withdraw()
                        next.geometry("860x600+0+0")
                        next.config(background="#00b3b3")
                        next.title("Admin portal")
                        employeeframe1 = LabelFrame(next, text="Employee section", borderwidth=2, background="#b3b3ff",foreground="#ff0000", relief="solid")
                        employeeframe1.place(x=5, y=5, width=850, height=250)
                        productframe = LabelFrame(next, text="Product section", borderwidth=2, background="#b3b3ff",foreground="#ff0000", relief="solid")
                        productframe.place(x=5, y=260, width=850, height=330)
                        list=Label(productframe, text="LIST OF MOBILES IN STORE", font=("Helvetica", 13),background="#b3b3ff", foreground="#802000")
                        list.place(x=3, y=1)
                        tv = LabelFrame(employeeframe1, text="", borderwidth=0, background="#b3b3ff",foreground="#ff0000", relief="solid")
                        tv.place(x=2, y=145, width=800, height=180)
                        pv = LabelFrame(productframe, text="", borderwidth=0, background="#b3b3ff",foreground="#ff0000", relief="solid")
                        pv.place(x=2, y=50, width=800, height=250)
                        total=Label(productframe,text="Number of mobiles", font=("Helvetica", 11),background="#b3b3ff", foreground="#802000")
                        total.place(x=520, y=10)
                        tentry=Entry(productframe, width=7)
                        tentry.place(x=670,y=15)
                        dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                        cur = dbms.cursor()
                        tmob = "select count(*) from mobile"
                        cur.execute(tmob)
                        tmobresult = cur.fetchone()
                        tentry.insert(0, tmobresult)
                        tentry.configure(state=tk.DISABLED)
                        col = ('NAME', 'BRAND', 'RAM', 'STORAGE', 'COLOUR', 'PRICE','DATE')
                        dis = ttk.Treeview(pv, height=10, show='headings', columns=col)
                        dis.column('NAME', width=100, anchor=CENTER)
                        dis.column('BRAND', width=100, anchor=CENTER)
                        dis.column('RAM', width=50, anchor=CENTER)
                        dis.column('STORAGE', width=50, anchor=CENTER)
                        dis.column('COLOUR', width=50, anchor=CENTER)
                        dis.column('PRICE', width=100, anchor=CENTER)
                        dis.column('DATE', width=100, anchor=CENTER)
                        dis.heading('NAME', text="NAME")
                        dis.heading('BRAND', text="BRAND")
                        dis.heading('RAM', text="RAM")
                        dis.heading('STORAGE', text="STORAGE")
                        dis.heading('COLOUR', text="COLOUR")
                        dis.heading('PRICE', text="PRICE")
                        dis.heading('DATE', text="DATE OF RELEASE")
                        dis.pack(side=TOP, fill=BOTH)
                        dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                        cur = dbms.cursor()
                        sql = "select * from mobile"
                        cur.execute(sql)
                        result = cur.fetchall()
                        for i in result:
                                dis.insert('', 'end', values=i)
                        heading2 = Label(employeeframe1, text="SEARCH EMPLOYEE", font=("Helvetica", 13),background="#b3b3ff", foreground="#802000")
                        heading2.place(x=45, y=1)
                        totalmob=Label(employeeframe1, text="Total employees in mobile section", font=("Helvetica", 11),background="#b3b3ff", foreground="#802000")
                        totalmob.place(x=400, y=15)
                        tmobentry=Entry(employeeframe1, width=7)
                        tmobentry.place(x=670,y=15)
                        # totallap = Label(employeeframe1, text="Total employees in laptop section", font=("Helvetica", 11),background="#b3b3ff", foreground="#802000")
                        # totallap.place(x=400, y=35)
                        # tlapentry = Entry(employeeframe1, width=7)
                        # tlapentry.place(x=670, y=35)
                        req="mobile"
                        # req1="laptop"
                        mobsql = "select count(*) from employee where department=%s"
                        cur.execute(mobsql, [(req)])
                        mobresult=cur.fetchone()
                        # lapsql = "select count(*) from employee where department=%s"
                        # cur.execute(mobsql, [(req1)])
                        # lapresult = cur.fetchone()
                        eserch = Label(employeeframe1, text="Employee Essn", font=("Helvetica", 11),background="#b3b3ff", foreground="#802000")
                        eserch.place(x=10, y=35)
                        esearchentry = Entry(employeeframe1, width=20)
                        esearchentry.place(x=130, y=35)
                        tmobentry.insert(0, mobresult)
                        # tlapentry.insert(0, lapresult)
                        tmobentry.configure(state=tk.DISABLED)
                        # tlapentry.configure(state=tk.DISABLED)
                        display = ttk.Treeview(tv, columns=(1, 2, 3, 4), show="headings", height="2")
                        display.pack()
                        display.heading(1, text="ESSN")
                        display.heading(2, text="NAME")
                        display.heading(3, text="DEPARTMENT")
                        display.heading(4, text="SALARY")

                        # This fucntion works on searching for a specific employee based on the ESSN
                        def ser_employee():
                            if esearchentry.get()=="":
                                messagebox.showerror("Error","Enter valid details")
                            else:
                                dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                                cur = dbms.cursor()
                                sql = "select * from employee where essn=%s"
                                cur.execute(sql, [(esearchentry.get())])
                                result = cur.fetchall()
                                if result:
                                    display.delete(*display.get_children())
                                    for i in result:
                                        display.insert('', 'end', values=i)
                                else:
                                    esearchentry.delete(0, END)
                                    messagebox.showwarning("error", "no details found")
                        esearch = Button(employeeframe1, text="Search", font=("bold", 13), command=ser_employee)
                        esearch.place(x=80, y=85)

                        # This fucntion works clearing the tree view section's column
                        def clear_employee():
                            for i in display.get_children():
                                display.delete(i)
                            esearchentry.delete(0, END)
                        eclear = Button(employeeframe1, text="Clear", font=("bold", 13), command=clear_employee)
                        eclear.place(x=170, y=85)

                        # This fucntion works on listing all the employees registered
                        def list_employee():
                            dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                            cur = dbms.cursor()
                            sqll = "select * from employee"
                            cur.execute(sqll)
                            result = cur.fetchall()
                            if result:
                                for i in result:
                                    display.insert('', 'end', values=i)
                            else:
                                messagebox.showwarning("error", "No employees registered!")
                        list = Button(employeeframe1, text="List", font=("bold", 13), command=list_employee)
                        list.place(x=260, y=85)
                        def back_employee():
                            next.withdraw()
                            admin1.deiconify()
                        eback = Button(employeeframe1, text="Back", font=("bold", 13),background="#40bf40", command=back_employee)
                        eback.place(x=750, y=5)
                        def logs():
                            next.withdraw()
                            root.deiconify()
                            messagebox.showinfo("Logout", "Successfully logged out")

                        log = Button(employeeframe1, text="Log Out", font=("bold", 13),background="#40bf40", command=logs)
                        log.place(x=750, y=50)

                    next=Button(employeeframe,text="Next",font=("bold", 13),command=next)
                    next.place(x=300, y=5)
            else:
                nameentry.delete(0, END)
                passentry.delete(0, END)
                messagebox.showerror("Login Error", "Invalid Username or password")

    submit=Button(admin,text="Login",font=("bold", 13),command=admincheck).place(x=200,y=250)
    def back():
        admin.withdraw()
        root.deiconify()
    back = Button(admin, text="Back", font=("bold", 13),command=back).place(x=280, y=250)

#code for supplier portal
def supplier():
   root.withdraw()
   supplier=Tk()
   supplier.geometry("500x400+100+100")
   supplier.config(background="#00b3b3")
   supplier.title("Supplier portal")
   suptitle = Label(supplier, text="Supplier Login", width=10, background="#00b3b3", font=("bold", 30))
   suptitle.place(x=140, y=33)
   supid = Label(supplier, text="Supplier Id", foreground="#b35900", background="#00b3b3", font=("bold", 15))
   supid.place(x=110, y=150)
   supidtry = Entry(supplier, width=20)
   supidtry.place(x=250, y=150)
   suppass = Label(supplier, text="Password", background="#00b3b3", foreground="#b35900", font=("bold", 15))
   suppass.place(x=110,y=200)
   suppassentry = Entry(supplier, width=20, show="*")
   suppassentry.place(x=250, y=200)
   def suplogin():
       if supidtry.get()=="" or suppassentry.get()=="":
           messagebox.showerror("Login Error","Enter valid details")
       else:
           dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999", database="project")
           cur = dbms.cursor()
           sql = "select * from supplier where sup_id=%s and password=%s"
           cur.execute(sql, (supidtry.get(),suppassentry.get()))
           res = cur.fetchall()
           name="select name from supplier where sup_id=%s and password=%s"
           cur.execute(name, (supidtry.get(), suppassentry.get()))
           nameres=StringVar()
           nameres=(cur.fetchone())
           id = "select sup_id from supplier where sup_id=%s and password=%s"
           cur.execute(id, (supidtry.get(), suppassentry.get()))
           idres = StringVar()
           idres = (cur.fetchone())
           contact = "select contact from supplier where sup_id=%s and password=%s"
           cur.execute(contact, (supidtry.get(), suppassentry.get()))
           contact = StringVar()
           contact = (cur.fetchone())
           if res:
               for i in res:
                   messagebox.showinfo("Login", "Login successful")
                   supplier.withdraw()
                   suppage = Tk()
                   suppage.geometry("720x500+0+0")
                   suppage.config(background="#00b3b3")
                   suppage.title("Supplier portal")

                   welcome=Label(suppage, text="Hello, "+nameres[0]+" !!!", foreground="#802b00", background="#00b3b3",font=("bold", 15))
                   welcome.place(x=5,y=75)
                   weltitle=Label(suppage, text="Your details:-", foreground="#802b00", background="#00b3b3",font=("bold", 15))
                   weltitle.place(x=500,y=10)
                   welid = Label(suppage, text="ID : ", foreground="#802b00", background="#00b3b3",font=("bold", 10))
                   welid.place(x=500, y=35)
                   welid1 = Label(suppage, text=idres[0], foreground="#802b00", background="#00b3b3",font=("bold", 10))
                   welid1.place(x=600, y=35)
                   welname = Label(suppage, text="NAME :", foreground="#802b00", background="#00b3b3",font=("bold", 10))
                   welname.place(x=500, y=60)
                   welname1 = Label(suppage, text=nameres[0], foreground="#802b00", background="#00b3b3", font=("bold", 10))
                   welname1.place(x=600, y=60)
                   welcon = Label(suppage, text="CONTACT :", foreground="#802b00", background="#00b3b3", font=("bold", 10))
                   welcon.place(x=500, y=85)
                   welcon1 = Label(suppage, text=contact[0], foreground="#802b00", background="#00b3b3",font=("bold", 10))
                   welcon1.place(x=600, y=85)

                   mname = Label(suppage, text="Mobile name", foreground="#000099", background="#00b3b3",font=("bold", 15))
                   mname.place(x=110, y=150)
                   mnameentry = Entry(suppage, width=20)
                   mnameentry.place(x=230, y=150)
                   mbrand = Label(suppage, text="Brand", background="#00b3b3", foreground="#000099",font=("bold", 15))
                   mbrand.place(x=110, y=190)
                   mbrandentry=Entry(suppage, width=20)
                   mbrandentry.place(x=230, y=190)
                   mram = Label(suppage, text="RAM", background="#00b3b3", foreground="#000099", font=("bold", 15))
                   mram.place(x=110, y=230)
                   mramentry = Entry(suppage, width=20)
                   mramentry.place(x=230, y=230)
                   mstore = Label(suppage, text="Storage", background="#00b3b3", foreground="#000099", font=("bold", 15))
                   mstore.place(x=110, y=270)
                   mstoreentry = Entry(suppage, width=20)
                   mstoreentry.place(x=230, y=270)
                   mcolor = Label(suppage, text="Colour", background="#00b3b3", foreground="#000099",font=("bold", 15))
                   mcolor.place(x=110, y=310)
                   mcolorentry = Entry(suppage, width=20)
                   mcolorentry.place(x=230, y=310)
                   mprice = Label(suppage, text="Price", background="#00b3b3", foreground="#000099", font=("bold", 15))
                   mprice.place(x=110, y=350)
                   mpriceentry = Entry(suppage, width=20)
                   mpriceentry.place(x=230, y=350)
                   mdate = Label(suppage, text="Date of release", background="#00b3b3", foreground="#000099", font=("bold", 13))
                   mdate.place(x=110, y=390)
                   mdateentry = Entry(suppage, width=20)
                   mdateentry.insert(0,"yyyy/mm/dd")
                   mdateentry.place(x=230, y=390)
                   quantl=Label(suppage, text="Quantity", background="#00b3b3", foreground="#000099", font=("bold", 13))
                   quantl.place(x=360, y=150)
                   quant = Entry(suppage, width=20)
                   quant.place(x=440, y=150)
                   def back():
                       suppage.withdraw()
                       root.deiconify()
                       messagebox.showinfo("Logout", "Successfully logged out")
                   back=Button(suppage, text="Log Out", font=("bold", 13),background="#40bf40", command=back)
                   back.place(x=600,y=450)
                   def add():
                       if mnameentry.get() == "" or mbrandentry.get() == "" or quant.get()=="" or mramentry.get() == "" or mstoreentry.get() == ""\
                            or mcolorentry.get() == "" or mpriceentry.get() == ""or mdateentry.get() == "":
                           messagebox.showerror("Error", "Enter valid details")
                       else:
                           dbms = mysql.connector.connect(host="localhost", user="root", passwd="Josephite1999",database="project")
                           cur = dbms.cursor()
                           insert = "insert into mobile values(%s,%s,%s,%s,%s,%s,%s)"
                           cur.execute(insert, (mnameentry.get(),mbrandentry.get(),mramentry.get(),mstoreentry.get(),mcolorentry.get(),mpriceentry.get(),mdateentry.get()))
                           dbms.commit()
                           messagebox.showinfo("Successfull", "Details added")
                           ins="insert into mobilecount values(%s,%s,%s)"
                           cur.execute(ins,(mnameentry.get(),0,quant.get()))
                           dbms.commit()
                           mnameentry.delete(0,END)
                           quant.delete(0,END)
                           mbrandentry.delete(0, END)
                           mramentry.delete(0, END)
                           mstoreentry.delete(0, END)
                           mcolorentry.delete(0, END)
                           mpriceentry.delete(0, END)
                           mdateentry.delete(0, END)
                           mdateentry.insert(0, "yyyy/mm/dd")
                   add=Button(suppage, text="Add product", font=("bold", 13), foreground="#b35900", command=add)
                   add.place(x=180,y=430)
           else:
               supidtry.delete(0,END)
               suppassentry.delete(0,END)
               messagebox.showerror("Error","Details not found")

   supsubmit = Button(supplier, text="Login", font=("bold", 13), command=suplogin)
   supsubmit.place(x=200, y=250)
   def back():
       supplier.withdraw()
       root.deiconify()

   back = Button(supplier, text="Back", font=("bold", 13), command=back).place(x=280, y=250)


#First root window page of the project which will display the login options for ADMIN, CUSTOMER and SUPPLIER
global root
root=Tk()
root.title("SALES MADE EASY")
backgrd=ImageTk.PhotoImage(Image.open("C://Users//Vishal Nikhil Kumar//Desktop//project_images//background.jpeg"))
imgadmin=ImageTk.PhotoImage(Image.open("C://Users//Vishal Nikhil Kumar//Desktop//project_images//admin.png"))
imgcustomer=ImageTk.PhotoImage(Image.open("C://Users//Vishal Nikhil Kumar//Desktop//project_images//customer.png"))
imgsupplier=ImageTk.PhotoImage(Image.open("C://Users//Vishal Nikhil Kumar//Desktop//project_images//supplier.png"))
backgrdlabel=Label(root,image=backgrd).place(relwidth=1,relheight=1)
admin_but = Button(root,text="ADMIN",border='5',image=imgadmin,command=admin).place(x=120, y=220)
customer_but = Button(root,text="CUSTOMER",command=customer,border='5',image=imgcustomer).place(x=430, y=220)
supplier_but = Button(root,text="SUPPLIER",command=supplier,border='5',image=imgsupplier).place(x=720, y=220)
root.geometry('1000x500+100+100')
root.resizable(False,False)
root.mainloop()