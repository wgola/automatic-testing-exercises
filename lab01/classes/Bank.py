from classes.BankAccount import BankAccount


class WrongAccountNumberLengthException(Exception):
    pass


class AccountAlreadyExistingException(Exception):
    pass


class NoAccountInBankException(Exception):
    pass


class Bank:

    def __init__(self) -> None:
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts

    def add_account(self, owner, account_number):
        if len(account_number) != 16:
            raise WrongAccountNumberLengthException
        else:
            for account in self.accounts:
                if account.account_number == account_number:
                    raise AccountAlreadyExistingException
            account = BankAccount(owner, account_number, self)
            self.accounts.append(account)
            return account

    def remove_account(self, account_number) -> None:
        account_found = self.find_account(account_number)
        self.accounts.remove(account_found)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise NoAccountInBankException
