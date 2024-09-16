#stu_select_all_records.py----------->file name cum module name
import  mysql.connector
def selectall():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="BAba026@",
                                    database="employee")
        #creating cursor object
        cur=con.cursor()
        #design sql query
        sq="select*from student"
        cur.execute(sq)
        #get the records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print(val,end="\t")
            print()
    except mysql.connector.DatabaseError as db:
        print("Problem in mysql",db)
#main program
