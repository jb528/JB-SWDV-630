from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker 

class Base(DeclarativeBase):
    pass

class Guest(Base):
    def __init__(self, fname,lname,arrival_date,departure_date,room_type):
        self.fname=fname
        self.lname=lname
        self.arrival_date=arrival_date
        self.departure_date=departure_date
        self.room_type=room_type
        
    __tablename__ = "guest"
        
    id=Column(Integer,primary_key=True)
    fname=Column(String)
    lname=Column(String)
    arrival_date=Column(String)
    departure_date=Column(String)
    room_type=Column(String)
    
    def __repr__(self):
        return "{0} {1}, Staying from {2} to {3}, Room type: {4}".format(self.fname,self.lname,self.arrival_date,self.departure_date,self.room_type)  





def main():
    engine = create_engine('sqlite:///memory', echo = False)
    
    Base.metadata.create_all(engine)
    
    
    g1=Guest('John','Smith','2/23/2023','2/27/2023','King')
    print(g1)
    print()
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.add(g1)
    
    session.add_all([
        Guest('Jake','Frost','2/23/2023','2/27/2023','King'),
        Guest('Jane','Heart','2/23/2023','2/27/2023','Queen'),
        Guest('Tim','Bob','2/23/2023','2/27/2023','King'),
        Guest('Doug','Wave','2/23/2023','2/27/2023','Suite')
        ])
    
    
    session.flush()
    
    guest = session.query(Guest)
    
    for g in guest:
        print(g.fname,g.room_type)
    
main()    
    