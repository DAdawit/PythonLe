class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account  '{self.name}' Created. \nYour balance is : {self.balance}")
    
    def get_balance(self):
        print(f"'{self.name}' Your current balance is {self.balance}")
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Your '{self.name}' account credited Successfully. \nYour current balance is {self.get_balance()}")
   
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"Your '{self.name}' account credited Successfully. \nYour current balance is {self.get_balance()}")
        except BalanceException as error:
            print(f"Withdraw inturrapted : \n{error}")
    
    def transfer(self, recipient, amount):
        print("************")
        try:
            print(f"Beginning Transfer ... 🚀🚀🚀")
            self.viableTransaction(amount)
            self.balance -= amount
            recipient.balance += amount
            print(f"Transfer Complete! ✅✅✅. \nYour current balance is {self.get_balance():.2f}")
            print("************")
        except BalanceException as error:
            print(f"Transfer inturrapted : \n{error}")


class InteresRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount + (amount * 0.01)
        print(f"Your '{self.name}' account credited Successfully. \nYour current balance is {self.get_balance()}")
        

class SavingAccount(InteresRewardAcct):
    def __init__(self, acctName, initialAmount):
        super().__init__(acctName, initialAmount)
        self.fee = 5

    def withdraw(self, amount): 
        try: 
            print(type(amount))
            print(type(self.fee))
            print(self.balance)
            print(f"type of self balance :{type(self.balance)}")
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.get_balance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')