#librarymainproject.py-----main program
from librarymemu import menu
from libraryadd import addbook
from librarydelete import deletebook
from libraryupdate import updatebook
from libraryselectallrecord import selectrecords
while(True):
    menu()
    try:
         ch=int(input("Enter your choice:"))
         match(ch):
              case 1:
                  addbook()
              case 2:
                  deletebook()
              case 3:
                  updatebook()
              case 4:
                  selectrecords()
              case 5:
                  print("Thanks for using this App")
                  break
              case _:
                  print("ur selection of operaton is wrong--try again")
    except ValueError:
        print("Don't Enter strs, alnums and symbols for Integer Choice:")
