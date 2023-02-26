import unittest

from classes.WorkersClasses.Address import Address
from classes.Exceptions import WrongIQException, WrongAgeException, OfficeWorkerIDTakenException, WorkerIDTakenException
from classes.WorkersClasses.OfficeWorker import OfficeWorker


class OfficeWorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.address = Address("Street", 1, 2, "City")
        self.office_worker = OfficeWorker(
            1, "Name", "Surname", 25, 5, self.address, 1, 80)

    def tearDown(self) -> None:
        del self.office_worker
        del self.address

    def test_office_worker_init(self) -> None:
        self.assertListEqual(
            [1, "Name", "Surname", 25, 5, 1, 80],
            [self.office_worker.worker_id,
             self.office_worker.name,
             self.office_worker.surname,
             self.office_worker.age,
             self.office_worker.experience,
             self.office_worker.office_worker_id,
             self.office_worker.iq]
        )

    def test_worker_id_taken(self) -> None:
        with self.assertRaises(WorkerIDTakenException):
            OfficeWorker(1, "Name1", "Surname1", 25, 5, self.address, 2, 80)

    def test_office_worker_id_taken(self) -> None:
        with self.assertRaises(OfficeWorkerIDTakenException):
            OfficeWorker(2, "Name1", "Surname1", 25, 5, self.address, 1, 80)

    def test_wrong_age(self) -> None:
        with self.assertRaises(WrongAgeException):
            self.office_worker.age = 3

    def test_wrong_iq(self) -> None:
        with self.assertRaises(WrongIQException):
            self.office_worker.iq = 50

    def test_company_worth(self) -> None:
        self.assertEqual(5 * 80, self.office_worker.company_worth)

    def test_to_string(self) -> None:
        self.assertMultiLineEqual(
            "{}. {} {}: age: {}, experience: {}, address: {}, office worker id: {}, iq: {}, company worth: {}".format(
                self.office_worker.worker_id, self.office_worker.name, self.office_worker.surname,
                self.office_worker.age, self.office_worker.experience, self.office_worker.address,
                self.office_worker.office_worker_id,
                self.office_worker.iq, self.office_worker.company_worth), self.office_worker.__str__())

    def test_dto(self) -> None:
        office_worker_dto = self.office_worker.dto()
        self.assertListEqual(
            [self.office_worker.worker_id, self.office_worker.name, self.office_worker.surname, self.office_worker.age,
             self.office_worker.experience, self.office_worker.address.dto(
             ), self.office_worker.company_worth,
             self.office_worker.office_worker_id,
             self.office_worker.iq],
            [office_worker_dto.worker_id, office_worker_dto.name, office_worker_dto.surname, office_worker_dto.age,
             office_worker_dto.experience, office_worker_dto.address, office_worker_dto.company_worth,
             office_worker_dto.office_worker_id,
             office_worker_dto.iq])


if __name__ == "__main__":
    unittest.main()
