import unittest
from classes.WorkersClasses.Address import Address
from classes.Exceptions import WorkerIDTakenException, EmptyStringArgumentException
from classes.WorkersClasses.PhysicalWorker import PhysicalWorker


class PhysicalWorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.address = Address("Street", 1, 2, "City")
        self.physical_worker = PhysicalWorker(
            1, "Name", "Surname", 20, 10, self.address, 60)

    def tearDown(self) -> None:
        del self.physical_worker
        del self.address

    def test_physical_worker_init(self) -> None:
        self.assertListEqual(
            [1, "Name", "Surname", 20, 10, self.address, 60],
            [self.physical_worker.worker_id,
             self.physical_worker.name,
             self.physical_worker.surname,
             self.physical_worker.age,
             self.physical_worker.experience,
             self.physical_worker.address,
             self.physical_worker.strength]
        )

    def test_worker_id_taken(self) -> None:
        with self.assertRaises(WorkerIDTakenException):
            PhysicalWorker(1, "Name2", "Surname2", 20, 10, self.address, 60)

    def test_wrong_name(self) -> None:
        with self.assertRaises(EmptyStringArgumentException):
            self.physical_worker.name = ""

    def test_wrong_experience(self) -> None:
        self.physical_worker.experience = -3
        self.assertNotEqual(-3, self.physical_worker.experience)

    def test_company_worth(self) -> None:
        self.physical_worker.experience = 10
        self.assertEqual(30, self.physical_worker.company_worth)

    def test_to_string(self) -> None:
        self.assertMultiLineEqual(
            "{}. {} {}: age: {}, experience: {}, address: {}, strength: {}, company worth: {}".format(
                self.physical_worker.worker_id,
                self.physical_worker.name,
                self.physical_worker.surname,
                self.physical_worker.age,
                self.physical_worker.experience,
                self.physical_worker.address,
                self.physical_worker.strength,
                self.physical_worker.company_worth),
            self.physical_worker.__str__())

    def test_dto(self) -> None:
        physical_worker_dto = self.physical_worker.dto()
        self.assertListEqual([self.physical_worker.worker_id, self.physical_worker.name, self.physical_worker.surname,
                              self.physical_worker.age, self.physical_worker.experience,
                              self.physical_worker.address.dto(), self.physical_worker.company_worth,
                              self.physical_worker.strength],
                             [physical_worker_dto.worker_id, physical_worker_dto.name, physical_worker_dto.surname,
                              physical_worker_dto.age, physical_worker_dto.experience, physical_worker_dto.address,
                              physical_worker_dto.company_worth, physical_worker_dto.strength])


if __name__ == "__main__":
    unittest.main()
