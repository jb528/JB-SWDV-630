from Customer import customer_main
from Rooms import rooms_main
from Booking import booking_main
from Employee import employee_main
from Etimecard import etimecard_main
from Epaycheck import epaycheck_main



def hotel_main():
    
    print("Welcome To Hotel Golden Retriever\n")
    print(" Select a function to Enter below:\n")
    print("   1 Customer\n")
    print("   2 Rooms\n")
    print("   3 Booking\n")
    print("   4 Employee\n")
    print("   5 Employee Timecard\n")
    print("   6 Employee Paycheck\n")
    print("   0 Exit\n")
  
    ch=int(input("Enter a Hotel function number:"))
     
    if ch == 1:
        print(" ")
        customer_main()
     
    elif ch == 2:
        print(" ")
        rooms_main()
     
    elif ch == 3:
        print(" ")
        booking_main()
     
    elif ch == 4:
        print(" ")
        employee_main()
     
    elif ch == 5:
        print(" ")
        etimecard_main()
    
    elif ch == 6:
        print(" ")
        epaycheck_main()
        
    else:
        exit()
        
        
hotel_main()