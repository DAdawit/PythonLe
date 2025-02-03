from bank_accounts import *

dave = BankAccount("Dave",2000)
sara = BankAccount("Sara",2000)

# dave.get_balance()

# dave.deposit()

# dave.withdraw()
# dave.transfer(sara)
# sara.get_balance()


jim = InteresRewardAcct("Jim",100)

# jim.deposit(200)
# jim.get_balance()

# jim.transfer(dave)
# jim.get_balance()

# dave.get_balance()


kasu = SavingAccount("Kasu", 50000)
kasu.withdraw(500)
kasu.get_balance()