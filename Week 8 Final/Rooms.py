from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Update,Delete,Insert
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker 



class Base(DeclarativeBase):
    pass

class Rooms(Base):
    __tablename__ = "Rooms"
        
    id=Column(Integer,primary_key=True)
    _number=Column(String)
    _type=Column(String)
    _description=Column(String)
    
    
    def edit_room(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        
        user_input1 = str(input("Enter the Room ID you wish to change: "))
        user_input2 = str(input("Enter the New Room Number you wish to change to: "))
        
        u = session.query(Rooms).get(user_input1)
        print(u)
        print("-")
        u._number=user_input2
        session.commit()
        print(u)
        print()
        print()
        rooms_main()
        
    def search_room(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        room = session.query(Rooms)
        
        user_input = int(input("Enter Room ID to search: "))
        print()
        for r in room:
            if r.id == user_input:
                print("ID#",user_input,"info:","Room Id:",r.id,"Room Number:",r._number,"Room Type:",r._type,"Room Description:",r._description)    
                print()
                print()
                rooms_main()
                
    def delete_room(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        rooms = session.query(Rooms)
        
        user_input = int(input("Enter the Room Id to delete: "))
        print()
        for r in rooms:
            if r.id == user_input:
                session.delete(r)
                session.commit()
                print(user_input,"-- Has been deleted.")       
                print()
                print()
                rooms_main()
        
    def add_room(self):
        engine = create_engine('sqlite:///memory', echo = False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        user_input= int(input("Enter a Room Number to add between 1 and 30: "))
        
        if (user_input >= 1) and (user_input <=30):
            self._number = _number = user_input
        else:
            print("Invalid Number - Please try agian")
            r=Rooms()
            r.add_room()
        
        if (user_input >= 1) and (user_input <=10):
            self._type = _type = "King Bed"
        if (user_input >= 11) and (user_input <=20):
            self._type = _type = "Queen Bed"   
        if (user_input >= 21) and (user_input <=30):
            self._type = _type = "Single Bed"
        
        if self._type == "King Bed":
            self._description = _description = "Sleeps 4"
        if self._type == "Queen Bed":
            self._description = _description = "Sleeps 2"    
        if self._type == "Single Bed":
            self._description = _description = "Sleeps 1"
       
        r1 = self._number,self._type,self._description
        
        
        a=Rooms(_number = r1[0],_type= r1[1],_description=r1[2])
        print()
        print(a,"-- Has been added.")
        print()
        session.add(a)
        session.commit()
        rooms = session.query(Rooms)
        print("Database Table Rooms")
        for r in rooms:
            
            print("Room Id:",r.id,"Room Number:",r._number,"Room Type:",r._type,"Room Description:",r._description)
        print()
        print()
        rooms_main()
        return r1
        
        
    def __repr__(self):
        return "Room Number: {0}  Room Type: {1}  description: {2}".format(self._number,self._type,self._description)  

def rooms_main():
    engine = create_engine('sqlite:///memory', echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    r=Rooms()
    rooms = session.query(Rooms)
    
    print("-- Select a Rooms function to Enter below: --\n")
    print("   1 Add Rooms\n")
    print("   2 Edit Rooms\n")
    print("   3 Search Rooms\n")
    print("   4 Delete Rooms\n")
    print("   0 Exit\n")
  
    ch=int(input("Enter a Rooms function number:"))
     
    if ch == 1:
        print(" ")
        r.add_room()
     
    elif ch == 2:
        print(" ")
        r.edit_room()
     
    elif ch == 3:
        print(" ")
        r.search_room()
     
    elif ch == 4:
        print(" ")
        r.delete_room()
        
    elif ch == 0:
        print(" ")
        exit()
        
    else:
        rooms_main()
    
    print()
    print("----")
    print()
  
   
        
#rooms_main()    