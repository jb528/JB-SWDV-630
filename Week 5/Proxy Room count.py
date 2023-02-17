from abc import ABCMeta, abstractmethod

class Room(metaclass=ABCMeta):
   def __init__(self, price, bed_number, sleeping_capacity):
      self.price = price
      self.bed_number = bed_number
      self.sleeping_capacity = sleeping_capacity

   @abstractmethod
   def get_type(self):
         pass

   def __str__(self):
       return "{} - ${} per night, #beds-{}, sleeping capacity-{}".format(self.__class__. __name__, self.price, self.bed_number, self.sleeping_capacity)



class Suite(Room):
   def get_type(self):
      return "suite"

class King(Room):
   def get_type(self):
      return "king"

class Queen(Room):
   def get_type(self):
      return "queen"



class RoomProxy(object):
# Count of rooms
  count = 0

  def __new__(cls, *args):
  # To keep track of counts
    instance = object.__new__(cls)
    cls.incr_count()
    return instance

  def __init__(self, room):
    self.room = room

  @classmethod
  def incr_count(cls):
    """ Increment room count """
    cls.count += 1

  @classmethod
  def decr_count(cls):
    """ Decrement room count """
    cls.count -= 1

  @classmethod
  def get_count(cls):
    """" Get room count """
    return cls.count

  def __str__(self):
    return str(self.room)

  def __getattr__(self, name):
     """ Redirect attributes to room instance """
     return getattr(self.room, name)

  def __del__(self):
     """ Overloaded __del__ method """
     # Decrement room count
     self.decr_count()

class RoomProxyFactory(object):
  """ An Room factory class returning proxy objects """
  @classmethod
  def create(cls, name, *args):
    """ Factory method for creating an Room instance """
    name = name.lower().strip()
    if name == 'suite':
     return RoomProxy(Suite(*args))
    elif name == 'king':
     return RoomProxy(King(*args))
    elif name == 'queen':
     return RoomProxy(Queen(*args))

   
  
def main():

  suite = RoomProxyFactory.create('suite',500,2,4)
  print(suite)

  king = RoomProxyFactory.create('king',400,1,2)

  print(king.get_count())
  print(RoomProxy.get_count())

  del suite
  print(RoomProxy.get_count())

  del king
  print(RoomProxy.get_count())

main()