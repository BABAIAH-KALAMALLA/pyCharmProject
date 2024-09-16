#program for creating table for library management
#creating_table_library_mange.py-------file name cum module name
import mysql.connector
def createtable():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="BAba026@",
                                    database="employee")
        cur=con.cursor()
        #difine query and excute
        tq="create table library(bno int primary key,bname varchar(10) not null,price real not null,pub varchar(10) not null)"
        cur.execute(tq)
        print("databased in mysql----verify")
    except mysql.connector.DatabaseError as db:
        print("problem with mysql ",db)



#main program
createtable()
