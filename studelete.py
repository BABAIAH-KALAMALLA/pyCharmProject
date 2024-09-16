#studelete.py----------->file name and module name
import mysql.connector
def deleterecord():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          password="BAba026@",
                                          database="employee")
            cur=con.cursor()
            #accepting record details from keyboard
            stuno=int(input("Enter student number:"))
            #design sql query for deleting a record
            dq="delete from student where stuno=%d"
            cur.execute(dq %stuno)
            con.commit()
            if(cur.rowcount>0):
                print("Record deleted from mysql {}".format(cur.rowcount))
            else:
                print("student number does not exists")
            print("*"*50)
            ch=input("Do you want to delete another record(yes/no):")
            if(ch=="no"):
                print("Thanks for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in mysqldb",db)
        except ValueError:
            print("Don't enter alnums,str and symbols for stuno")

#main program
