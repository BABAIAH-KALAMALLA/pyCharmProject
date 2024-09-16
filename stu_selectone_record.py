#stu_selectone_record.py-----------file name cum module name
import  mysql.connector
def selectonerecord():
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="BAba026@",
                                database="employee")
    #creating cursor object
    cur=con.cursor()
    #design sql query
    sq="select*from student where stuno= {}".format(int(input("Enter student number to view its details:")))
    cur.execute(sq)
    record=cur.fetchone()
    if(record==None):
        print("student record doesnot exist")
    else:
        print("student number:{}".format(record[0]))
        print("student name:{}".format(record[1]))
        print("student fees:{}".format(record[2]))
        print("student college:{}".format(record[3]))
#main program
