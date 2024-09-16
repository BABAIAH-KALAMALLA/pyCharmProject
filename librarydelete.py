#librarydelete.py------>file name cum module name
import mysql.connector
def deletebook():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="BAba026@",
                                        database="employee")
            cur=con.cursor()
            #accepting book details from keyboard
            bno=int(input("Enter the book number:"))
            #design sql query for deleting a record
            dq="delete from library where bno=%d"
            cur.execute(dq %bno)
            con.commit()
            if(cur.rowcount>0):
                print("{} record deleted from mysql DB".format(cur.rowcount))
            else:
                print("Book number does not exist")
            print("*"*50)
            ch=input("Do you want to delete another book(yes/no):")
            if(ch.lower()=="no"):
                print("thaks for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("problem in mysql",db)
        except ValueError:
            print("Don't enter alnums,str and symbols for bno")

#main program
