from decimal import Decimal
class CheckingAccount:
    #private variable has _ in front
    amount = 0 
    def __init__(self,_fname,_lname,_address,_accountNumber,_balance):
        self.fname = _fname
        self.lname = _lname
        self.address = _address
        self.accountNumber = _accountNumber
        self.balance = round(Decimal(_balance),2)
             
    def creditAccount(self):
        self.balance = self.balance + amount
        return self.balance 
        
    def debitAccount(self):
        if -(self.checkBalance()) < amount:
            self.balance = self.balance + amount
            return self.balance
        else:    
            print("There are Insuffient funds to complete transaction.")
                
    def checkBalance(self):
        return self.balance

    def runTransaction(self):
        response = input("What is the total amount you wish to deposit(enter positive number) or \n withdraw (enter negative number)?: ")
        global amount
        amount = round(Decimal(response),2)
        if amount > 0:
            self.creditAccount()
        else:
            self.debitAccount()
        print("Your balance is:",+self.balance)
        print()
    
    




