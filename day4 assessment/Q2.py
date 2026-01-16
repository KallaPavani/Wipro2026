class BankAccount():
    def __init__(self,account_num,balance):
        self.account_num=account_num
        self.balance=balance
        print("Account Created:",self.account_num)

    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print("Current Balance:",self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount<=0:
            print("Invalid withdraw amount")
        elif amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Withdrawn:",amount)
            print("Remaining Balance:",self.balance)

    def __del__(self):
        print("Account deleted:",self.account_num)


account=BankAccount(456889,3000)
account.deposit(2000)
account.withdraw(4000)
account.withdraw(300)

del account

