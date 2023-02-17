import copy

class Prototype(object):

  def clone(self):
    return copy.deepcopy(self)

class Guest(Prototype):
  def __init__(self, name, room_type, arrival_date, departure_date):
    self.name = name
    self.room_type = room_type
    self.arrival_date = arrival_date
    self.departure_date = departure_date

  def __str__(self):
    return 'Guest: {name},  Room Type: {room_type},  Dates: {d1} to {d2}'.format(name=self.name, room_type=self.room_type, d1=self.arrival_date, d2=self.departure_date)


def main():
  guest1 = Guest("John Doe", "King", "5/10/2023", "11/10/2023")
  print (guest1)

  guest2 = guest1.clone()
  guest2.name = "Jane Smith"
  guest2.arrival_date = "7/10/2023"
  print(guest2)

main()