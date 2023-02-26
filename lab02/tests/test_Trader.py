import unittest

from classes.WorkersClasses.Address import Address
from classes.WorkersClasses.Efficiency import Efficiency
from classes.Exceptions import WorkerIDTakenException, EmptyStringArgumentException
from classes.WorkersClasses.Trader import Trader


class TestTrader(unittest.TestCase):
    def setUp(self) -> None:
        self.address = Address("Street", 1, 2, "City")
        self.trader = Trader(1, "Name", "Surname", 25, 5,
                             self.address, Efficiency.SREDNIA, 60)

    def tearDown(self) -> None:
        del self.trader
        del self.address

    def test_trader_init(self) -> None:
        self.assertListEqual([1, "Name", "Surname", 25, 5, self.address, Efficiency.SREDNIA, 60],
                             [self.trader.worker_id,
                              self.trader.name,
                              self.trader.surname,
                              self.trader.age,
                              self.trader.experience,
                              self.trader.address,
                              self.trader.efficiency,
                              self.trader.provision])

    def test_worker_id_taken(self) -> None:
        with self.assertRaises(WorkerIDTakenException):
            Trader(1, "Name2", "Surname2", 25, 5,
                   self.address, Efficiency.SREDNIA, 60)

    def test_wrong_surname(self) -> None:
        with self.assertRaises(EmptyStringArgumentException):
            self.trader.surname = ""

    def test_company_worth(self) -> None:
        self.assertEqual(5 * 90, self.trader.company_worth)

    def test_to_string(self) -> None:
        self.assertMultiLineEqual(
            "{}. {} {}: age: {}, experience: {}, address: {}, efficiency: {}, provision: {}%, company worth: {}".format(
                self.trader.worker_id, self.trader.name, self.trader.surname, self.trader.age, self.trader.experience,
                self.trader.address, self.trader.efficiency.name, self.trader.provision, self.trader.company_worth
            ), self.trader.__str__())

    def test_dto(self) -> None:
        trader_dto = self.trader.dto()
        self.assertListEqual(
            [self.trader.worker_id, self.trader.name, self.trader.surname, self.trader.age, self.trader.experience,
             self.trader.address.dto(), self.trader.efficiency, self.trader.provision],
            [trader_dto.worker_id, trader_dto.name, trader_dto.surname, trader_dto.age, trader_dto.experience,
             trader_dto.address, trader_dto.efficiency, trader_dto.provision]
        )


if __name__ == "__main__":
    unittest.main()
