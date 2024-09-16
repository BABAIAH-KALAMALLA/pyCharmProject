#libraryupdate.py----->fille name and module name
import mysql.connector
def updatebook():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="BAba026@",
                                        database="employee")
            cur=con.cursor()
            #accepting bno,bname,price,pub from keyboard
            bno=int(input("Enter the book number for updating price and pub:"))
            price=float(input("Enter the new price:"))
            pub=input("enter new publication name:")
            #sql query
            uq="update library set price=%f,pub='%s' where bno=%d"
            cur.execute(uq %(price,pub,bno))
            con.commit()
            if (cur.rowcount > 0):
                print("{} Record Updated in MySQL DB".format(cur.rowcount))
            else:
                print("book Number does not Exist")
            print("-" * 50)
            ch=input("Do you want to update another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thanks for using ths program")
                break
        except mysql.connector.DatabaseError as db:
            print("problem in mysql db",db)
        except ValueError:
            print("Don't enter alnums,strs and symblos for bno")
#main program
