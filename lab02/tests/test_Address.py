import unittest

from classes.WorkersClasses.Address import Address
from classes.Exceptions import EmptyStringArgumentException, WrongNumberArgumentException


class TestAddress(unittest.TestCase):
    def setUp(self) -> None:
        self.address = Address("Street", 6, 5, "London")

    def tearDown(self) -> None:
        del self.address

    def test_address_initialization(self) -> None:
        self.assertMultiLineEqual("Street", self.address.street)
        self.assertEqual(6, self.address.building_nr)
        self.assertEqual(5, self.address.local_nr)
        self.assertMultiLineEqual("London", self.address.city)

    def test_setting_wrong_street(self) -> None:
        with self.assertRaises(EmptyStringArgumentException):
            self.address.street = ""

    def test_setting_wrong_building_number(self) -> None:
        with self.assertRaises(WrongNumberArgumentException):
            self.address.building_nr = -10

    def test_setting_wrong_local_number(self) -> None:
        with self.assertRaises(WrongNumberArgumentException):
            self.address.local_nr = -2

    def test_setting_wrong_city(self) -> None:
        with self.assertRaises(EmptyStringArgumentException):
            self.address.city = ""

    def test_dto(self) -> None:
        address_dto = self.address.dto()
        self.assertListEqual([self.address.street, self.address.building_nr, self.address.local_nr, self.address.city],
                             [address_dto.street, address_dto.building_nr, address_dto.local_nr, address_dto.city])


if __name__ == "__main__":
    unittest.main()
