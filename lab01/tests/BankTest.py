import unittest
from datetime import datetime
from classes.Bank import Bank, WrongAccountNumberLengthException, AccountAlreadyExistingException, \
    NoAccountInBankException
from classes.Owner import Owner


class BankTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.owner = Owner("Jan", "Kowalski", datetime(
            2001, 5, 17), "123456789", "Gdańsk ul. Wita Stwosza 40")

    def tearDown(self):
        del self.bank
        del self.owner

    def test_add_bank_account(self):
        account_number = "1234567890123456"

        account = self.bank.add_account(self.owner, account_number)

        self.assertIn(account, self.bank.accounts)

    def test_add_existing_bank_account(self):
        account_number = "1234567890123456"
        self.bank.add_account(self.owner, account_number)

        with self.assertRaises(AccountAlreadyExistingException):
            self.bank.add_account(self.owner, account_number)

    def test_wrong_account_number_length(self):
        account_number = "123456789012345"

        with self.assertRaises(WrongAccountNumberLengthException):
            self.bank.add_account(self.owner, account_number)

    def test_remove_bank_account(self):
        account_number = "1234567890123456"
        account = self.bank.add_account(self.owner, account_number)

        self.bank.remove_account(account_number)

        self.assertNotIn(account, self.bank.accounts)

    def test_remove_non_existing_bank_account(self):
        with self.assertRaises(NoAccountInBankException):
            self.bank.remove_account("1234567890123456")

    def test_find_bank_account(self):
        account_number = "1234567890123456"
        account = self.bank.add_account(self.owner, account_number)

        self.assertEqual(account, self.bank.find_account(account_number))

    def test_find_no_existing_bank_account(self):
        account_number = "1234567890123456"
        self.bank.add_account(self.owner, account_number)

        with self.assertRaises(NoAccountInBankException):
            self.bank.find_account("1234567890123457")


if __name__ == '__main__':
    unittest.main()
