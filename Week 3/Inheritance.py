class Employee:
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
                
                    
class SalaryEmployee(Employee):
    def __init__(self, name, id, salary, hours_worked):
        super().__init__(name, id, hours_worked)
        self.salary = salary
        
    def get_payroll(self):
        return self.salary
    
         
        
class HourlyEmployee(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name, id, hours_worked)
        self.hourly_rate = hourly_rate 
        
    def get_payroll(self):
        return self.hourly_rate * self.hours_worked
    
    
        
class ContractEmployee(Employee):
    def __init__(self, name, id, contract_rate, hours_worked):
        super().__init__(name, id, hours_worked)
        self.contract_rate = contract_rate
        
    def get_payroll(self):
        return self.contract_rate
    
   
    
salary = SalaryEmployee("John Doe", 1111, 1500, 720)
hourly = HourlyEmployee("Jane Doe", 2222, 10, 1440)
contract = ContractEmployee("Smith Doe",3333,600,10)

print(salary.get_payroll())
print(hourly.get_payroll())
print(contract.get_payroll())
print()
print(salary.get_vacation())
print(hourly.get_vacation())
print(contract.get_vacation())  