#update_studnt_record.py------------>file name cum module name
import  mysql.connector
def updaterecord():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="BAba026@",
                                        database="employee")
            #creating cursor object
            cur=con.cursor()
            #accepting stuno and stufees and stuname from keyboard
            stuno=int(input("Enter stuno:"))
            stuname=input("Enter new student name: ")
            stufees=float(input("Enter new student fees:"))
            #sql query
            uq="update student set stuname='%s',stufees=%f where stuno=%d"
            cur.execute(uq %(stuname,stufees,stuno))
            con.commit()
            if(cur.rowcount>0):
                print("Record updated successfully{}".format(cur.rowcount))
            else:
                print("Student number does not exists")
            print("*"*50)
            ch=input("Do you want to update another record(yes/no):")
            if(ch=="no"):
                print("Thanks for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("problem in mysql Db",db)
        except ValueError:
            print("Don't enter alnums, str and symbols for stuno")
#main program
