from abc import ABC

from Invoice import Invoice


class Shop(ABC):
    def __init__(self, repository=None, warehouse=None):
        self.__invoice_repository = repository
        self.__warehouse_repository = warehouse

    def buy(self, customer, items_list):
        price = 0
        for item in items_list:
            price += self.__warehouse_repository.sell_product(
                item["name"], item["amount"])
        invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=customer, items=items_list,
                          price=price)
        self.invoice_repository.add(invoice)
        return invoice

    def returning_goods(self, invoice):
        if self.invoice_repository.find_by_number(invoice.number):
            for item in invoice.items:
                self.__warehouse_repository.return_product(
                    item["name"], item["amount"])
            self.invoice_repository.delete(invoice)
            return True
        else:
            return False

    def partial_returning_goods(self, invoice, items_list):
        if self.invoice_repository.find_by_number(invoice.number):
            refund = 0
            for item in items_list:
                refund += self.__warehouse_repository.return_product(
                    item["name"], item["amount"])
            new_list = [
                item for item in invoice.items if item not in items_list]
            invoice.items = new_list
            invoice.price -= refund
            self.__invoice_repository.update(invoice)
            return True
        else:
            return False

    @property
    def invoice_repository(self):
        return self.__invoice_repository
