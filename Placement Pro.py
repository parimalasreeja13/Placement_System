from PIL import ImageTk
from tkinter import *
from tkinter import ttk, Label
import csv
from tkinter import messagebox
from cryptography.fernet import Fernet

pro = Tk()
pro.state("zoomed")
pro.title("PLACEMENT MANAGEMENT SYSTEM")
pro.rowconfigure(0, weight=1)
pro.columnconfigure(0, weight=1)
frame1 = Frame(pro)
frame2 = Frame(pro)
frame3 = Frame(pro)
frame4 = Frame(pro)
frame5 = Frame(pro)
frame6 = Frame(pro)
frame7 = Frame(pro)
frame8 = Frame(pro)
frame9 = Frame(pro)
frame10 = Frame(pro)
frame11 = Frame(pro)
frame12 = Frame(pro)
frame13 = Frame(pro)
frame14 = Frame(pro)
frame15 = Frame(pro)
frame16 = Frame(pro)
frame17 = Frame(pro)
frame18 = Frame(pro)
# For File Encryption :
k = 'gfjrgsfdhtolkjhjnfbdcstGSJdkudcndjsskcifhdk='
fr = Fernet(k)


def exit():
    with open('officer.csv', 'r') as f:
        d = f.read()
    with open('officer.csv', 'w') as f:
        f.write(fr.encrypt(d.encode()).decode())
    with open('Pro Pan.csv', 'r') as l:
        g = l.read()
    with open('Pro Pan.csv', 'w') as f:
        f.write(fr.encrypt(g.encode()).decode())
    quit()


with open('officer.csv', 'r') as f:
    d = f.read()
with open('officer.csv', 'w') as f:
    f.write(fr.decrypt(d.encode()).decode())
with open('Pro Pan.csv', 'r') as l:
    g = l.read()
with open('Pro Pan.csv', 'w') as l:
    l.write(fr.decrypt(g.encode()).decode())
for frame in (
        frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13,
        frame14,
        frame15, frame16, frame17, frame18):
    frame.grid(row=0, column=0, sticky='nsew')


#  To Switch to a Particular Frame
def show_frame(frame_faces):
    frame_faces.tkraise()


# Opening Frame User Interface ( Frame - 1 )
bg = ImageTk.PhotoImage(file="20220324_195439.jpg")
Label(frame1, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

frame1_title = Label(frame1, text='** Choose The User **', fg='green',
                     font=("Baskerville Old Face", 30, "bold")).place(x=510, y=75)
frame1_btn1 = Button(frame1, text=" COMPANY ", font=("Algerian", 30, "bold"), bg='gold',
                     command=lambda: show_frame(frame16)).place(
    x=575, y=200)
frame1_btn2 = Button(frame1, text=" ASPIRANT ", font=("Algerian", 30, "bold"), bg='gold',
                     command=lambda: show_frame(frame3)).place(x=570, y=400)
frame1_btn3 = Button(frame1, text=" EXIT ", font=("Algerian", 30, "bold"), bg='gold', command=exit).place(x=625, y=600)

show_frame(frame1)
#  Company Login Interface ( Frame -2 )
bg2 = ImageTk.PhotoImage(file='20220320_180102.png')
Label(frame2, image=bg2).place(x=0, y=0, relwidth=1, relheight=1)
frame2_company_id = ''


def clicked():
    Label(frame5, text="** Thank You **", font=("Algerian", 10)).place(x=200, y=700)


frame2_company_name = ''


def ex_adinfo(q1, q2):
    g = open('officer.csv', 'r')
    reading = csv.reader(g)
    global frame2_company_name
    for word in reading:
        if q1 == word[0] and q2 == word[2]:
            frame2_company_name = word[1]
            frame2_stu_id.delete(0, END)
            frame2_stu_pass.delete(0, END)
            show_frame(frame4)
            break
    else:
        messagebox.showerror('Warning', 'In-Correct Credentials')
        frame2_stu_id.delete(0, END)
        frame2_stu_pass.delete(0, END)


# Creating Functionality Keys For User Interface:
def get_adinfo():
    global frame2_company_id
    set_info = f"{frame2_p.get()}"
    set_password = f"{frame2_i.get()}"
    frame2_company_id = set_info
    ex_adinfo(set_info, set_password)


frame2_title = Label(frame2, text=" Welcome to Company Portal ", fg="white", bg="green", font=("Algerian", 20),
                     width=35).place(x=500, y=50)
frame2_Id = Label(frame2, text=" Enter Your ID ", fg="black", bg="pink", relief="solid",
                  font=("Arial", 25, "bold")).place(x=450, y=200)
frame2_password = Label(frame2, text=" Enter Password ", fg="black", bg="pink", relief="solid",
                        font=("Arial", 25, "bold")).place(x=450, y=300)
# The Variables we require to Get Student details(initialization):
frame2_p = StringVar()
frame2_i = StringVar()
#  Details Required From the User:
frame2_stu_id = Entry(frame2, textvariable=frame2_p, bg="white", font=("Arial", 25), width=15)
frame2_stu_id.pack()
frame2_stu_id.place(x=850, y=200)
frame2_stu_pass = Entry(frame2, show='*', textvariable=frame2_i, bg="white", font=("Arial", 25), width=15)
frame2_stu_pass.pack()
frame2_stu_pass.place(x=850, y=300)
frame2_browse = Button(frame2, text=" Login ", fg="white", bg="sky blue", font=("Baskerville Old Face", 15, "bold"),
                       width=10,
                       command=get_adinfo).place(x=680, y=500)
frame2_ext_but = Button(frame2, text=" Exit ", fg="white", bg="green", font=("caliber", 10, "bold"), width=15,
                        command=exit).place(x=800, y=650)
frame2_back = Button(frame2, text="Go Back ", fg="white", bg="green", font=("caliber", 10, "bold"), width=15,
                     command=lambda: show_frame(frame16)).place(x=540, y=650)

# For Company to View their Applicants (  Frame -  13 )
bg13 = ImageTk.PhotoImage(file="bgm.jpeg")
Label(frame13, image=bg13).place(x=0, y=0, relwidth=1, relheight=1)
frame13_l1 = Label(frame13, text="YOUR COMPANY SUBSCRIBERS DETAILS", fg="white", bg="green",
                   font=("Arial", 35, "bold")).place(x=400,
                                                     y=30)
frame13_noofsubscribers = Label(frame13, text="Number of subscribers", fg="white", bg="black",
                                font=("Baskerville Old Face", 30, "bold")).place(x=285, y=250)

frame13_subscriberslist = Label(frame13, text="Subscribers list", fg="white", bg="black",
                                font=("Baskerville Old Face", 30, "bold")).place(x=350, y=450)

frame13_back1 = Button(frame13, text="Go Back ", fg="blue", bg="white", font=("caliber", 14, "bold"),
                       command=lambda: show_frame(frame4)).place(x=700, y=600)
frame13_company_name = ''


def Subscribers_list():
    s = []
    count = 0
    l = open('officer.csv', 'r')
    global frame13_company_name
    book_reader = csv.reader(l)
    for row in book_reader:
        if frame2_company_id == row[0]:
            frame13_company_name = row[1]
            (frame13_company_name)
            s = row[3].split()
            k = '  ' + str(len(s)) + '  '
            for i in s:
                if count == 0:
                    m = i
                    count = 1
                else:
                    m = m + ',' + i

            Label(frame13, text=k, fg="black", bg="white", relief="solid",
                  font=("Calisto MT", 30)).place(x=900, y=250)
            Label(frame13, text=m, fg="black", bg="white", relief="solid",
                  font=("Calisto MT", 30)).place(x=900, y=450)


def frame13_open():
    show_frame(frame13)
    Subscribers_list()


# Companies to Release their Company Notification ( Frame - 14)

bg14 = ImageTk.PhotoImage(file="image7.jpg")
Label(frame14, image=bg14).place(x=0, y=0, relwidth=1, relheight=1)
frame14_list = []


def frame14_company():
    f = open('company_info.csv', 'r')
    reader = csv.reader(f)
    global frame14_list, frame14_type, frame2_company_name
    for row in reader:
        if frame2_company_name == row[0]:
            frame14_list = row[6].split(',')
            frame14_type = ttk.Combobox(frame14, values=frame14_list, textvariable=frame14_b, font=("Arial", 25)).place(
                x=850, y=350)
            frame14_b.set('Select Post')
            show_frame(frame14)


frame14_str = 'Release Notifications for Your Company ' + frame2_company_name
frame14_l1 = Label(frame14, text=frame14_str, fg="white", bg="green",
                   font=("Arial", 35, "bold")).place(x=400,
                                                     y=30)
frame14_Vacancies = Label(frame14, text=" Type of Vacancy ", fg="white", bg="black",
                          font=("Baskerville Old Face", 25, "bold")).place(x=425, y=250)

frame14_posts = Label(frame14, text=" Post Available For ", fg="white", bg="black",
                      font=("Baskerville Old Face", 25, "bold")).place(x=425, y=350)
frame14_no_ofVacancies = Label(frame14, text=" Vacancies Intake ", fg="white", bg="black",
                               font=("Baskerville Old Face", 25, "bold")).place(x=425, y=450)


def message():
    l = []
    global frame2_company_name
    f = open('officer.csv', 'r')
    reader = csv.reader(f)
    for word in reader:
        if frame2_company_name == word[1]:
            word[4] = 'yes'
            found = 1
        l.append(word)
    if found == 0:
        messagebox.showinfo('Message', 'Company Not Found')
    else:
        g = open("officer.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(l)
        g.close()
    frame14_z = 'Your Company ' + frame2_company_name + ' has released Notifications Successfully'
    messagebox.showinfo('Notifications', frame14_z)
    frame14_a.set('')
    frame14_b.set('')
    frame14_c.set('')


o = [' Job  ', 'Internship ']
frame14_a = StringVar()
frame14_info = ttk.Combobox(frame14, values=o, textvariable=frame14_a, font=("Arial", 25)).place(x=850, y=250)
frame14_a.set("Select type")
frame14_b = StringVar()
frame14_c = StringVar()
frame14_entry = Entry(frame14, textvariable=frame14_c, font=("Arial", 25)).place(x=850, y=450)
frame14_submit = Button(frame14, text=" Submit ", fg="blue", bg="white", font=("caliber", 14, "bold"),
                        command=message).place(x=700, y=580)
frame14_back = Button(frame14, text=" Go Back ", fg="blue", bg="white", font=("caliber", 14, "bold"),
                      command=lambda: show_frame(frame4)).place(x=700, y=690)

# Company to Change their Password (Frame - 18)
bg18 = ImageTk.PhotoImage(file="20220320_180032.png")
Label(frame18, image=bg18).place(x=0, y=0, relwidth=1, relheight=1)


def frame18_change_pass(w, r):
    g = open("officer.csv", 'r')
    reading = csv.reader(g)
    found = 0
    global frame2_company_id
    l = []
    for info in reading:
        if info[0] == frame2_company_id:
            info[2] = r
            found = 1
        l.append(info)
    g.close()
    if found == 0:
        messagebox.showwarning('Password Change', 'Check your Password')
    else:
        f = open("officer.csv", "w", newline='')
        messagebox.showinfo('Password Change', 'Your Password Changed Successfully')
        csvw = csv.writer(f)
        csvw.writerows(l)
        f.close()
    frame18_old_pass1.delete(0, END)
    frame18_new_pass1.delete(0, END)


def frame18_m_pass():
    frame18_set_old_pass = frame18_o_pass.get()
    frame18_set_pass = frame18_c_pass.get()
    frame18_change_pass(frame18_set_old_pass, frame18_set_pass)


frame18_change_label = Label(frame18, text=" Set Your New Password ", fg="yellow", bg="black", relief="solid",
                             font=("Centaur", 25)).place(x=600, y=50)
frame18_old_pass = Label(frame18, text="Enter Old Password", fg="black", bg="pink", relief="solid",
                         font=("Arial", 20, "bold")).place(x=400, y=150)
frame18_new_pass = Label(frame18, text="Enter New Password", fg="black", bg="pink", relief="solid",
                         font=("Arial", 20, "bold")).place(x=400, y=300)

frame18_o_pass = StringVar()
frame18_c_pass = StringVar()
frame18_old_pass1 = Entry(frame18, show="*", textvariable=frame18_o_pass, bg="white", font=("Arial", 15), width=10)
frame18_old_pass1.pack()
frame18_old_pass1.place(x=850, y=150)
frame18_new_pass1 = Entry(frame18, show="*", textvariable=frame18_c_pass, bg="white", font=("Arial", 15), width=10)
frame18_new_pass1.pack()
frame18_new_pass1.place(x=850, y=300)
frame18_change = Button(frame18, text="Change", fg="white", bg="sky blue", font=("Baskerville Old Face", 10, "bold"),
                        width=15,
                        command=frame18_m_pass).place(x=650, y=400)
frame18_back = Button(frame18, text="Go Back ", fg="blue", bg="white", font=("caliber", 10, "bold"), width=15,
                      command=lambda: show_frame(frame4)).place(x=650, y=500)

# Aspirant Interface (Frame - 3)
bg3 = ImageTk.PhotoImage(file="Pro1.jpeg")
Label(frame3, image=bg3).place(x=0, y=0, relwidth=1, relheight=1)
frame3_label = Label(frame3, text="** WELCOME **", font=("Algerian", 50, "bold"), fg='navajo white').place(x=500, y=150)
frame3_title = Label(frame3, text=" Choose the Option Below ", fg="white", bg="green",
                     font=("Baskerville Old Face", 35)).place(x=450, y=300)
frame3_signin = Button(frame3, text=" SIGN IN ", font=('arial', 25), command=lambda: show_frame(frame5)).place(x=360,
                                                                                                               y=460)
frame3_signup = Button(frame3, text=" SIGN UP ", font=('arial', 25), command=lambda: show_frame(frame10)).place(x=900,
                                                                                                                y=460)
frame3_back = Button(frame3, text=" GO BACK ", font=('arial', 15), fg='red', command=lambda: show_frame(frame1)).place(
    x=675, y=650)
#  Company Interface ( For Frame - 4  )
bg4 = ImageTk.PhotoImage(file='20220320_180253.png')
Label(frame4, image=bg4).place(x=0, y=0, relwidth=1, relheight=1)
frame4_title = Label(frame4, text='** Choose The Option Below **', fg='black', bg='red',
                     font=("Baskerville Old Face", 35, "bold")).place(x=485, y=20)
frame4_btn1 = Button(frame4, text=" View Applicants ", fg="blue", bg="white", font=("Algerian", 20, "bold"),
                     command=frame13_open).place(x=590, y=140)
frame4_btn2 = Button(frame4, text=" Release Notifications ", fg="blue", bg="white", font=("Algerian", 20, "bold"),
                     command=frame14_company).place(x=560, y=250)
frame4_btn3 = Button(frame4, text=" Update Vacancies ", fg="blue", bg="white", font=("Algerian", 20, "bold"),
                     command=lambda: show_frame(frame8)).place(x=590, y=360)
frame4_btn4 = Button(frame4, text=" Offer Letter ", fg="blue", bg="white", font=("Algerian", 20, "bold"),
                     command=lambda: show_frame(frame8)).place(x=605, y=470)
frame4_btn5 = Button(frame4, text=" Change Password ", fg="blue", bg="white", font=("Algerian", 20, "bold"),
                     command=lambda: show_frame(frame18)).place(x=590, y=580)
frame4_goback_btn = Button(frame4, text=" Log Out ", fg="white", bg="black", font=("caliber", 17, "bold"),
                           command=lambda: show_frame(frame2)).place(x=670, y=690)
# For Aspirant To View their Profile ( Frame - 7)
bg7 = ImageTk.PhotoImage(file='20220319_203638.png')
Label(frame7, image=bg7).place(x=0, y=0, relwidth=1, relheight=1)
get_aspirant_id = ''


def aspirant_info(z):
    l = open('Pro Pan.csv', 'r')
    book_reader = csv.reader(l)
    for row in book_reader:
        if z == row[0]:
            output = "\n->Id : %s \n\n->Name : %s \n\n->Gender : %s\n\n->DOB: %s\n\n->Qualification : %s \n\n->Specialisation: %s\n\n ->Year of passing out: %s \n\n->Percentage of Marks : %s \n\n ->Company interested: %s \n\n ->Expected package: %s \n\n->Courses did if any: %s\n\n" % (
                row[0], row[1], row[6], row[11], row[9], row[2], row[5], row[8], row[4], row[3], row[10])
            Label(frame7, text=" YOUR PROFILE ", fg="blue", bg="white", relief="solid",
                  font=("Baskerville Old Face", 25, "bold")).place(x=650, y=20)
            frame7_Aspirant_info = Label(frame7, text=output, fg="black", bg="light gray", relief="solid",
                                         font=("Calisto MT", 15))
            frame7_Aspirant_info.place(x=570, y=100)
            break


def get_aspirant_info():
    id = get_aspirant_id
    aspirant_info(id)


def frame7_open():
    get_aspirant_info()
    show_frame(frame7)


frame7_back = Button(frame7, text=" Go Back ", fg="white", bg="black", font=("Algerian", 18, "bold"), width=15,
                     command=lambda: show_frame(frame6)).place(x=650, y=700)
#  Aspirant Sign_in ( Frame - 5)
bg5 = ImageTk.PhotoImage(file='20220324_195656.jpg')
Label(frame5, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)


def ex_sinfo(a, b):
    f = open('Pro Pan.csv', 'r')
    reading = csv.reader(f)
    for word in reading:
        if a == word[0] and b == word[7]:
            frame5_stu_id.delete(0, END)
            frame5_stu_pass.delete(0, END)
            show_frame(frame6)
            break
    else:
        messagebox.showerror('Warning', 'In-Correct Credentials')
        frame5_stu_id.delete(0, END)
        frame5_stu_pass.delete(0, END)


# Creating Functionality Keys For User Interface:
def get_sinfo():
    global get_aspirant_id
    set_info = f"{frame5_p.get()}"
    get_aspirant_id = set_info
    set_password = f"{frame5_i.get()}"
    ex_sinfo(set_info, set_password)


frame5_title = Label(frame5, text=" Welcome to Aspirant Portal ", fg="white", bg="green", font=("Algerian", 20),
                     width=50).place(x=350, y=50)

frame5_Id = Label(frame5, text=" Enter Your ID ", fg="black", bg="pink", relief="solid",
                  font=("Arial", 25, "bold")).place(x=500, y=150)
frame5_password = Label(frame5, text=" Enter Password ", fg="black", bg="pink", relief="solid",
                        font=("Arial", 25, "bold")).place(x=500, y=300)

# The Variables we require to Get Student details(initialization):

frame5_p = StringVar()
frame5_i = StringVar()
#  Details Required From the User:
frame5_stu_id = Entry(frame5, textvariable=frame5_p, bg="white", font=("Arial", 25), width=12)
frame5_stu_id.pack()
frame5_stu_id.place(x=850, y=150)
frame5_stu_pass = Entry(frame5, show='*', textvariable=frame5_i, bg="white", font=("Arial", 25), width=12)
frame5_stu_pass.pack()
frame5_stu_pass.place(x=850, y=300)
frame5_browse = Button(frame5, text=" Login ", fg="white", bg="red", font=("Baskerville Old Face", 14, "bold"),
                       width=15,
                       command=get_sinfo).place(x=650, y=450)
frame5_ext_but = Button(frame5, text=" Exit ", fg="white", bg="black", font=("caliber", 14, "bold"), width=15,
                        command=exit).place(x=760, y=650)
frame5_back5 = Button(frame5, text="Go Back ", fg="white", bg="black", font=("caliber", 14, "bold"), width=15,
                      command=lambda: show_frame(frame3)).place(x=560, y=650)
# Aspirants to View Company Notifications (For Frame - 15)
bg15 = ImageTk.PhotoImage(file='20220324_195554.jpg')
Label(frame15, image=bg15).place(x=0, y=0, relwidth=1, relheight=1)
frame15_feedback = Label(frame15)
frame15_feedback1 = Label(frame15)
frame15_feedback2 = Label(frame15)


def all_clear1():
    frame15_feedback.destroy()
    frame15_feedback1.destroy()
    frame15_feedback2.destroy()
    msg1.destroy()
    msg2.destroy()
    msg3.destroy()
    msg4.destroy()
    msg5.destroy()
    msg6.destroy()
    msg7.destroy()
    msg8.destroy()
    msg9.destroy()
    msg10.destroy()


def all_clear2():
    messagebox.showinfo('Feed Back', 'Thank You For Your Feed Back')
    frame15_feedback.destroy()
    frame15_feedback1.destroy()
    frame15_feedback2.destroy()
    msg8.destroy()
    msg9.destroy()
    msg10.destroy()


def response():
    global msg1, msg2, msg3, msg4, msg5, msg6, msg7
    msg1 = Label(frame15, text="->May We Know the Reason for your Deny !", fg='black', relief="solid",
                 font=("Calibri", 15))
    msg1.pack()
    msg1.place(x=620, y=500)
    msg2 = Radiobutton(frame15, text='Interested in Higher Education', value=1, font=("Calibri", 10),
                       command=clicked)
    msg2.pack()
    msg2.place(x=700, y=550)
    msg3 = Radiobutton(frame15, text='Interested in Start Up', font=("Calibri", 10), value=2,
                       command=clicked)
    msg3.pack()
    msg3.place(x=700, y=580)
    msg4 = Radiobutton(frame15, text='Interested in Entrepreneurship', font=("Calibri", 10), value=3,
                       command=clicked)
    msg4.pack()
    msg4.place(x=700, y=610)
    msg5 = Radiobutton(frame15, text='Interested in PartnerShip', font=("Calibri", 10), value=3,
                       command=clicked)
    msg5.pack()
    msg5.place(x=700, y=640)
    msg6 = Radiobutton(frame15, text='Other Reasons', font=("Calibri", 10), value=4, command=clicked)
    msg6.pack()
    msg6.place(x=700, y=670)
    msg7 = Button(frame15, text='clear', font=("Calibri", 15), command=all_clear1)
    msg7.pack()
    msg7.place(x=1000, y=600)


def show_stinfo():
    global msg8, msg9, msg10
    msg8 = Label(frame15, text="May We Know the Reason", fg="green", bg="white",
                 relief="solid",
                 font=("Calisto MT", 15, "bold"))
    msg8.pack()
    msg8.place(x=620, y=400)
    msg9 = Button(frame15, text="Yes", fg="white", bg="blue", relief="solid",
                  font=("calibri", 10, "bold"), command=response)
    msg9.pack()
    msg9.place(x=690, y=450)
    msg10 = Button(frame15, text="No", fg="white", bg="blue", relief="solid",
                   font=("calibri", 10, "bold"), command=all_clear2)
    msg10.pack()
    msg10.place(x=790, y=450)


def feed_backmsg():
    global msg
    msg = Label(frame15, text="Thank you \n We will Get Back to you Soon", fg="blue", bg="white", relief="solid",
                font=("Baskerville Old Face", 20, "bold"))
    msg.pack()
    msg.place(x=580, y=500)
    Button(frame15, text='clear', font=("Calibri", 10), command=all_clear2).place(x=740, y=600)


def frame15_company():
    show_frame(frame15)
    s = []
    m = ' Job notifications released by your interested companies '
    n = ' Job notifications released by your interested companies '
    f = open('officer.csv', 'r')
    f_reader = csv.reader(f)
    g = open('Pro Pan.csv', 'r')
    g_reader = csv.reader(g)
    global get_aspirant_id
    for i in g_reader:
        if get_aspirant_id == i[0]:
            s = i[4].split()
    for j in f_reader:
        if j[1] in s and j[4] == 'yes':
            m = m + ' ' + j[1]
    if m == n:
        m = ' The Companies which You are Interested has not  Released any Job Notifications till now'
    frame15_label = Label(frame15, text=m, fg="black", bg="gold", relief="solid",
                          font=("Lucida Calligraphy", 20, "bold")).place(x=250, y=50)
    frame15_feedback = Label(frame15, text="Are You Interested in Joining This Company", fg="green",
                             bg="white",
                             relief="solid",
                             font=("Calisto MT", 15, "bold"))
    frame15_feedback.pack()
    frame15_feedback.place(x=550, y=150)
    frame15_feedback1 = Button(frame15, text="Yes", fg="white", bg="blue", relief="solid",
                               font=("calibri", 10, "bold"), command=feed_backmsg)
    frame15_feedback1.pack()
    frame15_feedback1.place(x=670, y=250)
    frame15_feedback2 = Button(frame15, text="No", fg="white", bg="blue", relief="solid",
                               font=("calibri", 10, "bold"), command=show_stinfo)
    frame15_feedback2.pack()
    frame15_feedback2.place(x=810, y=250)
    Button(frame15, text="Go Back ", fg="white", bg="black", font=("caliber", 10, "bold"), width=15,
           command=lambda: show_frame(frame6)).place(x=680, y=750)


# For Frame 6 :(Sign in) Aspirant Information Interface
bg6 = ImageTk.PhotoImage(file="20220320_175544.jpg")
Label(frame6, image=bg6).place(x=0, y=0, relwidth=1, relheight=1)
frame6_title = Label(frame6, text='ASPIRANT PORTAL', fg='black', bg='yellow',
                     font=("Algerian", '35', "bold")).place(x=500, y=20)
frame6_btn1 = Button(frame6, text=" VIEW YOUR PROFILE ", fg='blue', bg='teal', font=("Calibri", 30, "bold"),
                     command=frame7_open).place(x=250, y=200)
frame6_btn2 = Button(frame6, text=" COMPANY INFORMATION ", fg='blue', bg='teal', font=("Calibri", 30, "bold"),
                     command=lambda: show_frame(frame11)).place(x=230, y=400)
frame6_btn3 = Button(frame6, text=" COMPANY NOTIFICATION ", fg='blue', bg='teal', font=("Calibri", 30, "bold"),
                     command=frame15_company).place(x=230, y=600)
frame6_btn4 = Button(frame6, text=" PLACEMENT INFORMATION ", fg='blue', bg='teal', font=("Calibri", 30, "bold"),
                     command=lambda: show_frame(frame15)).place(x=800, y=200)
frame6_btn5 = Button(frame6, text=" UPDATE YOUR PROFILE ", fg='blue', bg='teal', font=("Calibri", 30, "bold"),
                     command=lambda: show_frame(frame12)).place(x=790, y=400)
frame6_btn6 = Button(frame6, text=" INTERNSHIPS ", fg='blue', bg='teal', font=("Calibri", 30, "bold"),
                     command=lambda: show_frame(frame17)).place(x=790, y=600)
frame6_back6 = Button(frame6, text=" LOG OUT  ", fg="honeydew", bg='black', font=("caliber", 15, "bold"),
                      command=lambda: show_frame(frame5)).place(x=660, y=750)

# For Company to Update Vacancies ( Frame - 8)
bg8 = ImageTk.PhotoImage(file="20220320_175744.png")
Label(frame8, image=bg8).place(x=0, y=0, relwidth=1, relheight=1)
frame8_title = Label(frame8, text=' Update Your Company Vacancies ', font=("Algerian", 25, "bold"), fg='green').place(
    x=500, y=20)


def change_pass(w, r, s):
    g = open("company_info.csv", 'r')
    reading = csv.reader(g)
    found = 0
    l = []
    for info in reading:
        if info[0] == w:
            info[6] = r
            info[7] = s
            found = 1
        l.append(info)
    g.close()
    if found == 0:
        messagebox.showinfo('Message', 'Company Not Found')
    else:
        g = open("company_info.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(l)
        g.close()
    messagebox.showinfo("Vacancies Updated", ' Vacancies Updated Successfully ')
    old_pass1.delete(0, END)
    new_pass1.delete(0, END)
    vacancies1.delete(0, END)


def m_pass():
    set_opass = f"{o_pass.get()}"
    set_pass = f"{c_pass.get()}"
    set_vac = f"{vacancies.get()}"
    change_pass(set_opass, set_pass, set_vac)


old_pass = Label(frame8, text=" Enter Company Name ", fg="black", bg="pink", relief="solid",
                 font=("Arial", 15, "bold")).place(x=400, y=200)
new_pass = Label(frame8, text=" Update Vacancies ", fg="black", bg="pink", relief="solid",
                 font=("Arial", 15, "bold")).place(x=400, y=300)
num_of_vacancies = Label(frame8, text="Number of vacancies ", fg="black", bg="pink", relief="solid",
                         font=("Arial", 15, "bold")).place(x=400, y=400)
o_pass = StringVar()
c_pass = StringVar()
vacancies = StringVar()
old_pass1 = Entry(frame8, textvariable=o_pass, bg="white", font=("Arial", 15), width=20)
old_pass1.pack()
old_pass1.place(x=850, y=200)
new_pass1 = Entry(frame8, textvariable=c_pass, bg="white", font=("Arial", 15), width=30)
new_pass1.pack()
new_pass1.place(x=850, y=300)
vacancies1 = Entry(frame8, textvariable=vacancies, bg="white", font=("Arial", 15), width=20)
vacancies1.pack()
vacancies1.place(x=850, y=400)

update = Button(frame8, text=" Update ", fg="white", bg="sky blue", font=("Baskerville Old Face", 14, "bold"),
                width=15,
                command=m_pass).place(x=700, y=600)
frame8_back = Button(frame8, text="Go Back ", fg="blue", bg="white", font=("caliber", 14, "bold"), width=15,
                     command=lambda: show_frame(frame4)).place(x=700, y=675)
# Aspirant Registration Form ( For Frame 10)


bg10 = ImageTk.PhotoImage(file='20220320_180358.png')
Label(frame10, image=bg10).place(x=0, y=0, relwidth=1, relheight=1)


def up_info():
    dict_data = []
    dz = []
    dz = dz + [x1.get()]
    dz = dz + [y1.get()]
    dz = dz + [a1.get()]
    dz = dz + [b1.get()]
    dz = dz + [c1.get()]
    dz = dz + [d1.get()]
    dz = dz + [f1.get()]
    dz = dz + [g1.get()]
    dz = dz + [h1.get()]
    dz = dz + [i1.get()]
    dz = dz + [j1.get()]
    dz = dz + [k1.get()]
    dict_data = dict_data + [dz]
    f = open("Pro Pan.csv", "a", newline="")
    wr = csv.writer(f)
    for word in dict_data:
        wr.writerow(word)
        messagebox.showinfo("Updated Result", " You have Registered Successfully ")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    c1.set('')
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)


frame10_title = Label(frame10, text=' Provide the Details Below ', font=("Algerian", 20, "bold"), bg='red',
                      fg='gold').place(x=500, y=10)
l1 = Label(frame10, text=" Enter Your ID : ", font=("Arial", 15, "bold")).place(x=450, y=100)
x1 = StringVar()
e1 = Entry(frame10, textvariable=x1, bg="white", font=("Arial", 15, "bold"), width=18)
e1.pack()
e1.place(x=850, y=100)
l2 = Label(frame10, text=" Enter Your Name :", font=("Arial", 15, "bold")).place(x=450, y=150)
y1 = StringVar()
e2 = Entry(frame10, textvariable=y1, bg="white", font=("Arial", 15, "bold"), width=18)
e2.pack()
e2.place(x=850, y=150)
l3 = Label(frame10, text="Specialization  :", font=("Arial", 15, "bold")).place(x=450, y=200)
a1 = StringVar()
e3 = Entry(frame10, textvariable=a1, bg="white", font=("Arial", 15, "bold"), width=18)
e3.pack()
e3.place(x=850, y=200)
l4 = Label(frame10, text=" Package :", font=("Arial", 15, "bold")).place(x=450, y=250)
b1 = StringVar()
e4 = Entry(frame10, textvariable=b1, bg="white", font=("Arial", 15, "bold"), width=18)
e4.pack()
e4.place(x=850, y=250)
l5 = Label(frame10, text="Interested Company  :", font=("Arial", 15, "bold")).place(x=450, y=300)
c1 = StringVar()
company_list = ['Infosys', 'Larsen&Toubro', 'Wipro', 'Huawei', 'Flipkart', 'Tech Mahindra', 'Cognizant', 'Mindtree',
                'TCS', 'IBM', 'Accenture', 'Microsoft', 'Apple Inc', 'Google', 'Amazon', 'The Coca Cola Co.',
                'Pepsi Co.', 'Mahindra Group', 'Procter&Gamble', 'Sony Corporation', 'Samsung', 'TATA Group',
                'Nestle', 'Aditya Birla Group', 'Hewlett Packard Enterprise', 'Deloitte', 'Dell', 'Unilever',
                'CITI Group', 'LTI', 'Nike Inc', 'Johnson&Johnson', 'Adidas']
company_info = ttk.Combobox(frame10, values=company_list, textvariable=c1, font=("Arial", 13, "bold")).place(x=850,
                                                                                                             y=300)
c1.set("Select Company")
l6 = Label(frame10, text=" Year of passing out : ", font=("Arial", 15, "bold")).place(x=450, y=350)
d1 = StringVar()
e6 = Entry(frame10, textvariable=d1, bg="white", font=("Arial", 15, "bold"), width=18)
e6.pack()
e6.place(x=850, y=350)
l7 = Label(frame10, text="Gender:", font=("Arial", 15, "bold")).place(x=450, y=400)
f1 = StringVar()
e7 = Entry(frame10, textvariable=f1, bg="white", font=("Arial", 15, "bold"), width=18)
e7.pack()
e7.place(x=850, y=400)
l8 = Label(frame10, text=" Set your password : ", font=("Arial", 15, "bold")).place(x=450, y=450)
g1 = StringVar()
e8 = Entry(frame10, textvariable=g1, bg="white", font=("Arial", 15, "bold"), width=18)
e8.pack()
e8.place(x=850, y=450)
l9 = Label(frame10, text=" Percentage of marks : ", font=("Arial", 15, "bold")).place(x=450, y=500)
h1 = StringVar()
e9 = Entry(frame10, textvariable=h1, bg="white", font=("Arial", 15, "bold"), width=18)
e9.pack()
e9.place(x=850, y=500)
l10 = Label(frame10, text=" Qualification : ", font=("Arial", 15, "bold")).place(x=450, y=550)
i1 = StringVar()
e10 = Entry(frame10, textvariable=i1, bg="white", font=("Arial", 15, "bold"), width=18)
e10.pack()
e10.place(x=850, y=550)
l11 = Label(frame10, text=" Courses did if any : ", font=("Arial", 15, "bold")).place(x=450, y=600)
j1 = StringVar()
e11 = Entry(frame10, textvariable=j1, bg="white", font=("Arial", 15, "bold"), width=18)
e11.pack()
e11.place(x=850, y=600)
l12 = Label(frame10, text=" DOB : ", font=("Arial", 15, "bold")).place(x=450, y=650)
k1 = StringVar()
e12 = Entry(frame10, textvariable=k1, bg="white", font=("Arial", 15, "bold"), width=18)
e12.pack()
e12.place(x=850, y=650)

frame10_update = Button(frame10, text=" Register ", fg="white", bg="sky blue",
                        font=("Baskerville Old Face", 14, "bold"),
                        width=15,
                        command=up_info).place(x=1200, y=450)
frame10_back10 = Button(frame10, text=" Go Back ", fg="blue", bg="white", font=("caliber", 14, "bold"), width=15,
                        command=lambda: show_frame(frame3)).place(x=1200, y=550)

# For Aspirant to View Company Information and Subscription ( Frame - 11)


frame11_bg11 = ImageTk.PhotoImage(file="20220320_180146.png")
Label(frame11, image=frame11_bg11).place(x=0, y=0, relwidth=1, relheight=1)
frame11_company_name = ''
frame11_subscribe = Button(frame11)
frame11_subscribed = Button(frame11)


def frame11_unsubscribe():
    s = []
    global frame11_subscribe
    f = open('officer.csv', 'r')
    officer_reader = csv.reader(f)
    global frame11_company_get_vacancies, get_aspirant_id
    found = 0
    for word in officer_reader:
        if frame11_company_name == word[1]:
            s = word[3].split()
            print(s)
            s.remove(get_aspirant_id)
            found = 1
            frame11_subscribed.place_forget()
            frame11_subscribe.place(x=1100, y=450)
    f.close()
    if found == 1:
        messagebox.showinfo('Subscription', 'You have Un-Subscribed the Company Successfully')
        g = open("officer.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(s)
        g.close()


frame11_subscribed = Button(frame11, text=' UN-SUBSCRIBE ', fg='black', bg='red', font=("caliber", 17, "bold"),
                            command=frame11_unsubscribe)
frame11_company_get_vacancies = ''


def frame11_msg():
    global frame11_company_name
    l = []
    p = []
    s = ''
    found = 0
    f = open('officer.csv', 'r')
    officer_reader = csv.reader(f)
    global frame11_company_get_vacancies, get_aspirant_id
    for word in officer_reader:
        if frame11_company_get_vacancies == word[1]:
            p = word[3].split()
            print(p)
            if get_aspirant_id not in p:
                s = word[3]
                word[3] = s + ' ' + get_aspirant_id
                found = 1
            l.append(word)
        else:
            messagebox.showinfo('Subscription', 'You have Already Subscribed for the Company ')
            break
    f.close()
    if found == 1:
        g = open("officer.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(l)
        g.close()
    r = []
    m = open('Pro Pan.csv', 'r')
    read = csv.reader(m)
    for j in read:
        if get_aspirant_id == j[0] and get_aspirant_id in p:
            j[4] = j[4] + ' ' + frame11_company_get_vacancies
            found = 1
        r.append(j)
    m.close()
    if found == 1:
        g = open("Pro Pan.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(r)
        g.close()
        messagebox.showinfo(' Subscription ',
                            'You have Subscribed for ' + frame11_company_name + ' Company Successfully')
        frame11_subscribe.place_forget()
        frame11_subscribed.place(x=1100, y=450)


frame11_subscribe = Button(frame11, text=' SUBSCRIBE ', fg='black', bg='red', font=("caliber", 17, "bold"),
                           command=frame11_msg)
frame11_company_info = Label(frame11)


def exc_info(z):
    f = open('company_info.csv', 'r')
    book_reader = csv.reader(f)
    for word in book_reader:
        if z == word[0]:
            output = "\n->Company name : %s \n\n->Eligibility Criteria : %s \n\n->Skills required : %s \n\n->Maximum package : %s \n\n->Minimum package : %s \n\n->Technical Skills : %s \n\n->Posts Available : %s  \n\n->Number of Vacancies : %s" % (
                word[0], word[1], word[2], word[3], word[4], word[5], word[6], word[7])
            Label(frame11, text=" Required Company Information ", fg="blue", bg="white", relief="solid",
                  font=("Baskerville Old Face", 20, "bold")).place(x=550, y=270)
            global frame11_company_info
            frame11_company_info = Label(frame11, text=output, fg="black", bg="white", relief="solid",
                                         font=("Calisto MT", 10))
            frame11_company_info.place(x=450, y=350)
            frame11_subscribe.place(x=1100, y=450)
            break


def get_Cinfo():
    global frame11_company_name, frame11_company_get_vacancies
    set_cname = f"{x.get()}"
    frame11_company_get_vacancies = set_cname
    frame11_company_name = set_cname
    exc_info(set_cname)


def frame6_open():
    global frame11_company_info
    frame11_company_info.place_forget()
    x.set('')
    frame11_subscribe.place_forget()
    show_frame(frame6)


frame11_title = Label(frame11, text=" COMPANY INFORMATION ", fg="white", bg="green", font=("Arial", 15, "bold")).place(
    x=610, y=50)
frame11_company_name = Label(frame11, text=" Enter The Company NAME ", fg="black", bg="pink", relief="solid",
                             font=("Castellar", 18, "bold")).place(x=200, y=120)
x = StringVar()
company_list = ['Infosys', 'Larsen&Toubro', 'Wipro', 'Huawei', 'Flipkart', 'Tech Mahindra', 'Cognizant', 'Mindtree',
                'TCS', 'IBM', 'Accenture', 'Microsoft', 'Apple Inc', 'Google', 'Amazon', 'The Coca Cola Co.',
                'Pepsi Co.', 'Mahindra Group', 'Procter&Gamble', 'Sony Corporation', 'Samsung', 'TATA Group',
                'Nestle', 'Aditya Birla Group', 'Hewlett Packard Enterprise', 'Deloitte', 'Dell', 'Unilever',
                'CITI Group', 'LTI', 'Nike Inc', 'Johnson&Johnson', 'Adidas']
company_info = ttk.Combobox(frame11, values=company_list, textvariable=x, font=("Arial", 20, "bold")).place(x=750,
                                                                                                            y=120)
x.set("Select Company")
frame11_browse = Button(frame11, text="Get Company Info", fg="white", bg="sky blue",
                        font=("Castellar", 10, "bold"), width=25, command=get_Cinfo).place(x=550, y=200)
frame11_back = Button(frame11, text="Go Back ", fg="white", bg="black", font=("Algerian", 18, "bold"), width=15,
                      command=frame6_open).place(x=570, y=650)

# Frame 12 Update Aspirant information
frame12_bg12 = ImageTk.PhotoImage(file="Image2.jpg")
Label(frame12, image=frame12_bg12).place(x=0, y=0, relwidth=1, relheight=1)
f12_qualification = ''
f12_Specialisation = ''
f12_year = ''
f12_percentage = ''
f12_courses = ''
f12_companies = ''
f12_package = ''
f12_password = ''

frame12_label12 = Label(frame12, text="UPDATE INFORMATION", fg="white", bg="green", font=("Arial", 15, "bold")).place(
    x=650,
    y=20)


def frame12_update_profile():
    l = []
    found = 0
    f = open('Pro Pan.csv', 'r')
    aspirant_reader = csv.reader(f)
    for word in aspirant_reader:
        if get_aspirant_id == word[0]:
            word[9] = f12_qualification
            word[2] = f12_Specialisation
            word[5] = f12_year
            word[8] = f12_percentage
            word[10] = f12_courses
            word[4] = f12_companies
            word[3] = f12_package
            word[7] = f12_password
            messagebox.showinfo('Updated Message', 'Your Profile has been Updated Successfully')
            found = 1
        l.append(word)
    f.close()
    if found == 0:
        messagebox.showinfo('Company', "Data Not Found")
    else:
        g = open("Pro Pan.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(l)
        frame12_e1.delete(0, END)
        frame12_e2.delete(0, END)
        frame12_e3.delete(0, END)
        frame12_e4.delete(0, END)
        frame12_e5.delete(0, END)
        e1.set('')
        frame12_e7.delete(0, END)
        frame12_e8.delete(0, END)
        g.close()


def frame12_get_info():
    global f12_qualification, f12_Specialisation, f12_year, f12_percentage, f12_courses, f12_companies, f12_package, f12_password
    f12_qualification = f"{x1.get()}"
    f12_Specialisation = f"{y1.get()}"
    f12_year = f"{a1.get()}"
    f12_percentage = f"{b1.get()}"
    f12_courses = f"{c1.get()}"
    f12_companies = f"{e1.get()}"
    f12_package = f"{f1.get()}"
    f12_password = f"{g1.get()}"
    frame12_update_profile()


frame12_l1 = Label(frame12, text=" Qualification : ", font=("Arial", 15, "bold")).place(x=580, y=100)
x1 = StringVar()
frame12_e1 = Entry(frame12, textvariable=x1, bg="white", font=("Arial", 15, "bold"), width=15)
frame12_e1.pack()
frame12_e1.place(x=850, y=100)
frame12_l2 = Label(frame12, text=" Specialisation : ", font=("Arial", 15, "bold")).place(x=580, y=180)
y1 = StringVar()
frame12_e2 = Entry(frame12, textvariable=y1, bg="white", font=("Arial", 15, "bold"), width=15)
frame12_e2.pack()
frame12_e2.place(x=850, y=180)
frame12_l3 = Label(frame12, text="Year of passing out :", font=("Arial", 15, "bold")).place(x=580, y=260)
a1 = StringVar()
frame12_e3 = Entry(frame12, textvariable=a1, bg="white", font=("Arial", 15, "bold"), width=15)
frame12_e3.pack()
frame12_e3.place(x=850, y=260)
frame12_l4 = Label(frame12, text="Percentage of marks :", font=("Arial", 15, "bold")).place(x=580, y=340)
b1 = StringVar()
frame12_e4 = Entry(frame12, textvariable=b1, bg="white", font=("Arial", 15, "bold"), width=15)
frame12_e4.pack()
frame12_e4.place(x=850, y=340)
frame12_l5 = Label(frame12, text="Courses done if any :", font=("Arial", 15, "bold")).place(x=580, y=420)
c1 = StringVar()
frame12_e5 = Entry(frame12, textvariable=c1, bg="white", font=("Arial", 15, "bold"), width=15)
frame12_e5.pack()
frame12_e5.place(x=850, y=420)
frame12_l6 = Label(frame12, text="Companies Interested:", font=("Arial", 15, "bold")).place(x=580, y=500)
e1 = StringVar()
company_list = ['Infosys', 'Larsen&Toubro', 'Wipro', 'Huawei', 'Flipkart', 'Tech Mahindra', 'Cognizant', 'Mindtree',
                'TCS', 'IBM', 'Accenture', 'Microsoft', 'Apple Inc', 'Google', 'Amazon', 'The Coca Cola Co.',
                'Pepsi Co.', 'Mahindra Group', 'Procter&Gamble', 'Sony Corporation', 'Samsung', 'TATA Group',
                'Nestle', 'Aditya Birla Group', 'Hewlett Packard Enterprise', 'Deloitte', 'Dell', 'Unilever',
                'CITI Group', 'LTI', 'Nike Inc', 'Johnson&Johnson', 'Adidas']
frame12_company_info = ttk.Combobox(frame12, values=company_list, textvariable=e1, font=("Arial", 10, "bold")).place(
    x=850, y=500)
e1.set("Select Company")
frame12_l7 = Label(frame12, text="Expected package :", font=("Arial", 15, "bold")).place(x=580, y=580)
f1 = StringVar()
frame12_e7 = Entry(frame12, textvariable=f1, bg="white", font=("Arial", 15, "bold"), width=15)
frame12_e7.pack()
frame12_e7.place(x=850, y=580)
frame12_l8 = Label(frame12, text="Modify password :", font=("Arial", 15, "bold")).place(x=580, y=660)
g1 = StringVar()
frame12_e8 = Entry(frame12, show='*', textvariable=g1, bg="white", font=("Arial", 15, "bold"), width=15)
frame12_e8.pack()
frame12_e8.place(x=850, y=660)

frame12_update = Button(frame12, text="Update Profile", fg="white", bg="sky blue",
                        font=("Baskerville Old Face", 14, "bold"),
                        command=frame12_get_info).place(x=790, y=720)
frame12_back12 = Button(frame12, text="Go Back ", fg="blue", bg="white", font=("caliber", 14, "bold"),
                        command=lambda: show_frame(frame6)).place(x=600, y=720)
# Company Interface (Frame - 16)

bg16 = ImageTk.PhotoImage(file="20220320_175835.png")
Label(frame16, image=bg16).place(x=0, y=0, relwidth=1, relheight=1)
frame16_label = Label(frame16, text="** WELCOME **", font=("Algerian", 50, "bold"), fg='navajo white').place(x=500,
                                                                                                             y=150)
frame16_title = Label(frame16, text=" Choose the Option Below ", fg="white", bg="green",
                      font=("Baskerville Old Face", 35)).place(x=450, y=300)
frame16_signin = Button(frame16, text=" SIGN IN ", font=('arial', 25), command=lambda: show_frame(frame2)).place(x=360,
                                                                                                                 y=460)
frame16_signup = Button(frame16, text=" SIGN UP ", font=('arial', 25), command=lambda: show_frame(frame17)).place(x=900,
                                                                                                                  y=460)
frame16_back = Button(frame16, text=" GO BACK ", font=('arial', 15), fg='red',
                      command=lambda: show_frame(frame1)).place(
    x=675, y=650)

# Company signup frame (Frame 17)
bg17 = ImageTk.PhotoImage(file="20220320_180253.png")
Label(frame17, image=bg17).place(x=0, y=0, relwidth=1, relheight=1)


def register_info():
    dict_data = []
    dz = []
    dz = dz + [x1.get()]
    dz = dz + [y1.get()]
    dz = dz + [a1.get()]

    dict_data = dict_data + [dz]
    f = open("officer.csv", "a", newline="")
    wr = csv.writer(f)
    for word in dict_data:
        wr.writerow(word)
        messagebox.showinfo("Updated Result", " You have Registered Successfully ")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


frame17_title = frame17_title = Label(frame17, text=" Welcome to Company Portal ", fg="yellow", bg="black",
                                      font=("Algerian", 20),
                                      width=50).place(x=350, y=50)
l1 = Label(frame17, text=" Enter Your Company ID : ", fg="blue", bg="orange", relief="solid",
           font=("Arial", 18, "bold")).place(x=450, y=150)
x1 = StringVar()
e1 = Entry(frame17, textvariable=x1, bg="white", font=("Arial", 15, "bold"), width=18)
e1.pack()
e1.place(x=850, y=150)
l2 = Label(frame17, text=" Company Name ", fg="blue", bg="orange", relief="solid",
           font=("Arial", 18, "bold")).place(x=450, y=250)
y1 = StringVar()
e2 = Entry(frame17, textvariable=y1, bg="white", font=("Arial", 15, "bold"), width=18)
e2.pack()
e2.place(x=850, y=250)
l3 = Label(frame17, text=" Create Your Password ", fg="blue", bg="orange", relief="solid",
           font=("Arial", 18, "bold")).place(x=450, y=350)
a1 = StringVar()
e3 = Entry(frame17, show='*', textvariable=a1, bg="white", font=("Arial", 15, "bold"), width=18)
e3.pack()
e3.place(x=850, y=350)

frame17_browse = Button(frame17, text=" Register ", fg="white", bg="red", font=("Baskerville Old Face", 14, "bold"),
                        width=15,
                        command=register_info).place(x=650, y=580)
frame17_ext_but = Button(frame17, text=" Exit ", fg="pink", bg="grey", font=("caliber", 14, "bold"), width=15,
                         command=exit).place(x=760, y=700)
frame17_back = Button(frame17, text="Go Back ", fg="pink", bg="grey", font=("caliber", 14, "bold"), width=15,
                      command=lambda: show_frame(frame16)).place(x=560, y=700)
pro.mainloop()
