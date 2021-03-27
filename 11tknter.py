from tkinter import *
from tkinter.ttk import *
import re
import pymysql
from tkinter import messagebox

#user info
def clicked():
    root.withdraw()
    window = Tk()
    window.title("User Information")
    window.geometry('650x400')
    window.configure(bg="grey")

    #labels and fields
    lbl = Label(window, text="Name :",font="Times " )      #name label
    lbl.grid(column=0, row=1)
    lbl.configure(foreground="black")
    lbl.configure(background="grey")
    txt_name = Entry(window, width=30)       #name field
    txt_name.grid(column=1, row=1)
    lbl1 = Label(window, text="Email :",font="Times")
    lbl1.grid(column=0, row=2)
    lbl1.configure(foreground="black")
    lbl1.configure(background="grey")
    txt_email = Entry(window, width=30)
    txt_email.grid(column=1, row=2)
    UAddress = Label(window,text="Address :",font="Times")
    UAddress.grid(column=0, row=3)
    UAddress.configure(foreground="black")
    UAddress.configure(background="grey")
    txt_address = Entry(window, width=30)
    txt_address.grid(column=1, row=3)
    Uage = Label(window,text="User Age :",font="Times")
    Uage.grid(column=0, row=4)
    Uage.configure(foreground="black")
    Uage.configure(background="grey")
    var = IntVar(window)
    var.set(18)
    spin = Spinbox(window, from_=0, to=100, width=28,textvariable=var)
    spin.grid(column=1, row=4)
    lbl2 = Label(window, text="Enter 10 digit Mobile No. :",font="Times")
    lbl2.grid(column=0, row=5)
    lbl2.configure(foreground="black")
    lbl2.configure(background="grey")
    txt_no = Entry(window, width=30)
    txt_no.grid(column=1, row=5)
    lbl3 = Label(window, text="Select Category of CD DVD :",font="Times")
    lbl3.grid(column=0, row=7)
    lbl3.configure(foreground="black")
    lbl3.configure(background="grey")
    combo = Combobox(window)
    combo['values'] = ("Movies", "Music", "Games")
    combo.current()
    combo.grid(column=1, row=7, padx=30)
    lbl4 = Label(window, text="Select Genre:",font="Times")
    lbl4.grid(column=0, row=8)
    lbl4.configure(foreground="black")
    lbl4.configure(background="grey")
    combo1 = Combobox(window)
    combo1['values'] = ("Action", "Adventure", "Thriller","Sports")
    combo1.current()
    combo1.grid(column=1, row=8)
    lbl5 = Label(window, text="Enter 5 digit CD DVD ID. :",font="Times")
    lbl5.grid(column=0, row=6)
    lbl5.configure(foreground="black")
    lbl5.configure(background="grey")
    txt_no1 = Entry(window, width=30)
    txt_no1.grid(column=1, row=6)

    #validation if any field is empty
    def validation():
        if txt_name.get() == "" or txt_email.get() == "" or txt_address.get() == "" or var.get() ==0 or txt_no.get() == "" or  combo.get() == "" or combo1.get() == "" or txt_no1.get() == "":
            return False
        else:
            return True

    #email vaidation
    def valid_email():
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex, txt_email.get()):
            return True
        else:
            return False

    #phoneno validation
    def phone_valid():
        Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
        if Pattern.match(txt_no.get()) and len(txt_no.get()) == 10:
            return True
        else:
            return False

    #cddvdid validation
    def id_valid():
        if (len(txt_no1.get())) == 5:
            return True
        else:
            return False
    #insert into database
    def insert():
        connection = pymysql.connect(host="localhost", user="root", password="", database="python")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO userinfo ( Name, Email,address,age,mobile,category,genre,cd_dvd_id) VALUES ('%s' , '%s','%s', '%d' , '%s','%s','%s','%s')"%( txt_name.get(),  txt_email.get(), txt_address.get(),int(var.get()),txt_no.get(),  combo.get(),  combo1.get(), txt_no1.get()))

        connection.commit()

    #reset option
    def reset():
        txt_no.delete(0, END)
        txt_email.delete(0, END)
        txt_name.delete(0, END)
        txt_address.delete(0,END)
        txt_no1.delete(0,END)
        var.set(0)
        combo.set(NONE)
        combo1.set(NONE)

    #reset button
    btnreset = Button(window, text="Reset", command=reset)
    btnreset.grid(column=4, row=2,)
    btnreset.configure()

    #delete option
    def delete():
        if(txt_no1.get() == ""):
           messagebox.showinfo("Delete Status"," CD DVD ID is needed to delete")
        else:
            con=pymysql.connect(host="localhost", user="root", password="", database="python")
            cursor = con.cursor()
            cursor.execute("select  * from userinfo where cd_dvd_id='" + txt_no1.get() + "'")
            if cursor.fetchone()==None:
                messagebox.showinfo("Delete Status", "Deleted id invalid");
            else:
                cursor.execute("delete from userinfo where cd_dvd_id='"+txt_no1.get()+"'")
                con.commit()
                txt_no.delete(0, 'end')
                txt_email.delete(0, 'end')
                txt_name.delete(0, 'end')
                txt_address.delete(0, 'end')
                txt_no1.delete(0, 'end')
                var.set(0)
                combo.set(NONE)
                combo1.set(NONE)
                messagebox.showinfo("Delete Status","Deleted Successfully");
                con.close();
    style=Style()
    style.configure("btndelete", font=('calibri', 10, 'bold', 'underline'), foreground='red')
    #delete button
    btndelete = Button(window, text="Delete", command=delete)
    btndelete.grid(column=3, row=2,padx=10,pady=10)
    style.configure("btndelete",font= ('calibri', 10, 'bold', 'underline'),foreground='red')


    #save option
    def Save():
        if validation() == False:
            messagebox.showerror('Error', 'Field is empty')
        else:
            if valid_email() == False:
                messagebox.showerror('Error', 'Email is incorrect')
            else:
                if phone_valid() == False:
                    messagebox.showerror('Error', 'phone number  is incorrect')
                else:
                    if id_valid() == False:
                        messagebox.showerror('Error', 'ID  is not valid')
                    else:
                        insert()
                        messagebox.showinfo('Saved', 'Deatils Saved')
                        reset()
    #save button
    btn = Button(window, text="Save", command=Save)
    btn.grid(column=3, row=1)

    #update option
    def update():
        name = txt_name.get()
        email = txt_email.get()
        address = txt_address.get()
        age = var.get()
        mobile = txt_no.get()
        category = combo.get()
        genre = combo1.get()
        cd_dvd_id= txt_no1.get()

        if name == "" or email == "" or address == "" or age == 0 or mobile == "" or category == "" or genre == "" or cd_dvd_id =="":
            messagebox.showinfo("Update Status", "All fileds are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="python")
            cursor = con.cursor()
            cursor.execute("select  * from userinfo where cd_dvd_id='" + txt_no1.get() + "'")
            if cursor.fetchone() == None:
                messagebox.showinfo("Delete Status", "Entered CD DVD ID is not present in database ");
            else:
                con = pymysql.connect(host="localhost", user="root", password="", database="python")
                cursor = con.cursor()
                cursor.execute(
                    "update userinfo set name='" + name + "',email='" + email + "',address='" + address + "',age='" + str(
                        age) + "',mobile='" + mobile + "',category='" + category + "',genre='"+genre+"'where cd_dvd_id='" + cd_dvd_id + "'")
                con.commit()

                txt_no.delete(0, END)
                txt_email.delete(0, END)
                txt_name.delete(0, END)
                txt_address.delete(0, END)
                txt_no1.delete(0, END)
                var.set(0)
                combo.set(NONE)
                combo1.set(NONE)
                messagebox.showinfo("Update Status", "Update successfull")
                con.close()

    #update button
    b = Button(window, text="Update", command=update)
    b.grid(column=3, row=3)

    #display option
    def Display():
        # window.withdraw()
        newwin = Toplevel(window)
        newwin.title("Display Details")
        newwin.geometry("1200x600")
        list = Listbox(newwin, height=20, width=95, bg="grey", activestyle='dotbox', font="Arial", fg="black")
        list.place(x=100, y=30)

        def show():
            con = pymysql.connect(host="localhost", user="root", password="", database="python")
            cursor = con.cursor()
            cursor.execute("select * from userinfo")
            rows = cursor.fetchall()

            for row in rows:
                insertData = row[0] + '   ' + row[1] + '    ' + row[2] + '     ' + str(row[3]) + '    ' + row[4] + '    ' + row[5] + '      ' + row[6]+'     '+row[7]
                list.insert(list.size() + 1, insertData)
            con.commit()
            con.close()
        show()

        #display screen back button
        def backbutton():
            newwin.withdraw()
            window.deiconify()

        btns1 = Button(newwin, text="back", command=backbutton)
        btns1.grid(column=0, row=0)

    #display button of user info
    btn1 = Button(window, text="Display", command=Display)
    btn1.grid(column=4, row=1)

    #back button of user info page
    def back():
        window.withdraw()
        root.deiconify()
    btns = Button(window, text="back", command=back)
    btns.grid(column=4, row=3)

#Salesdetails opion
def clicked2():
    root.withdraw()
    window = Tk()
    window.title("Sales Details")
    window.geometry('600x400')
    window.configure(bg="grey")

    #labels and their entry fields
    lbl5 = Label(window, text="Enter 5 digit CD DVD ID :",font="Times")
    lbl5.grid(column=0, row=0)
    lbl5.configure(foreground="black")
    lbl5.configure(background="grey")
    txt_no1 = Entry(window, width=30)
    txt_no1.grid(column=1, row=0)
    sales = Label(window, text="Enter Sales :",font="Times")
    sales.grid(column=0, row=1)
    sales.configure(foreground="black")
    sales.configure(background="grey")
    var = IntVar(window)
    var.set(0)
    spin = Spinbox(window, from_=0, to=100, width=28, textvariable=var)
    spin.grid(column=1, row=1)

    #valid of empty fields
    def validation():
        if txt_no1.get() == "" or var.get()==0 :
            return False
        else:
            return True

    # cddvdid validation
    def id_valid():
        #Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
        if (len(txt_no1.get())) == 5:
            return True
        else:
            return False

    # insert into database
    def insert():
        connection = pymysql.connect(host="localhost", user="root", password="", database="python")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO stockinfo ( cd_dvd_id,sales) VALUES ('%s' , '%d')" % (txt_no1.get(),int(var.get())))

        connection.commit()

    #reset option
    def reset():
        txt_no1.delete(0,END)
        var.set(0)

    #reset button
    btnreset = Button(window, text="Reset", command=reset)
    btnreset.grid(column=1, row=4)

    # delete option
    def delete():
        if (txt_no1.get() == ""):
            messagebox.showinfo("Delete Status", " CD DVD ID is needed to delete")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="python")
            cursor = con.cursor()
            cursor.execute("select  * from stockinfo where cd_dvd_id='" + txt_no1.get() + "'")
            if cursor.fetchone() == None:
                messagebox.showinfo("Delete Status", "Delete id invalid");
            else:
                cursor.execute("delete from stockinfo where cd_dvd_id='" + txt_no1.get() + "'")
                con.commit()
                txt_no1.delete(0, 'end')
                var.set(0)
                messagebox.showinfo("Delete Status", "Deleted Successfully");
                con.close();

    # delete button
    btndelete = Button(window, text="Delete", command=delete)
    btndelete.grid(column=1, row=3)


    # save option
    def Save():
        if validation() == False:
            messagebox.showerror('Error', 'Field is empty')
        else:
            if id_valid() == False:
                messagebox.showerror('Error', 'ID  is not valid')
            else:
                insert()
                messagebox.showinfo('Saved', 'Deatils Saved')
                reset()

    # save button
    btn = Button(window, text="Save", command=Save)
    btn.grid(column=0, row=3,padx=10,pady=10)

    def update():  #cd_dvd_id sales
        sales = var.get()
        cd_dvd_id = txt_no1.get()
        if cd_dvd_id == "" or sales == "":
            messagebox.showinfo("Update Status", "All fileds are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="python")
            cursor = con.cursor()
            cursor.execute("select  * from stockinfo where cd_dvd_id='" + txt_no1.get() + "'")
            if cursor.fetchone() == None:
                messagebox.showinfo("Delete Status", "Entered cd dvd id is not present in database ");
            else:
                con = pymysql.connect(host="localhost", user="root", password="", database="python")
                cursor = con.cursor()
                cursor.execute(
                    "update stockinfo set sales='" + str(sales)  + "'where cd_dvd_id='" + cd_dvd_id + "'")
                con.commit()

                txt_no1.delete(0, END)
                var.set(0)
                messagebox.showinfo("Update Status", "Update successfull")
                con.close()

    #update button
    b = Button(window, text="Update", command=update)
    b.grid(column=0, row=4)

    # display option
    def Display():
        # window.withdraw()
        newwin = Toplevel(window)
        newwin.title("Display Details")
        newwin.geometry("500x400")
        list = Listbox(newwin, height=10, width=20, bg="grey", activestyle='dotbox', font="Arial", fg="black")
        list.place(x=100, y=30)

        def show():
            con = pymysql.connect(host="localhost", user="root", password="", database="python")
            cursor = con.cursor()
            cursor.execute("select * from stockinfo")
            rows = cursor.fetchall()

            for row in rows:
                insertData = row[0] + '   ' + str(row[1])
                list.insert(list.size() + 1, insertData)
            con.commit()
            con.close()

        show()

        # display screen back button
        def backbutton():
            newwin.withdraw()
            window.deiconify()

        btns1 = Button(newwin, text="back", command=backbutton)
        btns1.grid(column=0, row=0)

    # display button of sales info
    btn1 = Button(window, text="Display", command=Display)
    btn1.grid(column=2, row=3)

    #sales details back
    def back():
        window.withdraw()
        root.deiconify()

    # salesdetails back button
    btns = Button(window, text="back", command=back)
    btns.grid(column=2, row=4)

#main
root = Tk()
root.title("CD DVD Store Management App")
root.geometry("580x200")
root.configure(bg='grey')
lbl = Label(root, text="Welcome To CD-DVD Store Management App", font=("Times New Roman Bold", 20)).place(x=20,y=70)
menubar = Menu(root)
storemenu = Menu(menubar, tearoff=0, background='grey',foreground='white',activebackground='white', activeforeground='green')
storemenu.add_command(label="User Info", command=clicked)
storemenu.add_command(label="Sales Info", command=clicked2)
storemenu.add_separator()
storemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Store", menu=storemenu)
root.config(menu=menubar)
root.mainloop()