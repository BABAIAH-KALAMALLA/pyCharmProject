#studentadd.py--------> file name cum module name
import mysql.connector
def adddsturecord():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="BAba026@",
                                        database="employee")
            cur=con.cursor()
            #accepting student details from keyboard
            stuno=int(input("Enter the student number:"))
            stuname=input("Enter the student name:")
            stufees=float(input("Enter the student fees:"))
            stuclg=input("Enter the student college:")
            #write  the query and execute
            iq="insert into student values(%d,'%s',%f,'%s')"
            cur.execute(iq %(stuno,stuname,stufees,stuclg))
            con.commit()
            print("Record inserted succeccfully check in mysql {} ".format(cur.rowcount))
            print("-"*50)
            ch=input("Do you want insert another record (yes/no):")
            if(ch.lower()=="no"):
                print("Thanks for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("problem in mysql db",db)
        except ValueError:
            print("Don't enter alnums,str,symbols for stuno and stufees")

#main program
