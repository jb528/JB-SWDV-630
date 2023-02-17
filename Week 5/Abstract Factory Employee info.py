from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
   def __init__(self, name, id, hours_worked):
      self.name = name
      self.id = id
      self.hours_worked = hours_worked

   def get_vacation(self):
        if self.hours_worked < 720:
            return 0
        else:
            num = self.hours_worked / 720
            days = num * 2.5
            return days

   @abstractmethod 
   def get_role(self):
    pass

   def __str__(self):
       return "{} - {}, ID# {}, Hrs-{}".format(self.__class__. __name__, self.name, self.id, self.hours_worked)

class Salary(Employee):
    def __init__(self, name, id, hours_worked, salary):
        super().__init__(name, id, hours_worked)
        self.salary = salary
        
    def get_payroll(self):
        return self.salary

    def get_role(self):
      return "salary"

class Hourly(Employee):
    def __init__(self, name, id, hours_worked, hourly_rate):
        super().__init__(name, id, hours_worked)
        self.hourly_rate = hourly_rate 
        
    def get_payroll(self):
        return self.hourly_rate * self.hours_worked

    def get_role(self):
      return "hourly"

class Contract(Employee):
    def __init__(self, name, id, hours_worked, contract_rate):
        super().__init__(name, id, hours_worked)
        self.contract_rate = contract_rate
        
    def get_payroll(self):
        return self.contract_rate
    
    def get_role(self):
      return "contract"

class EmployeeFactory(object):
   @classmethod
   def create(cls, name, *args):
      name = name.lower().strip()

      if name == 'salary':
         return Salary(*args)
      elif name == 'hourly':
         return Hourly(*args)
      elif name == 'contract':
         return Contract(*args)

def main():
   factory = EmployeeFactory()
   s1 = factory.create('salary', 'Sam', 25, 720, 999)
   print (EmployeeFactory.create('salary', 'Tracy', 28, 50, 888)) #better

   h1 = factory.create('hourly', 'Hema', 39, 100, 10)
   print (h1)

   c1 = factory.create('Contract', 'Supritha', 32, 150, 60)
   print(c1.get_payroll())
   print(c1.get_vacation())
   print(s1.get_payroll())
   print(s1.get_vacation())





main()