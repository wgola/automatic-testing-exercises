class TransactionEntry:
    def __init__(self, transaction_type, sender, getter, amount, balance_after, date) -> None:
        self.__transaction_type = transaction_type
        self.__sender = sender
        self.__getter = getter
        self.__amount = amount
        self.__balance_after = balance_after
        self.__date = date

    @property
    def transaction_type(self):
        return self.__transaction_type

    @property
    def sender(self):
        return self.__sender

    @property
    def getter(self):
        return self.__getter

    @property
    def amount(self):
        return self.__amount

    @property
    def balance_after(self):
        return self.__balance_after

    @property
    def date(self):
        return self.__date

    def get_entry_info(self):
        if self.__transaction_type == "transfer":
            return "Type: {0} | From: {1} | To: {2} | Amount: {3} | Balance after: {4} | Date: {5}".format(
                self.transaction_type, self.sender.name + " " + self.sender.surname, self.getter.name + " " +
                self.getter.surname, self.amount, self.balance_after, self.date)
        else:
            return "Type: {0} | Amount: {1} | Balance after: {2} | Date: {3}".format(self.transaction_type,
                                                                                     self.amount, self.balance_after,
                                                                                     self.date)
