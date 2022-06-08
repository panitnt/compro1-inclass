class BankAccount:
    def __init__(self, number, name, balance, db):
        self.number = number
        self.name = name
        self.balance = balance
        self.db = db
        db.insert(self)

    # add your implementation
    @property
    def number(self):
        '''get number'''
        return self.__number

    @number.setter
    def number(self, number):
        '''set number'''
        if not isinstance(number, str):
            raise TypeError('account number must be a string')
        self.__number = number

    @property
    def name(self):
        '''get name'''
        return self.__name

    @name.setter
    def name(self, name):
        '''set name'''
        if not isinstance(name, str):
            raise TypeError('account name must be a string')
        self.__name = name

    @property
    def balance(self):
        '''get balance'''
        return self.__balance

    @balance.setter
    def balance(self, balance):
        '''set balance'''
        if not isinstance(balance, (int, float)):
            raise TypeError('balance must be a number')
        if balance <= 0:
            raise ValueError('balance must be greater than zero')
        self.__balance = balance

    @property
    def db(self):
        '''get database'''
        return self.__db

    @db.setter
    def db(self, db):
        '''set database'''
        self.__db = db

    def deposit(self, amount):
        '''to deposit money'''
        # add your implementation
        self.__balance += amount
        self.db.record_transaction(self, amount)  # to update to .json

    def withdraw(self, amount):
        '''to withdraw money'''
        # add your implementation
        if amount <= self.balance:
            self.__balance -= amount
            self.db.record_transaction(self, -amount)  # to update to .json
        else:
            print('Not enough money')

    def transfer(self, amount, to_account):
        # add your implementation
        if amount <= self.balance:
            self.__balance -= amount
            to_account.balance += amount
            self.db.record_transaction(self, -amount)  # to update to .json
            to_account.db.record_transaction(to_account, amount)  # to update to .json
        else:
            print('Not enough money')

    def __repr__(self):
        '''to representation of an object'''
        # add your implementation
        return f'Account(number="{self.number}", name="{self.name}", balance={self.balance}, db="{self.db.name}")'
