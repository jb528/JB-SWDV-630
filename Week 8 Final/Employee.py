from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Update,Delete,Insert
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker 



class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "Employee"
        
    id=Column(Integer,primary_key=True)
    fname=Column(String)
    lname=Column(String)
    username=Column(String)
    password=Column(String)
    
    
    def edit_employee(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        
        user_input1 = str(input("Enter Employee's ID to edit: "))
        user_input2 = str(input("Enter new password: "))
        
        u = session.query(Employee).get(user_input1)
        print(u)
        print("-")
        u.password=user_input2
        session.commit()
        print(u)
        print()
        print()
        employee_main()
        
    def search_employee(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        employee = session.query(Employee)
        
        user_input = str(input("Enter Employee's Last Name to search for: "))
        
        for e in employee:
            if e.lname == user_input:
                print("Last Name:",user_input,", info-","Employee Id:",e.id," First Name:",e.fname," Last Name",e.lname," username:",e.username," password:",e.password)
                print()
                print()
                employee_main()
                
    def delete_employee(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        employee = session.query(Employee)
        
        user_input = str(input("Enter the Last Name of the Employee to delete: "))
        
        for e in employee:
            if e.lname == user_input:
                session.delete(e)
                session.commit()
                print(user_input,"-- Has been deleted.")
                print()
                print()
                employee_main()
        
    def add_employee(self):
        
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        self.fname = fname = input("Enter Employee First Name: ")
        self.lname = lname = input("Enter Employee Last Name: ")
        self.username = username = input("Enter Employee username: ")
        self.password = password = input("Enter Employee password: ")
        print()
        e1= self.fname,self.lname,self.username,self.password
        b=Employee(fname = e1[0],lname= e1[1],username=e1[2],password=e1[3])
        print(b,"--Has been added.")
        print()
        session.add(b)
        session.commit()
        employee = session.query(Employee)
        
        print("Database Table Employee")
        for e in employee:
            print("Employee Id:",e.id," First Name:",e.fname," Last Name:",e.lname)
        print()
        print()
        employee_main()
        return e1
        
        
    
    def __repr__(self):
        return "First Name:{0}  Last Name:{1}  username: {2}  password: {3}".format(self.fname,self.lname,self.username,self.password)  

def employee_main():
    engine = create_engine('sqlite:///memory', echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    employee = session.query(Employee)
    e=Employee()
    
    
    print("-- Select a Employee function to Enter below: --\n")
    print("   1 Add Employee\n")
    print("   2 Edit Employee\n")
    print("   3 Search Employee\n")
    print("   4 Delete Employee\n")
    print("   0 Exit\n")
  
    ch=int(input("Enter a Employee function number:"))
     
    if ch == 1:
        print(" ")
        e.add_employee()
     
    elif ch == 2:
        print(" ")
        e.edit_employee()
     
    elif ch == 3:
        print(" ")
        e.search_employee()
     
    elif ch == 4:
        print(" ")
        e.delete_employee()
        
    elif ch == 0:
        print(" ")
        exit()
        
    else:
        employee_main()
    
    print()
    print("----")
    print()
    
    
   
    
    
#employee_main()    