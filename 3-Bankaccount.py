#                               3. BankAccount
# Create a Python class called BankAccount which represents a bank account, having as attributes: 
# accountNumber, name , balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a deposit() method which manages the deposit actions. (deposit() method will take parameter d
#  and you will increase the balance with the amount d)
# Create a withdrawal() method which manages withdrawals actions. (withdrawal() method will take
#  parameter w, you will reduce the amount of balance with w, if w is larger than the balance:
#  then print Impossible operation! Insufficient balance!")
# Create a bankFees() method to apply the bank fees with a percentage of 5% of the balance account. 
# (When this method is called, the balance amount should reduce 5%)
# Create a display() method to display account details.

class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def deposit(self,d):
        self.balance +=d 
        print("Your amount was deposited")
        return self.balance

    def withdrawal(self,w):
        if w>self.balance:
            print( "Impossible operation! Insufficient balance!")
        else:
           self.balance-=w
           print("Your amount was withdrawaled")
           return self.balance

    def bankfees(self):
        self.balance=self.balance-self.balance*5/100
        print("Your bank fees was paid")

    def display(self):
        print(" Mr./Mrs.{} \n Your accound number:{} \n Your balance is:{} ".format(self.name,self.accountNumber,self.balance))
    
object_1=BankAccount(123456,"Ali kaya",1550)
    
object_1.withdrawal(345)
object_1.deposit(245)
object_1.bankfees()
object_1.display()

