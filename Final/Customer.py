from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Update,Delete,Insert
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker



class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "Customer"
        
    id=Column(Integer,primary_key=True)
    fname=Column(String)
    lname=Column(String)
    username=Column(String)
    password=Column(String)
    
    
    def edit_customer(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        
        user_input1 = str(input("Enter Customer's ID: "))
        user_input2 = str(input("Enter new password: "))
        
        u = session.query(Customer).get(user_input1)
        print(u)
        print("-")
        u.password=user_input2
        session.commit()
        print(u)
        print()
        print()
        customer_main()
        
    def search_customer(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        customer = session.query(Customer)
        
        user_input = str(input("Enter Customer's Last Name to search for: "))
        
        for c in customer:
            if c.lname == user_input:
                print()
                print("Last Name:",user_input,", info-","Customer Id:",c.id," First Name:",c.fname," Last Name",c.lname," username:",c.username," password:",c.password)
                print()
                print()
                customer_main()
                
    def delete_customer(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        customer = session.query(Customer)
        
        user_input = str(input("Enter the Last Name of the Customer to delete: "))
        
        for c in customer:
            if c.lname == user_input:
                session.delete(c)
                session.commit()
                print()
                print(user_input,"--Has been deleted.")
                print()
                print()
                customer_main()
    
    def add_customer(self):
        
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        self.fname = fname = input("Enter Customer First Name: ")
        self.lname = lname = input("Enter Customer Last Name: ")
        self.username = username = input("Enter Customer username: ")
        self.password = password = input("Enter Customer password: ")
        print()
        c1= self.fname,self.lname,self.username,self.password
        b=Customer(fname = c1[0],lname= c1[1],username=c1[2],password=c1[3])
        print(b,"--Has been added.")
        print()
        session.add(b)
        session.commit()
        customer = session.query(Customer)
        
        print("Database Table - Customer")
        for c in customer:
            
            print("Customer Id:",c.id," First Name:",c.fname," Last Name:",c.lname)
        print()
        print()
        customer_main()
        return c1
        
        
    def __repr__(self):
        return "First Name:{0}  Last Name:{1}  username: {2}  password: {3}".format(self.fname,self.lname,self.username,self.password)  

def customer_main():
    engine = create_engine('sqlite:///memory', echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    customer = session.query(Customer)
    c=Customer()
    
    
    print("-- Select a Customer function to Enter below: --\n")
    print("   1 Add Customer\n")
    print("   2 Edit Customer\n")
    print("   3 Search Customer\n")
    print("   4 Delete Customer\n")
    print("   0 Exit\n")
  
    ch=int(input("Enter a Customer function number:"))
     
    if ch == 1:
        print(" ")
        c.add_customer()
     
    elif ch == 2:
        print(" ")
        c.edit_customer()
     
    elif ch == 3:
        print(" ")
        c.search_customer()
     
    elif ch == 4:
        print(" ")
        c.delete_customer()
        
    elif ch == 0:
        print(" ")
        exit()
        
    else:
        customer_main()
    
    print()
    print("----")
    print()
  
    
#customer_main()    