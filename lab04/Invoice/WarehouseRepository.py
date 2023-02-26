from WarehouseEntry import WarehouseEntry


class OutOfStore(Exception):
    pass


class WarehouseRepository:
    def __init__(self, data_source=[]):
        self.__data_source = data_source

    def find_by_name(self, name: str) -> WarehouseEntry:
        return next((entry for entry in self.__data_source if entry.name == name), None)

    def add(self, magazine_entry):
        if not self.find_by_name(magazine_entry.name):
            self.__data_source.append(magazine_entry)
        else:
            found_entry = self.find_by_name(magazine_entry.name)
            found_entry.amount += magazine_entry.amount

    def delete(self, magazine_entry):
        self.__data_source.remove(magazine_entry)

    def change_price(self, name, new_price):
        self.find_by_name(name).price = new_price

    def sell_product(self, name, amount):
        product = self.find_by_name(name)
        if product is None or product.amount < amount:
            raise OutOfStore
        else:
            product.amount -= amount
            return product.price * amount

    def return_product(self, name, amount):
        product = self.find_by_name(name)
        if product is not None:
            product.amount += amount
            return product.price * amount

    @property
    def data_source(self):
        return self.__data_source
