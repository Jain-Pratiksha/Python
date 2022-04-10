# Code contribution by Purva Lokare

import tkinter
from tkinter import *
from tkinter import messagebox
import random
import mysql.connector as mysql



quesions=[" “Macintosh” an Operating System is a product of ?",
          "  Full form of URL is?",
          "  _______ are software which is used to do a particular task.",
          " Father of ‘C’ programming language?",
          " What is the common name for the crime of stealing passwords?",
          " 'Connecting people' is the tagline of ....",
          " Who is the father of computer ethics?",
          " Tic-Tac-Toe is .....",
          " What is Blue Brain project?",
          " Which Penguin is the mascot of Linux Operating system?",
          " Expand SUN in sun Micrsystem.",
          " Who invented Java?",
          " 'Do no evil' is tag line of ......",
          " First Indian cinema released through internet is .....",
          " World's first microprocessor is ....."
          ]

choice=[
        ["A. Microsoft","B. Apple","C. Intel","D. Google"],
        ["A. Uniform Resource Locator","B. Uniform Resource Linkwrong","C. Uniform Registered Link","D. Unified Resource Link"],
        ["A. Operating system","B. Program","C. Data","D. Software"],
        ["A. Dennis Ritchie","B. Prof Jhon Kemenywrong","C. Thomas Kurtz","D. Bill Gates"],
        ["A. spooling","B. identity theft","C. spoofing","D. hacking"],
        ["A. Nokia","B. RedMi","C. RealMe","Samsung"],
        ["A. Frederick Morton Eden","B. Nell Mary Dunn","C. Norbetweiner.","D. Susannah Dobson"],
        ["A. latest Game","B. developed by Kurtz","C. 1st graphical game","D. developed by Jhon"],
        ["A. Cloning of human brain.","B. Cloning of animal brain.","C. Cloning of bird brain.","D. Cloning of blue brain."],
        ["A. Dux","B. PUX","C. MUX","D. TUX"],
        ["A. Sandfort University Node","B. Sandfort Union Node","C. Sandford Union Network","D. Stanford University Network"],
        ["A. Jemes A Eden","B. James A Gosling","C. Jhon A Gosling","D. James Dunn"],
        ["A. Opera","B. Google","C. GitHub","D. Microsoft"],
        ["A. Vivah","B. Gol Maal","C. Mother India","D. Sholay"],
        ["A. Intel 4007","B. Intel 4001","C. Intel 4004","D. Intel 4000"]
    ]

answer=[1,0,1,0,2,0,2,2,0,3,3,1,1,0,2]

user_ans=[]


indexes=[]
def gen():
    
    while(len(indexes)<10):
        x=random.randint(0,14)

        if x in indexes:
            continue
        else:
            indexes.append(x)
       


def showresult(score):
    l1.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    global label,label1,label11,btn
    label=Label(win,text="Your Score is ",font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
    label.place(x=500,y=250)
    label1=Label(win,text=score,font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
    label1.place(x=750,y=250)
    
    if score!=10:
        label11=Label(win,text="/10",font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
        label11.place(x=775,y=250)
    else:
        label11=Label(win,text="/10",font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
        label11.place(x=800,y=250)


    btn1=Button(text="Quit",font="bold 14",bg="#e5c50e",fg="black",command=win.destroy)
    btn1.place(x=675,y=400)
     
    
def calc():
    global indexes,user_ans,answer
    x=0
    score=0
    for i in indexes:
        if user_ans[x]==answer[i]:
            score=score+1
        x+=1
    showresult(score)
    

ques=1

def select():
    global i,user_ans,l1,r1,r2,r3,r4,ques
    x=i.get()
    user_ans.append(x)
    i.set(-1)
    
    if ques < 10:
        l1.config(text=quesions[indexes[ques]])
        r1['text']=choice[indexes[ques]][0]
        r2['text']=choice[indexes[ques]][1]
        r3['text']=choice[indexes[ques]][2]
        r4['text']=choice[indexes[ques]][3]
        ques +=1
    else:
        calc()


def start():
    global l1,r1,r2,r3,r4
    
    
    l1=Label(win,text=quesions[indexes[0]],font=("cambria",25,"bold"),bg="#e5c50e",fg="black")
    l1.place(x=400,y=150)
    
    global i
    i=IntVar()
    i.set(-1)
    r1=Radiobutton(win,text=choice[indexes[0]][0],value=0,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r1.place(x=500,y=250)   
   
    r2=Radiobutton(win,text=choice[indexes[0]][1],value=1,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r2.place(x=500,y=300)
   
    r3=Radiobutton(win,text=choice[indexes[0]][2],value=2,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r3.place(x=500,y=350)

    r4=Radiobutton(win,text=choice[indexes[0]][3],value=3,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r4.place(x=500,y=400)    

   
def remove():
    global l,b
    l.destroy()
    b.destroy()
    gen()
    start()
    


def welcome():
    global l,b
    l=Label(win,text="Welcome To The Quiz World",bg="#e5C50e",fg="black",font=("cambria",30,"bold"))
    l.place(x=350,y=250)
    

    b=Button(win,text="Start Quiz",font="bold 14",bg="#e5c50e",command=remove)
    b.place(x=600,y=400)


def open_window():

    def check():
        name=Entry.get(e1)
        roll=Entry.get(e2)
        year=Entry.get(e3)
        unm=Entry.get(e4)
        password=Entry.get(e5)
        cpass=Entry.get(e6)
        
    
        if(name!="" and roll!="" and year!="" and unm!="" and password!="" and cpass!=""):
            if(password!=cpass):
                messagebox.showinfo("Error","Password Doesn't Match!!")
        
            else:
                con = mysql.connect(host="localhost",user="root",password="",database="python")
                cursor = con.cursor()
                cursor.execute("insert into quiz values('"+name+"','"+roll+"','"+year+"','"+unm+"','"+password+"','"+cpass+"')")
                cursor.execute("commit")
                
                messagebox.showinfo("SignUp Status","SignUp Successful!!!!")
               
                con.close()
                x = rem0()
            
        else:
            messagebox.showinfo("Error","Please Fill All the fields")

        
      
    global l,l1,l2,l3,l4,l5,l6,e1,e2,e3,e4,e5,e6,b1
    l=Label(win,text="SignUp!!",fg="black",font="Verdana 24 bold",bg="#e5c50e")
    l.place(x=600,y=100)
    
    
    l1=Label(win,text="Name:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l1.place(x=500,y=200)
    e1=Entry(win,bg="#e5c50e",width=25,bd=3)
    e1.place(x=750,y=200)
        
    l2=Label(win,text="Enrollment No:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l2.place(x=500,y=250)
    e2=Entry(win,bg="#e5c50e",width=25,bd=3)
    e2.place(x=750,y=250)
        
    l3=Label(win,text="Email:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l3.place(x=500,y=300)
    e3=Entry(win,bg="#e5c50e",width=25,bd=3)
    e3.place(x=750,y=300)
        
    l4=Label(win,text="Enter Username:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l4.place(x=500,y=350)
    e4=Entry(win,bg="#e5c50e",width=25,bd=3)
    e4.place(x=750,y=350)
        
    l5=Label(win,text="Enter Password:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l5.place(x=500,y=400)
    e5=Entry(win,bg="#e5c50e",width=25,bd=3)
    e5.place(x=750,y=400)
        
    l6=Label(win,text="Confirm Password:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l6.place(x=500,y=450)
    e6=Entry(win,bg="#e5c50e",width=25,bd=3)
    e6.place(x=750,y=450)

    b1=Button(win,text="Submit",fg="black",font="Verdana 13 bold",bg="#e5c50e",command=check)
    b1.place(x=650,y=550)
    

def rem1():
    global l1,l2,l0,e1,e2,b1,b2,fm
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()            
    open_window()


def rem():
    global l1,l2,l0,e1,e2,b1,b2,fm
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    welcome()
    
def rem0():
    global l,l2,l3,l4,l5,l6
    global e1,e2,e3,e4
    global e5,e6,b1
    l.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    e4.destroy()
    e5.destroy()
    e6.destroy()
    b1.destroy()
    login()


con=mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
    )

cursor=con.cursor()

def user_login(uname,passw):
    try:
        cursor.execute("select * from `users` where `name`='"+uname+"' and `password`='"+passw+"'")
        return (cursor.fetchone())
    except:
        return False
    
    
    
def msg():
    uname=Entry.get(e1)
    passw=Entry.get(e2)

    if(uname=="" or passw==""):
        messagebox.showinfo("Alert","Fill all details......")
    else:
        res = user_login(uname,passw)
        if res:
            messagebox.showinfo("Message","login Successfully....")
            x = rem()
        else:
            messagebox.showinfo("Alert","Login Failed.......")



    
win=tkinter.Tk()
win.title("Let's Play Quiz")
win.configure(bg="#e5c50e")
win.geometry("1350x700+0+0")
#photo=ImageTk.PhotoImage(Image.open(r'C:\\Users\\Purva\\Desktop\\ff\\cer2.png'))


def login():
    global l1,l2,l0,e1,e2,b1,b2,fm
    l0=Label(win,text="Login!!",bg="#e5c50e",fg="black",font="Verdana 30 bold")
    l0.place(x=625,y=125)


    fm=Frame(win,bd=4,relief=RIDGE,bg="#e5c50e")
    fm.place(x=450,y=200,width=475,height=300)

    

    l1=Label(fm,text="Username:",bg="#e5c50e",fg="black",font="Verdana 16 bold",padx=20)
    l1.grid(row=1,column=0,padx=20,pady=40)
    e1=Entry(fm,font="Verdana 12 ",bd=2,bg="#e5c50e")
    e1.grid(row=1,column=1,padx=20)

    l2=Label(fm,text="Password:",bg="#e5c50e",fg="black",font="Verdana 16 bold")
    l2.grid(row=2,column=0,padx=20,pady=40)
    e2=Entry(fm,font="Verdana 12 ",bd=2,bg="#e5c50e",show='x')
    e2.grid(row=2,column=1,padx=20)


    b1=Button(fm,text="Login",font="Verdana 13 bold",bg="#e5c50e",command=msg)
    b1.grid(row=3,column=0,padx=50)

    b2=Button(fm,text="Sign Up",font="Verdana 13 bold",bg="#e5c50e",command=rem1)
    b2.grid(row=3,column=1)

login()
win.mainloop()
