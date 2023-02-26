from datetime import datetime
import unittest

from classes.Owner import Owner
from classes.TransactionEntry import TransactionEntry


class TransactionEntryTestCase(unittest.TestCase):
    def setUp(self):
        self.owner1 = Owner("Jan", "Kowalski", datetime(
            2001, 5, 17), "123456789", "Gdańsk ul. Wita Stwosza 40")
        self.owner2 = Owner("Adam", "Nowak", datetime(
            2000, 6, 19), "012345678", "Gdańsk ul. Wita Stwosza 42")
        self.time = datetime.now()
        self.entry = TransactionEntry(
            "transfer", self.owner1, self.owner2, 20.0, 30.0, self.time)

    def tearDown(self):
        del self.owner1
        del self.owner2
        del self.time

    def test_transaction_entry_correctly_initialized(self):
        self.assertMultiLineEqual(self.entry.transaction_type, "transfer")
        self.assertEqual(self.entry.sender, self.owner1)
        self.assertEqual(self.entry.getter, self.owner2)
        self.assertEqual(self.entry.amount, 20.0)
        self.assertEqual(self.entry.balance_after, 30.0)
        self.assertEqual(self.entry.date, self.time)

    def test_transaction_entry_correct_info(self):
        self.assertMultiLineEqual(self.entry.get_entry_info(), "Type: transfer | From: Jan Kowalski | To: Adam Nowak | "
                                                               "Amount: 20.0 | Balance after: 30.0 | Date: {0}".format(
            self.time))


if __name__ == "__main__":
    unittest.main()
