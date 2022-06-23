class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('You just deposited ${}'.format(amount))
            self.check_balance()
        else:
            print('Invalid deposit amount')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('You just withdrew ${}'.format(amount))
            self.check_balance()
        else:
            print('Insufficient balance')

    def check_balance(self):
        print('Your current balance is ${}'.format(self.balance))


jason = BankAccount('jason', 1000)

jason.check_balance()

jason.deposit(200)

jason.withdraw(300)

jason.deposit(-20)

jason.withdraw(905)
