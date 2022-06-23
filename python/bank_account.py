class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('You just deposited ${}'.format(amount))
        self.check_balance()

    def withdraw(self, amount):
        self.balance -= amount
        print('You just withdrew ${}'.format(amount))
        self.check_balance()

    def check_balance(self):
        print('Your current balance is ${}'.format(self.balance))


jason = BankAccount('jason', 1000)

jason.check_balance()

jason.deposit(200)

jason.withdraw(300)
