from CheckingAccount import CheckingAccount

ca = CheckingAccount("Bob","Duck","545 elm dr", "35453", 100.10)

print("Account holder's First Name:",ca.fname)
print("Account holder's Last Name:",ca.lname)
print("Account holder's Address:",ca.address)
print("Account Number:",ca.accountNumber)
print("Account Balance:",ca.balance)
print()
ca.runTransaction()
ca.runTransaction()
ca.runTransaction()
ca.runTransaction()
