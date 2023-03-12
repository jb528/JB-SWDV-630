from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Update,Delete,Insert
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker 



class Base(DeclarativeBase):
    pass

class Epaycheck(Base):
    __tablename__ = "Epaycheck"
        
    id=Column(Integer,primary_key=True)
    employee_id=Column(Integer)
    rate=Column(Integer)
    hours=Column(Integer)
    
    
    def add_paycheck(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        user_input = int(input("Enter the Employee ID: "))
        user_input1 = int(input("Enter the Employee pay rate: "))
        user_input2 = int(input("Enter the Employee hours work: "))
        print()
        self.employee_id = employee_id = user_input
        self.rate = rate = user_input1
        self.hours = hours = user_input2
        
        r1 = self.employee_id,self.rate,self.hours
    
        a=Epaycheck(employee_id = r1[0],rate= r1[1],hours=r1[2])
        print(a,"-- Has been added.")
        print()
        session.add(a)
        session.commit()
        pay = session.query(Epaycheck)
        
        print("Paycheck Table")
        for p in pay:
            print("Paycheck Id:",p.id,"Employee Id:",p.employee_id,"Rate:",p.rate,"Hours:",p.hours,"Amount: $",(p.rate*p.hours))
        print()
        print()
        epaycheck_main()
        return r1
    
    def edit_paycheck(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        
        user_input1 = int(input("Enter the Paycheck ID: "))
        user_input2 = int(input("Enter the New Hours: "))
        
        u = session.query(Epaycheck).get(user_input1)
        print(u)
        print("-")
        u.hours = user_input2
        session.commit()
        print(u)
        print()
        print()
        epaycheck_main()
        
    def search_paycheck(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        pay = session.query(Epaycheck)
        
        user_input = int(input("Enter Paycheck ID: "))
        
        for p in pay:
            if p.id == user_input:
                print("ID#",user_input,"info:","Paycheck Id:",p.id,"Employee Id:",p.employee_id,"Rate:",p.rate,"Hours:",p.hours)    
                print()
                print()
                epaycheck_main()
        
    def delete_paycheck(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        pay = session.query(Epaycheck)
        
        user_input = int(input("Enter Paycheck Id: "))
        
        for p in pay:
            if p.id == user_input:
                session.delete(p)
                session.commit()
                print("Paycheck Id:",user_input,"-- Has been deleted.")       
                print()
                print()
                epaycheck_main()
               
        
    def __repr__(self):
        return "Employee Id: {0}, Rate: {1}, Hours: {2}".format(self.employee_id,self.rate,self.hours)  

def epaycheck_main():
    engine = create_engine('sqlite:///memory', echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    p=Epaycheck()
    pay = session.query(Epaycheck)
    
    print("-- Select a Employee Paycheck function to Enter below: --\n")
    print("   1 Add Employee Paycheck\n")
    print("   2 Edit Employee Paycheck\n")
    print("   3 Search Employee Paycheck\n")
    print("   4 Delete Employee Paycheck\n")
    print("   0 Exit\n")
  
    ch=int(input("Enter a Employee Paycheck function number:"))
     
    if ch == 1:
        print(" ")
        p.add_paycheck()
     
    elif ch == 2:
        print(" ")
        p.edit_paycheck()
     
    elif ch == 3:
        print(" ")
        p.search_paycheck()
     
    elif ch == 4:
        print(" ")
        p.delete_paycheck()
        
    elif ch == 0:
        print(" ")
        exit()
        
    else:
        epaycheck_main()
    
    print()
    print("----")
    print()
    
  
        
        
#epaycheck_main() 