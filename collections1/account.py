from abc import ABCMeta, abstractmethod


class Account:

    __metaClass__ = ABCMeta

    def __init__(self, code):
        self._code = code
        self._money = 0

    @property
    def code(self):
        return self._code

    def deposit(self, value):
        self._money += value

    def __lt__(self, other):
        return self._money < other._money

    def __eq__(self, other):
        return isinstance(other, Account) and self._code == other._code

    def __str__(self):
        return f'Bank code: {self._code} Money: {self._money}'

    @abstractmethod
    def tax_per_month(self):
        pass


class Normal_account(Account):

    def tax_per_month(self):
        self._money -= 2


class Saving_account(Account):

    def tax_per_month(self):
        self._money *= 1.01
        self._money -= 3


if __name__ == '__main__':

    account01 = Account(666)
    account01 = Saving_account(account01.code)
    account02 = Account(555)
    account02 = Normal_account(account02.code)
    account01.deposit(100)
    account02.deposit(500)
    accounts = (account01,  account02)

    for account in accounts:
        account.tax_per_month()  # duck typing

    print(accounts[0])

    account01 = Account(666)
    account02 = Account(666)
    account02 = Saving_account(account02.code)

    if account01 == account02:
        print("True")

    # Sorted function, using account.money as key param to sort

    for account in sorted(accounts):
        print(account)
