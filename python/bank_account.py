def puts(str):
    print('{}\n'.format(str))


class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name.upper()
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            puts('You just deposited ${}'.format(amount))
            self.check_balance()
        else:
            puts('Invalid deposit amount')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            puts('You just withdrew ${}'.format(amount))
            self.check_balance()
        else:
            puts('Insufficient balance')

    def check_balance(self):
        puts('Your current balance is ${}'.format(self.balance))

    def get_account_name(self):
        puts('Your account name is {}'.format(self.account_name))


jason = BankAccount('Jason Ho', 1000)

jason.get_account_name()

jason.check_balance()

jason.deposit(200)

jason.withdraw(300)

jason.deposit(-20)

jason.withdraw(905)
