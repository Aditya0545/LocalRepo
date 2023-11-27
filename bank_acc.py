'''Create a heirarical bank accounts classes using inheritance. start with a base class bank accounts with common attributes and methods for all types of bank accounts then create derived class such as saving accounts and checking accounts that inherit from the bank account class but also have their specific attributes and methods'''

class Bank_accounts():
    def account_type(self):
        print("1. Demat Account\n2. Current Account\n3. Saving Account")

class Saving_accounts(Bank_accounts):
    def sav_info(self):
        print("Saving Account information:\nAccount Holder's: Abhimanyu Gurjar\nAccount Number: 3455656646656\nInterest rate: 7.54%")

class Checking_accounts(Bank_accounts):
    def Acc_info(self):
        print("Checking Account Information:\nAccount Holder's: Rohan Mishra\nAccount number: 10003425674\nAvailable Balance: $1200")

check1 = Saving_accounts()
check1.account_type()
print("\n")
check1.sav_info()

check2 = Checking_accounts()
check2.account_type()
print("\n")
check2.Acc_info()
