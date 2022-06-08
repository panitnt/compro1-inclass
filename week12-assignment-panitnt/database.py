import json


class BankDB:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        '''get name'''
        return self.__name

    @name.setter
    def name(self, name):
        '''set name'''
        self.__name = name

    def insert(self, bank_account):
        '''to insert new data to database file when initialize the BankAccount object'''
        # add your implementation
        new_data = {
            bank_account.number: {
                "name": bank_account.name,
                "balance": bank_account.balance
            }
        }
        try:
            with open('accounts.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('accounts.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('accounts.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

    def search(self, account_number):
        '''to search for a bank account'''
        # add your implementation
        try:
            with open('accounts.json', 'r') as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print('No data file found.')
        else:
            if account_number in data_dict:
                name = data_dict[account_number]['name']
                balance = data_dict[account_number]['balance']
                print(f'Name={name}, Balance={balance}')
            else:
                print(f'No data for account number: {account_number}')

    def delete(self, account_number):
        '''to delete a bank account'''
        # add your implementation
        try:
            with open('accounts.json', 'r') as data_file:
                data_dict = json.load(data_file)
        except KeyError:
            pass
        else:
            try:
                data_dict.pop(account_number)
            except KeyError:
                print(f'No data for account number: {account_number}')
            else:
                print(f'DELETE account {account_number}')
                with open('accounts.json', 'w') as data_file:
                    json.dump(data_dict, data_file, indent=4)

    def record_transaction(self, account, amount):
        '''to record transaction when withdraw or deposit money'''
        # add your implementation
        try:
            with open('accounts.json', 'r') as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print('Expected nothing')
        else:
            if account.number in data_dict:
                print(f'UPDATE account {account.number} balance = {account.balance}')
                update_data = {
                    account.number: {
                        "name": account.name,
                        "balance": account.balance
                    }
                }
                data_dict.update(update_data)  # to update data in new dict
                with open('accounts.json', 'w') as data_file:
                    json.dump(data_dict, data_file, indent=4)  # update to .json file

    def __repr__(self):
        '''to representation of an object'''
        # add your implementation
        return f'BankDB(name="{self.name}")'
