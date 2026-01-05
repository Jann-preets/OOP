class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
        pass
    
    def deposit(self,amount):
        self.__balance+=amount
        pass
    
    def withdraw(self,amount):
        self.__balance-=amount
        pass
    def get_bal(self):
        print(f"balance: {self.__balance}")
        pass
    
s1=BankAccount(1000)
s1.get_bal()
s1.deposit(500)
s1.get_bal()
s1.withdraw(200)
s1.get_bal()