from classes.TransactionEntry import TransactionEntry


class WrongTimePeriodException(Exception):
    pass


class TransactionHistory:
    def __init__(self) -> None:
        self.__history = []

    @property
    def history(self):
        return self.__history

    def add(self, transaction_type, sender, getter, amount, balance_after, date):
        entry = TransactionEntry(
            transaction_type, sender, getter, amount, balance_after, date)
        self.history.append(entry)
        return entry

    def get_history_from_time_period(self, start, end):
        if start >= end:
            raise WrongTimePeriodException
        result = []
        for entry in self.history:
            if start <= entry.date <= end:
                result.append(entry)
        return result
