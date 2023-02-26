import unittest
from unittest.mock import Mock, call
from InvoiceRepository import InvoiceRepository
from WarehouseRepository import WarehouseRepository, OutOfStore
from Shop import Shop
from Invoice import Invoice


class ShopTests(unittest.TestCase):

    def test_while_buy_the_repository_add_should_be_called(self):
        spy_repository = Mock(InvoiceRepository)
        stub_warehouse = Mock(WarehouseRepository)
        stub_warehouse.sell_product.return_value = 0

        shop = Shop(spy_repository, stub_warehouse)
        shop.buy(customer="Jan", items_list=[
                 {"name": "cukierki", "amount": 1}])

        spy_repository.add.assert_called_once()

    def test_while_buy_the_warehouse_sell_should_be_called_with_data(self):
        spy_warehouse = Mock(WarehouseRepository)
        spy_warehouse.sell_product.return_value = 0

        shop = Shop(Mock(InvoiceRepository), spy_warehouse)
        shop.buy(customer="Jan", items_list=[
                 {"name": "cukierki", "amount": 1}])

        spy_warehouse.sell_product.assert_called_once_with("cukierki", 1)

    def test_while_buy_many_products_the_warehouse_sell_should_be_called_many_times(self):
        spy_warehouse = Mock(WarehouseRepository)
        spy_warehouse.sell_product.return_value = 0

        shop = Shop(Mock(InvoiceRepository), spy_warehouse)
        shop.buy(customer="Jan", items_list=[
                 {"name": "cukierki", "amount": 1}, {"name": "książka", "amount": 2}])

        calls = [call("cukierki", 1), call("książka", 2)]
        spy_warehouse.sell_product.assert_has_calls(calls)

    def test_while_buy_no_products_the_warehouse_sell_should_not_be_called(self):
        spy_warehouse = Mock(WarehouseRepository)

        shop = Shop(Mock(InvoiceRepository), spy_warehouse)
        shop.buy(customer="Jan", items_list=[])

        spy_warehouse.sell_product.assert_not_called()

    def test_while_buy_non_existing_prodcuts_the_warehouse_sell_should_raise_exception(self):
        shop = Shop(Mock(InvoiceRepository), WarehouseRepository())

        with self.assertRaises(OutOfStore):
            shop.buy(customer="Jan", items_list=[
                     {"name": "cukierki", "amount": 1}])

    def test_while_returning_goods_the_repository_returns_false_when_not_find(self):
        stub_repository = Mock(InvoiceRepository)
        stub_repository.find_by_number.return_value = None

        shop = Shop(stub_repository, Mock(WarehouseRepository))
        result = shop.returning_goods(Mock(Invoice))

        self.assertEqual(result, False)

    def test_while_returning_goods_the_warehouse_return_should_be_called_when_find_with_data(self):
        spy_warehouse = Mock(WarehouseRepository)
        mocked_invoice = Mock(Invoice)
        mocked_invoice.items = [{"name": "cukierki", "amount": 1}]
        spy_repository = Mock(InvoiceRepository)
        spy_repository.find_by_number.return_value = mocked_invoice

        shop = Shop(spy_repository, spy_warehouse)
        shop.returning_goods(mocked_invoice)

        spy_warehouse.return_product.assert_called_once_with("cukierki", 1)

    def test_while_returning_goods_the_repository_delete_should_be_called_when_find(self):
        mocked_invoice = Mock(Invoice)
        mocked_invoice.items = []
        spy_repository = Mock(InvoiceRepository)
        spy_repository.find_by_number.return_value = mocked_invoice

        shop = Shop(spy_repository, Mock(WarehouseRepository))
        shop.returning_goods(mocked_invoice)

        spy_repository.delete.assert_called_once()

    def test_while_partial_returning_goods_the_repository_update_should_be_called_when_found(self):
        mocked_invoice = Mock(Invoice)
        mocked_invoice.items = []
        mocked_invoice.price = 0
        spy_repository = Mock(InvoiceRepository)
        spy_repository.find_by_number.return_value = mocked_invoice

        shop = Shop(spy_repository, Mock(WarehouseRepository))
        shop.partial_returning_goods(mocked_invoice, [])

        spy_repository.update.assert_called_once()

    def test_while_partial_returning_goods_return_product_should_be_called_with_data(self):
        mock_warehouse = Mock(WarehouseRepository)
        mock_warehouse.return_product.return_value = 0
        mocked_invoice = Mock(Invoice)
        mocked_invoice.items = []
        mocked_invoice.price = 0
        spy_repository = Mock(InvoiceRepository)
        spy_repository.find_by_number.return_value = mocked_invoice

        shop = Shop(spy_repository, mock_warehouse)
        shop.partial_returning_goods(
            mocked_invoice, [{"name": "cukierki", "amount": 1}])

        mock_warehouse.return_product.assert_called_once_with("cukierki", 1)
