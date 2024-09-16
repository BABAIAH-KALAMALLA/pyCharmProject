#Program for Reading the Records from Employee Table--fetchall()
#libraryselectallrecord.py
import mysql.connector
def  selectrecords():
	try:
		con=mysql.connector.connect(host="localhost",
										  user="root",
										  passwd="BAba026@",
										  database="employee")
		cur=con.cursor()
		sq="select * from library order by price desc"
		cur.execute(sq)
		#get the records
		print("*"*50)
		records=cur.fetchall()
		for record in records:
			for val in record:
				print(val,end="\t")
			print()
		print("*"*50)
	except mysql.connector.DatabaseError as db:
		print("Problem in MySQL Data Base:",db)

#Main Program