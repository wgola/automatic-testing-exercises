import unittest
from datetime import datetime

from classes.Owner import Owner


class OwnerTestCase(unittest.TestCase):

    def setUp(self):
        self.owner = Owner("Jan", "Kowalski", datetime(
            2001, 5, 17), "123456789", "Gdańsk ul. Wita Stwosza 40")

    def tearDown(self):
        del self.owner

    def test_person_correctly_initialized(self):
        self.assertMultiLineEqual("Jan", self.owner.name)
        self.assertMultiLineEqual("Kowalski", self.owner.surname)
        self.assertEqual(datetime(2001, 5, 17), self.owner.date_of_birth)
        self.assertMultiLineEqual("123456789", self.owner.phone)
        self.assertMultiLineEqual(
            "Gdańsk ul. Wita Stwosza 40", self.owner.address)

    def test_person_data_change_correctly(self):
        self.owner.name = "Marek"
        self.owner.surname = "Nowak"
        self.owner.date_of_birth = datetime(2002, 6, 18)
        self.owner.phone = "234567890"
        self.owner.address = "Gdańsk ul. Wita Stwosza 50"

        self.assertMultiLineEqual("Marek", self.owner.name)
        self.assertMultiLineEqual("Nowak", self.owner.surname)
        self.assertEqual(datetime(2002, 6, 18), self.owner.date_of_birth)
        self.assertMultiLineEqual("234567890", self.owner.phone)
        self.assertMultiLineEqual(
            "Gdańsk ul. Wita Stwosza 50", self.owner.address)


if __name__ == '__main__':
    unittest.main()
