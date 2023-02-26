from datetime import datetime
import unittest

from classes.Owner import Owner
from classes.TransactionHistory import TransactionHistory, WrongTimePeriodException


class TransactionHistoryTestCase(unittest.TestCase):

    def setUp(self):
        self.history = TransactionHistory()
        self.owner1 = Owner("Jan", "Kowalski", datetime(
            2001, 5, 17), "123456789", "Gdańsk ul. Wita Stwosza 40")
        self.owner2 = Owner("Adam", "Nowak", datetime(
            2000, 6, 19), "012345678", "Gdańsk ul. Wita Stwosza 42")

    def tearDown(self):
        del self.history
        del self.owner1
        del self.owner2

    def test_add_entry_to_history(self):
        entry = self.history.add(
            "transfer", self.owner1, self.owner2, 20.00, 30.00, datetime.now())

        self.assertIn(entry, self.history.history)

    def test_get_entry_from_time_period(self):
        time1 = datetime(2022, 10, 18)
        self.history.add("transfer", self.owner1,
                         self.owner2, 20.0, 30.0, time1)
        time2 = datetime(2022, 11, 20)
        self.history.add("transfer", self.owner1,
                         self.owner2, 20.0, 10.0, time2)

        all_entries = self.history.get_history_from_time_period(
            datetime(2022, 10, 10), datetime(2022, 11, 30))
        october_entries = self.history.get_history_from_time_period(
            datetime(2022, 10, 1), datetime(2022, 10, 31))
        december_entries = self.history.get_history_from_time_period(
            datetime(2022, 12, 1), datetime(2022, 12, 31))

        self.assertEqual(len(all_entries), 2)
        self.assertEqual(len(october_entries), 1)
        self.assertEqual(len(december_entries), 0)

    def test_get_entry_from_wrong_time_period(self):
        time1 = datetime(2022, 10, 18)
        self.history.add("transfer", self.owner1,
                         self.owner2, 20.0, 30.0, time1)

        with self.assertRaises(WrongTimePeriodException):
            self.history.get_history_from_time_period(
                datetime(2022, 10, 31), datetime(2022, 10, 1))


if __name__ == "__main__":
    unittest.main()
