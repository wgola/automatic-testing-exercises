import unittest
from datetime import datetime
from classes.Bank import Bank
from classes.BankAccount import WrongDepositException, WrongWithdrawalException
from classes.Owner import Owner


class BankAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.owner1 = Owner("Jan", "Kowalski", datetime(
            2001, 5, 17), "123456789", "Gdańsk ul. Wita Stwosza 40")
        self.owner2 = Owner("Adam", "Nowak", datetime(
            2000, 6, 19), "012345678", "Gdańsk ul. Wita Stwosza 42")
        self.account_number1 = "1234567890123456"
        self.account_number2 = "0123456789012345"
        self.account1 = self.bank.add_account(
            self.owner1, self.account_number1)
        self.account2 = self.bank.add_account(
            self.owner2, self.account_number2)

    def tearDown(self):
        del self.bank
        del self.owner1
        del self.owner2
        del self.account_number1
        del self.account_number2
        del self.account1
        del self.account2

    def test_deposit(self):
        balance_before = self.account1.balance

        self.account1.deposit(100)

        self.assertEqual(balance_before + 100, self.account1.balance)

    def test_wrong_deposit_amount(self):
        with self.assertRaises(WrongDepositException):
            self.account1.deposit(-20)

    def test_withdrawal(self):
        self.account1.deposit(100)
        balance_before = self.account1.balance

        self.account1.withdrawal(50)

        self.assertEqual(balance_before - 50, self.account1.balance)

    def test_wrong_withdrawal_amount(self):
        self.account1.deposit(100)

        with self.assertRaises(WrongWithdrawalException):
            self.account1.withdrawal(150)

    def test_transfer(self):
        self.account1.deposit(100)
        account1_balance_before = self.account1.balance
        account2_balance_before = self.account2.balance

        self.account1.transfer("0123456789012345", 50)

        self.assertEqual(account1_balance_before - 50, self.account1.balance)
        self.assertEqual(account2_balance_before + 50, self.account2.balance)

    def test_get_all_history(self):
        self.account1.deposit(100)

        self.account1.transfer("0123456789012345", 50)
        self.account2.transfer("1234567890123456", 50)
        self.account1.withdrawal(100)

        history_account1 = self.account1.get_history()
        history_account2 = self.account2.get_history()

        self.assertEqual(len(history_account1), 4)
        self.assertEqual(len(history_account2), 2)

    def test_get_history_from_time_period(self):
        self.account1.deposit(100)

        self.account1.transfer("0123456789012345", 50)
        self.account2.transfer("1234567890123456", 50)
        self.account1.withdrawal(100)

        today = datetime.now()
        history_account1_from_month_before = self.account1.get_history_from_time_period(
            datetime(today.year, today.month - 1, 1), datetime(today.year, today.month - 1, 30))

        history_account2_from_current_day = self.account2.get_history_from_time_period(
            datetime(today.year, today.month, today.day), datetime(today.year, today.month, today.day + 1))

        self.assertEqual(len(history_account1_from_month_before), 0)
        self.assertEqual(len(history_account2_from_current_day), 2)


if __name__ == '__main__':
    unittest.main()
