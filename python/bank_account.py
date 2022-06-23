def puts(str):
    print('{}\n'.format(str))


class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name.upper()
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            puts(f'You just deposited ${amount}')
            self.get_balance()
        else:
            puts('Invalid deposit amount')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            puts(f'You just withdrew ${amount}')
            self.get_balance()
        else:
            puts('Insufficient balance')

    def get_balance(self):
        puts(f'Your current balance is ${self.balance}')

    def get_account_name(self):
        puts(f'Your account name is {self.account_name}')


jason = BankAccount('Jason Ho', 1000)

jason.get_account_name()

jason.get_balance()

jason.deposit(200)

jason.withdraw(300)

jason.deposit(-20)

jason.withdraw(905)
