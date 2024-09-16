#student_main_project.py-------------->main program
from stumenu import menu
from  studentadd import adddsturecord
from  studelete import deleterecord
from update_stu_record import updaterecord
from stu_selectone_record import selectonerecord
from  stu_select_all_records import selectall
while(True):
    menu()
    try:
        ch = int(input("Enter your choice:"))
        match(ch):
            case 1:
                adddsturecord()
            case 2:
                deleterecord()
            case 3:
                updaterecord()
            case 4:
                selectonerecord()
            case 5:
                selectall()
            case 6:
                print("Thanks for using this program")
                break
            case _:
                print("Ur selection of operation is wrong---try again")
    except ValueError:
        print("Don't enter alnums ,str and symbols for integer choice")