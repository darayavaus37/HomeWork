class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return (f'{self._name}\n'
                f'{self._balance}')

    def money_x(self, amount):
        self._balance += amount
        return self._balance
        print(self._balance)


    def _jackpott(self):
        self._balance *= 10
        return self._balance
        print(self._balance)

    def _kill(self):
        self._balance = 0
        print(f'{self._name}  ваши деньги были обнулины {self._balance}')

    def _united(self, other):
        summa = self._balance + other
        return summa




account = Bank('Erzhan', 1200)
account2 = Bank('Tilek', 2200)
print(account)
print(account.money_x(500))

print(account._jackpott())
print(account._united(account2._balance))
account._kill()