#creating_table_for_stu_manage.py ----------> file name cum modulename
import mysql.connector
def createtable():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="BAba026@",
                                    database="employee")
        #creating cursor object
        cur=con.cursor()
        #define query and execute
        ct="create table student(stuno int primary key,stuname varchar(10) not null,stufees real not null,stuclg varchar(10) not null)"
        cur.execute(ct)
        print("databased in mysql----verify")
    except mysql.connector.DatabaseError as db:
        print("problem in mysqlDB",db)

#main program
createtable()