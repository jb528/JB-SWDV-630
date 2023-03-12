from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Update,Delete,Insert
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker 
from datetime import datetime

#format hour:min:sec
#example time "2:15:45"

class Base(DeclarativeBase):
    pass

class Etimecard(Base):
    __tablename__ = "Etimecard"
        
    id=Column(Integer,primary_key=True)
    employee_id=Column(Integer)
    start_time=Column(String)
    end_time=Column(String)
    
    
    def add_timecard(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        user_input = int(input("Enter the Employee ID: "))
        user_input1 = str(input("Enter Start Time (hour:min:sec): "))
        user_input2 = str(input("Enter End Time (hour:min:sec): "))
        print()
        self.employee_id = employee_id = user_input
        self.start_time = start_time = user_input1
        self.end_time = end_time = user_input2
        
        r1 = self.employee_id,self.start_time,self.end_time
    
        a=Etimecard(employee_id = r1[0],start_time= r1[1],end_time=r1[2])
        print(a,"-- Has been added.")
        print()
        session.add(a)
        session.commit()
        time = session.query(Etimecard)
        
       
        print("Database Table Etimecard")
        for t in time:
            #The last data point is equation for calulating total hours worked
            print("Timecard Id:",t.id,"Employee Id:",t.employee_id,"Start Time:",t.start_time,"End Time:",t.end_time,"Total Hours: ",(
               (((datetime.strptime(t.end_time,"%H:%M:%S"))- (datetime.strptime(t.start_time,"%H:%M:%S"))).total_seconds()) /(60*60)  ))
        print()
        print()
        etimecard_main()
        return r1
    
    def edit_timecard(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        
        user_input1 = int(input("Enter the Employee ID: "))
        user_input2 = str(input("Enter the New End Time (hour:min:sec): "))
        
        
        u = session.query(Etimecard).get(user_input1)
        print(u)
        print("-")
        u.end_time = user_input2
        session.commit()
        print(u)
        print()
        print()
        etimecard_main()
        
    def search_timecard(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        time = session.query(Etimecard)
        
        user_input = int(input("Enter Timecard ID: "))
        
        for t in time:
            if t.id == user_input:
                print("ID#",user_input,"info:","Timecard Id:",t.id,"Employee Id:",t.employee_id,"Start Time:",t.start_time,"End Time:",t.end_time)    
                print()
                print()
                etimecard_main()
        
    def delete_timecard(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        time = session.query(Etimecard)
        
        user_input = int(input("Enter Timecard Id: "))
        
        for t in time:
            if t.id == user_input:
                session.delete(t)
                session.commit()
                print("Timecard Id:",user_input,"-- Has been deleted.")       
                print()
                print()
                etimecard_main()
               
        
    def __repr__(self):
        return "Employee Id: {0}, Start Time: {1}, End Time: {2}".format(self.employee_id,self.start_time,self.end_time)  

def etimecard_main():
    engine = create_engine('sqlite:///memory', echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    t=Etimecard()
    time = session.query(Etimecard)
    
    print("-- Select a Employee Timecard function to Enter below: --\n")
    print("   1 Add Employee Timecard\n")
    print("   2 Edit Employee Timecard\n")
    print("   3 Search Employee Timecard\n")
    print("   4 Delete Employee Timecard\n")
    print("   0 Exit\n")
  
    ch=int(input("Enter a Employee Timecard function number:"))
     
    if ch == 1:
        print(" ")
        t.add_timecard()
     
    elif ch == 2:
        print(" ")
        t.edit_timecard()
     
    elif ch == 3:
        print(" ")
        t.search_timecard()
     
    elif ch == 4:
        print(" ")
        t.delete_timecard()
        
    elif ch == 0:
        print(" ")
        exit()
        
    else:
        etimecard_main()
    
    print()
    print("----")
    print()
    
   
        
        
#etimecard_main() 