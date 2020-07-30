import os
import pandas as pd
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('studentattendance')
cur=con.cursor()
from tkinter import *

dataArray1=[]
dataArray2=[]
dataArray3=[]
dataArray4=[]
dataArray5=[]
dataArray6=[]
dataArray7=[]
dataArray8=[]
dataArray9=[]
dataArray10=[]
dataArray11=[]
dataArray12=[]
dataArray13=[]
dataArray14=[]
dataArray15=[]
dataArray16=[]
dataArray17=[]
dataArrayA=[]
dataArrayB=[]
dataArrayC=[]
dataArrayD=[]



window=Tk()
window.geometry('1080x540')
window.title('Start Window')
#window.iconbitmap('icon.ico')


Label(window).place(x=1,y=0)


def start():
    window=Toplevel()
    window.geometry('540x140')
    window.title('Login Window')
    Label(window,text='Username  ',font=("Times New",20)).grid(row=1,column=1)
    v=Entry(window,width=25,font=("Times New",18),bd=5,bg="light grey")
    v.grid(row=1,column=2)
    Label(window,text='Password  ',font=("Times n=New",20)).grid(row=2,column=1)
    vv=Entry(window,show='*',width=25,font=("Times New",18),bd=5,bg="light grey")
    vv.grid(row=2,column=2)

    mode=StringVar(window)
    mode.set("Select Mode") # default value
    var = OptionMenu(window,mode, "Faculty", "Student")
    var.grid(row=2,column=4)

    def login():
        if(((int(v.get())!=123) or (int(vv.get())!=123)) and (mode.get()!="Select Mode")):
            showwarning('Login Failed','Incorrect Id Or Password Used Or Mode Not Selected')
        else:
            menu = Toplevel()
            menu.geometry('540x540')
            menu.title('Menu Window')

            l=Label(menu,text='Dashboard :',font='Times 20 bold')
            l.grid(row=0,column=0)
            Label(menu).grid(row=1,column=100,rowspan=30)
###################################################################################################################
            if(mode.get()=="Faculty"):
                showinfo('Notice','Any Important notice can be written here :))))')
            else:
                showinfo('Notice','Any Important notice can be written here for student :))))')
            def option1():
                if(mode.get()=="Faculty"):
                    root = Toplevel()
                    root.geometry('540x540')
                    root.title('Register Students Details')
                    l=Label(root,text='Register Student Details :',font='Times 20 bold')
                    l.grid(row=0,column=0)
                    
                    l=Label(root,text=' ')
                    l.grid(row=1,column=0)

                    l=Label(root,text='Enter Student Registration ID : ')
                    l.grid(row=2,column=0)
                    
                    c=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    c.grid(row=2,column=1)
                    xp=c.get()
                    
                    l=Label(root,text='Enter First Name : ')
                    l.grid(row=3,column=0)
                    d=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    d.grid(row=3,column=1)
                    l=Label(root,text='Enter Last Name : ')
                    l.grid(row=4,column=0)
                    e=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    e.grid(row=4,column=1)
                    l=Label(root,text='Enter the School : ')
                    l.grid(row=5,column=0)

                    f=StringVar(root)
                    f.set("Select School")
                    w = OptionMenu(root,f, "SCSE", "SAS", "SITE", "SCOPE", "V-SIGN", "VIT BS", "V-SPARC", "SSL", "SMEC", "SENSE", "SELECT", "SCE","SCHEME","SBST","HOT","VAIAL")
                    w.grid(row=5,column=1)

                    l=Label(root,text='Enter total year fee : ')
                    l.grid(row=6,column=0)
                    q=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    q.grid(row=6,column=1)
                    l = Label(root, text='Enter DBMS Attendance : ')
                    l.grid(row=7, column=0)
                    db = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    db.grid(row=7, column=1)

                    l = Label(root, text='Enter DLD Attendance : ')
                    l.grid(row=8, column=0)
                    dl = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    dl.grid(row=8, column=1)
                    l = Label(root, text='Enter Mat Attendance : ')
                    l.grid(row=9, column=0)
                    ma = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    ma.grid(row=9, column=1)
                    l = Label(root, text='Enter Phy Attendance : ')
                    l.grid(row=10, column=0)
                    ph = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    ph.grid(row=10, column=1)
                    l = Label(root, text='Enter Soft skills Attendance : ')
                    l.grid(row=11, column=0)
                    so = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    so.grid(row=11, column=1)
                    l = Label(root, text='Enter CSE Attendance : ')
                    l.grid(row=12, column=0)
                    cs = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    cs.grid(row=12, column=1)

                    cur.execute("create table if not exists student(sid varchar(10) primary key, fname varchar(20), lname varchar(20), clno number(4), yearduefee number(6), dbms_at number(4), dld_at number(4), mat_at number(4), phy_at number(4), ss_at number(4),cse_at number(4),dbms_m number(4), dld_m number(4), mat_m number(4), phy_m number(4), ss_m number(4), cse_m number(4))")
                    def insertinstudent():
                        cur.execute("select * from student where sid=?",(c.get(),))
                        cpy=cur.fetchone()
                        try:
                            cur.execute("insert into student values(?,?,?,?,?,?,?,?,?,?,?,0,0,0,0,0,0)",(c.get(),d.get(),e.get(),f.get(),int(q.get()),int(db.get()),int(dl.get()),int(ma.get()),int(ph.get()),int(so.get()),int(cs.get())))
                            con.commit()
                            showinfo('Information','Student Insertion Successful')
###################################################     PANDAS            ####################################################
                            dataArray1.append(c.get())
                            dataArray2.append(d.get())
                            dataArray3.append(e.get())
                            dataArray4.append(f.get())
                            dataArray5.append(int(q.get()))
                            dataArray6.append(int(db.get()))
                            dataArray7.append(int(dl.get()))
                            dataArray8.append(int(ma.get()))
                            dataArray9.append(int(ph.get()))
                            dataArray10.append(int(so.get()))
                            dataArray11.append(int(cs.get()))


                            df1 = pd.DataFrame({'Student Id': dataArray1,'First Name':dataArray2,'Last Name':dataArray3,'School':dataArray4,'Yearly Due Fee':dataArray5,'Attendance In DBMS':dataArray6,'Attendance In DLD':dataArray7,'Attendance In Math':dataArray8,'Attendance In Physics':dataArray9,'Attendance In Soft skills':dataArray10,'Attendance In CSE':dataArray11})#,'Marks In English':dataArray12,'Marks In Hindi':dataArray13,'Marks In Math':dataArray14,'Marks In Science':dataArray15,'Marks In SSt':dataArray16,'Marks In Sanskrit':dataArray17})
                            writer = pd.ExcelWriter('/Users/suriyakrishnan/Desktop/sams/Student_Details.xlsx', engine='xlsxwriter')
                            df1.to_excel(writer, sheet_name='Sheet1')
                            writer.save()
                            
###################################################     PANDAS            #############################################################                                                        
                        except sqlite3.IntegrityError as error:
                            showwarning('Error','Already exists!')
            

                    
                    Button(root,text='Insert Data Of Student',command=insertinstudent,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=14,column =1,sticky=N+S+E+W)
                    
                    def logout():
                         ans=askyesno('Confirmation', 'Do You Want To Exit?')
                         if(ans==True):
                             root.destroy()
                    Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=15,column=1,sticky=N+S+E+W)
                    root.mainloop()
                else:
                      showerror('Information','Access Denied')
            
            Button(menu,text='Register Student details',command=option1,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=1,column=0,sticky=N+S+E+W)
##############################################################################################################################################
            def option2():
                root = Toplevel()
                root.geometry('1080x600')
                root.title('Student Details View')
                l=Label(root,text='View Student Details :',font='Times 20 bold')
                l.grid(row=0,column=3)
                l=Label(root,text=' ')
                l.grid(row=1,column=0)

                l=Label(root,text='Enter Student Registration Id : ')
                l.grid(row=2,column=0)
                ui=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                    #ui=sid
                ui.grid(row=2,column=1)
                
                l=Label(root,text='Enter School : ')
                l.grid(row=4,column=0)
                f=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                        #f=clno.
                f.grid(row=4,column=1)
                def show1():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    val=[(ui.get())]
                    row_number=0
                    Label(root, text = "Student ID").grid(column=1,row = row_number)
                    Label(root, text = "First Name").grid(column=2,row = row_number)
                    Label(root, text = "Last Name").grid(column=3,row = row_number)
                    Label(root, text = "School").grid(column=4,row = row_number)
                    Label(root, text = "Year Due Fee").grid(column=5,row = row_number)
                    Label(root, text = "DBMS").grid(column=6,row = row_number)
                    Label(root, text = "DLD").grid(column=7,row = row_number)
                    Label(root, text = "Mathematics").grid(column=8,row = row_number)
                    Label(root, text = "Phyiscs").grid(column=9,row = row_number)
                    Label(root, text = "Soft Skills").grid(column=10,row = row_number)
                    Label(root, text = "CSE").grid(column=11,row = row_number)

                    z=cur.execute("select *from student where sid=?",val)
                    for row_number,row in enumerate(z):
                        Label(root, text = "" + str(row[0])).grid(column=1,row = row_number+1)
                        Label(root, text = "" + str(row[1])).grid(column=2,row = row_number+1)
                        Label(root, text = "" + str(row[2])).grid(column=3,row = row_number+1)
                        Label(root, text = "" + str(row[3])).grid(column=4,row = row_number+1)
                        Label(root, text = "" + str(row[4])).grid(column=5,row = row_number+1)
                        Label(root, text = "" + str(row[5])).grid(column=6,row = row_number+1)
                        Label(root, text = "" + str(row[6])).grid(column=7,row = row_number+1)
                        Label(root, text = "" + str(row[7])).grid(column=8,row = row_number+1)
                        Label(root, text = "" + str(row[8])).grid(column=9,row = row_number+1)
                        Label(root, text = "" + str(row[9])).grid(column=10,row = row_number+1)
                        Label(root, text = "" + str(row[10])).grid(column=11,row = row_number+1)
                    root.mainloop()
                Button(root,text='Show Student Data',command=show1,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column =2,sticky=N+S+E+W)
##################################################################################################################################################
                def show2():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    v=[(f.get())]
                    z=cur.execute("select *from student where clno=?",v)
                    Label(root, text = "Student ID").grid(column=0,row=0)
                    Label(root, text = "First Name").grid(column=1,row=0)
                    Label(root, text = "Last Name").grid(column=2,row=0)
                    Label(root, text = "School").grid(column=3,row=0)
                    Label(root, text = "Year Due Fee").grid(column=4,row=0)
                    Label(root, text = "DBMS").grid(column=5,row=0)
                    Label(root, text = "DLD").grid(column=6,row=0)
                    Label(root, text = "Mathematics").grid(column=7,row=0)
                    Label(root, text = "Physics").grid(column=8,row=0)
                    Label(root, text = "Soft Skills").grid(column=9,row=0)
                    Label(root, text = "CSE").grid(column=10,row=0)
                    y=-1
                    for row_number,row in enumerate(z):
                        y=y+1
                        Label(root, text = "" + str(row[0])).grid(column=0,row = row_number+1+y)
                        Label(root, text = "" + str(row[1])).grid(column=1,row = row_number+1+y)
                        Label(root, text = "" + str(row[2])).grid(column=2,row = row_number+1+y)
                        Label(root, text = "" + str(row[3])).grid(column=3,row = row_number+1+y)
                        Label(root, text = "" + str(row[4])).grid(column=4,row = row_number+1+y)
                        Label(root, text = "" + str(row[5])).grid(column=5,row = row_number+1+y)
                        Label(root, text = "" + str(row[6])).grid(column=6,row = row_number+1+y)
                        Label(root, text = "" + str(row[7])).grid(column=7,row = row_number+1+y)
                        Label(root, text = "" + str(row[8])).grid(column=8,row = row_number+1+y)
                        Label(root, text = "" + str(row[9])).grid(column=9,row = row_number+1+y)
                        Label(root, text = "" + str(row[10])).grid(column=10,row = row_number+1+y)
                    root.mainloop()
                Button(root,text='Show All Student Data Of Class',command=show2,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=4,column =2,sticky=N+S+E+W)
                
##################################################################################################################################################
                def delete2():
                    if(mode.get()=="Faculty"):
                        cur.execute("drop table student")
                        showinfo('Information','Student Deletion Successful')
                    else:
                        showerror('Information','Access Denied')
                Button(root,text='Delete All Student Data',command=delete2,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column =0,sticky=N+S+E+W)
                def logout():
                    ans=askyesno('Confirmation', 'Do You Want To Exit?')
                    if(ans==True):
                        root.destroy()
                Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0,sticky=N+S+E+W)
                root.mainloop()
            Button(menu,text='View Student details',command=option2,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column=0,sticky=N+S+E+W)
###############################################################################################################################################
            def option3():
                if(mode.get()=="Faculty"):
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('Student Fee Updation')
                    l=Label(root,text='Student Fee Updation :',font='Times 20 bold')
                    l.grid(row=0,column=3)
                    
                    l=Label(root,text=' ')
                    l.grid(row=1,column=0)

                    l=Label(root,text='Enter Student ID : ')
                    l.grid(row=2,column=0)
                    g=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    g.grid(row=2,column=1)
                    l=Label(root,text='Enter fee paid : ')
                    l.grid(row=3,column=0)
                    h=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    h.grid(row=3,column=1)
                    def update1():
                        p=int(g.get())
                        cur.execute("update student set yearduefee=yearduefee-? where sid=?",(int(h.get()),p))
                        con.commit()
                        showinfo('Information','Fee Updation Successful')

                     
                    Button(root,text='Update Fee',command=update1,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=4,column =0,sticky=N+S+E+W)

                    l=Label(root,text=' ')
                    l.grid(row=5,column=0)

                    l=Label(root,text='Enter Student ID to see details : ')
                    l.grid(row=6,column=0)
                    i=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    i.grid(row=6,column=1)
                    def show3():
                        w=[(int(i.get()))]
                        cur.execute("select yearduefee from student where sid=?",w)
                        x=cur.fetchall()
                        showinfo('Result',x)
                    Button(root,text='Show Student due fee ',command=show3,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column =0,sticky=N+S+E+W)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            root.destroy()
                    Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0)
                    root.mainloop()
                else:
                    showerror('Information','Access Denied')
            Button(menu,text='Student Fee Updation',command=option3,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=3,column=0,sticky=N+S+E+W)
######################################################################################################################################################################

            def option4():
                if(mode.get()=="Faculty"):
                    win = Toplevel()
                    win.geometry('540x140')
                    win.title('Update Attendance')
                    l=Label(win,text='Enter Student Id : ')
                    l.grid(row=2,column=0)
                    f=Entry(win,font=("Times New",10),bd=5,bg="light grey")
                    f.grid(row=2,column=1)

                    def fill():
                        v=[(f.get())]
                        z=cur.execute("select fname from student where sid=?",v)
                        Label(win, text = "Student Name").grid(column=0,row = 3,sticky=N+S+E+W)
                        Label(win, text = z).grid(column=0,row = 4,sticky=N+S+E+W)
                        
                        
                        Label(win, text = "DBMS").grid(column=1,row = 3,sticky=N+S+E+W)
                        dbms=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        dbms.grid(row=4,column=1,sticky=N+S+E+W)
                            
                        Label(win, text = "DLD").grid(column=2,row = 3,sticky=N+S+E+W)
                        dld=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        dld.grid(row=4,column=2,sticky=N+S+E+W)
                        
                        Label(win, text = "Mathematics").grid(column=3,row = 3,sticky=N+S+E+W)
                        mat=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        mat.grid(row=4,column=3,sticky=N+S+E+W)
                            
                        Label(win, text = "Physics").grid(column=4,row = 3)
                        phy=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        phy.grid(row=4,column=4,sticky=N+S+E+W)
                         
                        Label(win, text = "Soft skills").grid(column=5,row = 3,sticky=N+S+E+W)
                        ss=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        ss.grid(row=4,column=5,sticky=N+S+E+W)
                     
                        Label(win, text = "CSE").grid(column=6,row = 3,sticky=N+S+E+W)
                        cse=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        cse.grid(row=4,column=6,sticky=N+S+E+W)
                            
                        def regist():
                            cur.execute("update student set dbms_at=dbms_at+? where sid=?",(dbms.get(),f.get()))
                            con.commit()
                            cur.execute("update student set dld_at=dld_at+? where sid=?",(dld.get(),f.get()))
                            con.commit()
                            cur.execute("update student set mat_at=mat_at+? where sid=?",(mat.get(),f.get()))
                            con.commit()
                            cur.execute("update student set phy_at=phy_at+? where sid=?",(phy.get(),f.get()))
                            con.commit()
                            cur.execute("update student set ss_at=ss_at+? where sid=?",(ss.get(),f.get()))
                            con.commit()
                            cur.execute("update student set cse_at=cse_at+? where sid=?",(cse.get(),f.get()))
                            con.commit()
                            cur.execute("select fname from student where sid=?",f.get())
                            new=cur.fetchone()
                            showinfo('Information','Attendance Locked')

##############################################          PANDAS         #########################################################
                            dataArrayA.append(int(f.get()))
                            dataArray6.append(int(dbms.get()))
                            dataArray7.append(int(dld.get()))
                            dataArray8.append(int(mat.get()))
                            dataArray9.append(int(phy.get()))
                            dataArray10.append(int(ss.get()))
                            dataArray11.append(int(cse.get()))
                            dataArrayC.append(str(new))
                            df2 = pd.DataFrame({'Student ID':dataArrayA,'Name':dataArrayC,'Attendance In DBMS':dataArray6,'Attendance In DLD':dataArray7,'Attendance In Math':dataArray8,'Attendance In Physics':dataArray9,'Attendance In Soft Skills':dataArray10,'Attendance In CSE':dataArray11})
                            writer = pd.ExcelWriter('/Users/suriyakrishnan/Desktop/sams/Student_Attendance.xlsx', engine='xlsxwriter')
                            df2.to_excel(writer, sheet_name='Sheet1')
                            writer.save()

##############################################          PANDAS         #########################################################
                        Button(win,text='Submit',command=regist,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column =0)
                    Button(win,text='Show',command=fill,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column =2)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            win.destroy()
                    Button(win,text='Exit',command=logout,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column=3)
                    
                    win.mainloop()
                else:
                    showerror('Information','Access Denied')
            Button(menu,text='Update Attendance',command=option4,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=4,column=0,sticky=N+S+E+W)
#########################################################################################################################################
            def option5():
                root=Toplevel()
                root.geometry('1080x600')
                root.title('Attandence View')
                l=Label(root,text='Student Attendance View',font='Times 20 bold')
                l.grid(row=0,column=3)
                
                l=Label(root,text='')
                l.grid(row=1,column=0)

                l=Label(root,text='Enter Student Registration ID : ')
                l.grid(row=2,column=0)
                stid=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                stid.grid(row=2,column=1)
                def show4():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    row_number=0
                    Label(root, text = "DBMS").grid(column=1,row = row_number)
                    Label(root, text = "DLD").grid(column=2,row = row_number)
                    Label(root, text = "Mathematics").grid(column=3,row = row_number)
                    Label(root, text = "Physics").grid(column=4,row = row_number)
                    Label(root, text = "Soft Skills").grid(column=5,row = row_number)
                    Label(root, text = "CSE").grid(column=6,row = row_number)
                    
                    w=[(int(stid.get()))]
                    z=cur.execute("select dbms_at,dld_at,mat_at,phy_at,ss_at,cse_at from student where sid=?",w)
                    for row_number,row in enumerate(z):
                        Label(root, text = "" + str(row[0])).grid(column=1,row = row_number+1)
                        Label(root, text = "" + str(row[1])).grid(column=2,row = row_number+1)
                        Label(root, text = "" + str(row[2])).grid(column=3,row = row_number+1)
                        Label(root, text = "" + str(row[3])).grid(column=4,row = row_number+1)
                        Label(root, text = "" + str(row[4])).grid(column=5,row = row_number+1)
                        Label(root, text = "" + str(row[5])).grid(column=6,row = row_number+1)
                    root.mainloop()
                Button(root,text='Show Student Attendance ',command=show4,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column =0,sticky=N+S+E+W)
                def logout():
                    ans=askyesno('Confirmation', 'Do You Want To Exit?')
                    if(ans==True):
                        root.destroy()
                Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0)
                root.mainloop()
            Button(menu,text='View Attendance',command=option5,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column=0,sticky=N+S+E+W)

#########################################################################################################################################
            def option6():
                if(mode.get()=="Faculty"):
                    win=Toplevel()
                    win.geometry('1080x600')
                    win.title('Register Student Marks')
                    #l=Label(root,text='Student Marks Updation',font='Times 20 bold')
                    #l.grid(row=0,column=3)
                    l=Label(win,text='Enter Student Id : ')
                    l.grid(row=2,column=0)
                    f=Entry(win,font=("Times New",10),bd=5,bg="light grey")                                                        #f=sid.
                    f.grid(row=2,column=1)

                    def fill():
                        v=[(f.get())]
                        z=cur.execute("select fname from student where sid=?",v)
                        Label(win, text = "Student Name").grid(column=0,row = 3,sticky=N+S+E+W)
                        Label(win, text = z).grid(column=0,row = 4,sticky=N+S+E+W)
                        
                        
                        Label(win, text = "DBMS").grid(column=1,row = 3,sticky=N+S+E+W)
                        dbms=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        dbms.grid(row=4,column=1,sticky=N+S+E+W)
                            
                        Label(win, text = "DLD").grid(column=2,row = 3,sticky=N+S+E+W)
                        dld=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        dld.grid(row=4,column=2,sticky=N+S+E+W)
                        
                        Label(win, text = "Mathematics").grid(column=3,row = 3,sticky=N+S+E+W)
                        mat=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        mat.grid(row=4,column=3,sticky=N+S+E+W)
                            
                        Label(win, text = "Physics").grid(column=4,row = 3)
                        phy=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        phy.grid(row=4,column=4,sticky=N+S+E+W)
                         
                        Label(win, text = "Soft skills").grid(column=5,row = 3,sticky=N+S+E+W)
                        ss=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        ss.grid(row=4,column=5,sticky=N+S+E+W)
                     
                        Label(win, text = "CSE").grid(column=6,row = 3,sticky=N+S+E+W)
                        cse=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        cse.grid(row=4,column=6,sticky=N+S+E+W)
                            
                        def regist():
                            cur.execute("update student set dbms_m=? where sid=?",(dbms.get(),f.get()))
                            con.commit()
                            cur.execute("update student set dld_m=? where sid=?",(dld.get(),f.get()))
                            con.commit()
                            cur.execute("update student set mat_m=? where sid=?",(mat.get(),f.get()))
                            con.commit()
                            cur.execute("update student set phy_m=? where sid=?",(phy.get(),f.get()))
                            con.commit()
                            cur.execute("update student set ss_m=? where sid=?",(ss.get(),f.get()))
                            con.commit()
                            cur.execute("update student set cse_m=? where sid=?",(cse.get(),f.get()))
                            con.commit()
                            cur.execute("select fname from student where sid=?",(f.get()))
                            new=cur.fetchone()
                            showinfo('Information','Marks Locked')


##############################################          PANDAS         #########################################################
                            dataArrayB.append(int(f.get()))
                            dataArray12.append(int(dbms.get()))
                            dataArray13.append(int(dld.get()))
                            dataArray14.append(int(mat.get()))
                            dataArray15.append(int(phy.get()))
                            dataArray16.append(int(ss.get()))
                            dataArray17.append(int(cse.get()))
                            dataArrayD.append(str(new))
                            df2 = pd.DataFrame({'Student ID':dataArrayA,'Name':dataArrayD,'Marks In DBMS':dataArray12,'Marks In DLD':dataArray13,'Marks In Math':dataArray14,'Marks In Physics':dataArray15,'Marks In soft skills':dataArray16,'Marks In CSE':dataArray17})
                            writer = pd.ExcelWriter('/Users/suriyakrishnan/Desktop/sams/Student_Marks.xlsx', engine='xlsxwriter')
                            df2.to_excel(writer, sheet_name='Sheet1')
                            writer.save()

##############################################          PANDAS         #########################################################
                            
                        Button(win,text='Submit',command=regist,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column =0)
                    Button(win,text='Show',command=fill,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column =2)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            win.destroy()
                    Button(win,text='Exit',command=logout,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column=3)
                    
                    win.mainloop()
                else:
                    showerror('Information','Access Denied')
            Button(menu,text='Update Student Marks',command=option6,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=6,column=0,sticky=N+S+E+W)
#########################################################################################################################################
            def option7():
                    root=Toplevel()
                    root.geometry('1080x600')
                    root.title('Marks View')

                    l=Label(root,text='Enter Student ID : ')
                    l.grid(row=2,column=0)
                    stid=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                    stid.grid(row=2,column=1)

                    def show4():
                        root = Toplevel()
                        root.geometry('1080x600')
                        root.title('View Window')
                        row_number=0
                        Label(root, text = "DBMS").grid(column=1,row = row_number)
                        Label(root, text = "DLD").grid(column=2,row = row_number)
                        Label(root, text = "Mathematics").grid(column=3,row = row_number)
                        Label(root, text = "Physics").grid(column=4,row = row_number)
                        Label(root, text = "Soft skills").grid(column=5,row = row_number)
                        Label(root, text = "CSE").grid(column=6,row = row_number)
                        w=[(int(stid.get()))]
                        z=cur.execute("select dbms_m,dld_m,mat_m,phy_m,ss_m,cse_m from student where sid=?",w)
                        for row_number,row in enumerate(z):
                            Label(root, text = "" + str(row[0])).grid(column=1,row = row_number+1)
                            Label(root, text = "" + str(row[1])).grid(column=2,row = row_number+1)
                            Label(root, text = "" + str(row[2])).grid(column=3,row = row_number+1)
                            Label(root, text = "" + str(row[3])).grid(column=4,row = row_number+1)
                            Label(root, text = "" + str(row[4])).grid(column=5,row = row_number+1)
                            Label(root, text = "" + str(row[5])).grid(column=6,row = row_number+1)
                        root.mainloop()
                    Button(root,text='Show Student Marks ',command=show4,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column =0,sticky=N+S+E+W)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            root.destroy()
                    Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0)
                    root.mainloop()                  
        
            Button(menu,text='View Marks',command=option7,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column=0,sticky=N+S+E+W)

            def logout():
                ans=askyesno('Confirmation', 'Do You Want To Logout?')
                if(ans==True):
                    menu.destroy()
            Button(menu,text='Logout',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=10,column=0,sticky=N+S+E+W)

            menu.mainloop()
    Button(window,text='Login',command=login,width=20,font=("Times New",15),bd=5,bg="light grey").grid(row=3,column=2,sticky=N+S+E+W)

    window.mainloop()

###############################################################################################################################################################

Button(window,command=start,text ='Start',width=25,font=("Helvetica Neue bold",30),bd=8,bg="white",fg="red").place(x=320,y=390)

Label(window,text='Name: S.Suriyakrishnan\nRegistration Id: 19BCE1050\nB.Tech\nPhone Number: 6382081820\nEmail: suriyakrishnan.s2019@vitstudent.ac.in\nTopic:Student Attendance management system',font=("Arial",20,"bold"),bg='black',fg='red').place(x=300,y=150)
window.mainloop()
