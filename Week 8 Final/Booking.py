from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Update,Delete,Insert
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import datetime


class Base(DeclarativeBase):
    pass

class Booking(Base):
    __tablename__ = "Booking"
        
    id=Column(Integer,primary_key=True)
    _number=Column(String)
    _arrival=Column(String)
    _departure=Column(String)
    
    def edit_booking(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        
        user_input1 = str(input("Enter the Booking ID you wish to change: "))
        nyear = int(input("Enter new Departure Year (YYYY): "))
        nmonth = int(input("Enter new Departure Month (MM): "))
        nday = int(input("Enter new Departure Day (DD): "))
        user_input2= str(datetime.date(nyear,nmonth,nday))
        
        
        u = session.query(Booking).get(user_input1)
        print(u)
        print("-")
        u._departure=user_input2
        session.commit()
        print(u)
        print()
        print()
        booking_main()

    
    def search_booking(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        booking = session.query(Booking)
        
        user_input = int(input("Enter Booking ID: "))
        
        for b in booking:
            if b.id == user_input:
                print("ID#",user_input,"info:","Booking Id:",b.id,"Room Number:",b._number,"Arrival Date:",b._arrival,"Departure Date:",b._departure)
                print()
                print()
                booking_main()
                
    def delete_booking(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        booking = session.query(Booking)
        
        user_input = int(input("Enter Booking ID to delete: "))
        
        for b in booking:
            if b.id == user_input:
                session.delete(b)
                session.commit()
                print(user_input,"-- Has been deleted.")       
                print()
                print()
                booking_main()
        
    def add_booking(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        user_input= int(input("Enter a Room Number to stay in between 1 and 30: "))
        
        ayear = int(input("Enter the Year of Arrival (YYYY): "))
        amonth = int(input("Enter the Month of Arrival (MM): "))
        aday = int(input("Enter the Day of Arrival (DD): "))
        user_input1= str(datetime.date(ayear,amonth,aday))
        print()
        dyear = int(input("Enter the Year of Departure (YYYY): "))
        dmonth = int(input("Enter the Month of Departure (MM): "))
        dday = int(input("Enter the Day of Departure (DD): "))
        user_input2= str(datetime.date(dyear,dmonth,dday))
        
        
        if (user_input >= 1) and (user_input <=30):
            self._number = _number = user_input
        else:
            print("Invalid Number - Please try agian")
            b=Booking()
            b.add_booking()
        
        self._arrival=_arrival=user_input1
        self._departure=_departure=user_input2
       
        b1 = self._number,self._arrival,self._departure
        
        
        a=Booking(_number = b1[0],_arrival= b1[1],_departure=b1[2])
        print()
        print(a,"-- Has been added.")
        session.add(a)
        session.commit()
        booking = session.query(Booking)
        
        print("Database Table Booking")
        for b in booking:
            print("Booking Id:",b.id,"Room Number:",b._number,"Arrival Date:",b._arrival,"Departure Date:",b._departure)
        print()
        print()
        booking_main()
        return b1
        
        
    def __repr__(self):
        return "Room Number: {0}  Arrival Date: {1}  Departure Date: {2}".format(self._number,self._arrival,self._departure)  

def booking_main():
    engine = create_engine('sqlite:///memory', echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    b=Booking()
    booking = session.query(Booking)
    
    print("-- Select a Booking function to Enter below: --\n")
    print("   1 Add Booking\n")
    print("   2 Edit Booking\n")
    print("   3 Search Booking\n")
    print("   4 Delete Booking\n")
    print("   0 Exit\n")
  
    ch=int(input("Enter a Booking function number:"))
     
    if ch == 1:
        print(" ")
        b.add_booking()
     
    elif ch == 2:
        print(" ")
        b.edit_booking()
     
    elif ch == 3:
        print(" ")
        b.search_booking()
     
    elif ch == 4:
        print(" ")
        b.delete_booking()
        
    elif ch == 0:
        print(" ")
        exit()
        
    else:
        booking_main()
    
    print()
    print("----")
    print()
    
   
        
#booking_main()     