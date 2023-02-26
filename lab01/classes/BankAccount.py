from datetime import datetime

from classes.TransactionHistory import TransactionHistory


class WrongDepositException(Exception):
    pass


class WrongWithdrawalException(Exception):
    pass


class BankAccount:
    def __init__(self, owner, account_number, bank) -> None:
        self.__owner = owner
        self.__account_number = account_number
        self.__bank = bank
        self.__transaction_history = TransactionHistory()
        self.__balance = 0

    @property
    def owner(self):
        return self.__owner

    @property
    def account_number(self):
        return self.__account_number

    @property
    def bank(self):
        return self.__bank

    @property
    def transaction_history(self):
        return self.__transaction_history

    @property
    def balance(self):
        return self.__balance

    def get_history(self):
        return self.transaction_history.history

    def get_history_from_time_period(self, start, end):
        return self.transaction_history.get_history_from_time_period(start, end)

    def _add_balance(self, amount) -> None:
        if amount < 0:
            raise WrongDepositException
        else:
            self.__balance += amount

    def _subtract_balance(self, amount) -> None:
        if amount < 0 or amount > self.balance:
            raise WrongWithdrawalException
        else:
            self.__balance -= amount

    def deposit(self, amount) -> None:
        self._add_balance(amount)
        self.transaction_history.add(
            "deposit", None, self.owner, amount, self.balance, datetime.now())

    def withdrawal(self, amount) -> None:
        self._subtract_balance(amount)
        self.transaction_history.add(
            "withdrawal", None, self.owner, amount, self.balance, datetime.now())

    def transfer(self, account_number, amount) -> None:
        getter: BankAccount = self.bank.find_account(account_number)
        self._subtract_balance(amount)
        getter._add_balance(amount)
        time = datetime.now()
        self.transaction_history.add("transfer", self.owner, getter.owner, amount, self.balance,
                                     time)
        getter.transaction_history.add("transfer", self.owner, getter.owner, amount, getter.balance,
                                       time)
