#program for adding a record in table
#libraaryadd.py
import  mysql.connector
def addbook():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="BAba026@",
                                        database="employee")
            cur=con.cursor()
            #accepting the book details from keybord
            bno=int(input("Enter the book number:"))
            bname=input("Enter the book name:")
            price=float(input("Enter the price book:"))
            pub=input("Enter the book publication:")
            #design the query for inserting the above book details
            iq = "insert into library values(%d,'%s',%f,'%s') "
            cur.execute(iq % (bno, bname, price, pub))
            con.commit()
            print("record inserted successfully in mysql {}".format(cur.rowcount))
            print("-"*50)
            ch=input("Do you want to insert another record(yes/no):")
            if(ch=="no"):
                print("Thanks for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("problem in mysql db",db)
        except ValueError:
            print("Don't enter alnums,str and symbols for bno,price")
#main program

