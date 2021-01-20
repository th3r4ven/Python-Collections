class Account:

    def __init__(self, code):
        self.__code = code
        self.__money = 0

    def deposit(self, value):
        self.__money += value

    def __str__(self):
        return f'Bank code: {self.__code} Money: {self.__money}'


def deposit_everyone(accounts):
    for account in accounts:
        account.deposit(100)


if __name__ == '__main__':

    account01 = Account(666)
    account02 = Account(555)
    account01.deposit(100)
    account02.deposit(500)

    accounts = (account01,  account02)
    deposit_everyone(accounts)

    print(accounts)
