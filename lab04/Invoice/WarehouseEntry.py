class WarehouseEntry:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price if new_price > 0 else 0

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, new_amount):
        self.__amount = new_amount if new_amount > 0 else 0
