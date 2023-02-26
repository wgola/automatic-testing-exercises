import unittest

from classes.WorkersClasses.Address import Address
from classes.WorkersClasses.Efficiency import Efficiency
from classes.Exceptions import WrongWorkerTypeException
from classes.Register import Register


class TestRegister(unittest.TestCase):
    def setUp(self) -> None:
        self.register = Register()
        self.address1 = Address("Street", 1, 2, "City")
        self.address2 = Address("Street", 1, 2, "City")
        self.address3 = Address("Street", 1, 2, "City")
        self.office_worker = {
            "worker_type": "OfficeWorker",
            "worker_id": 1,
            "name": "Name1",
            "surname": "Surname1",
            "age": 40,
            "exp": 2,
            "address": self.address1,
            "office_worker_id": 1,
            "iq": 100
        }
        self.physical_worker = {
            "worker_type": "PhysicalWorker",
            "worker_id": 2,
            "name": "Name2",
            "surname": "Surname2",
            "age": 30,
            "exp": 10,
            "address": self.address2,
            "strength": 100
        }
        self.trader = {
            "worker_type": "Trader",
            "worker_id": 3,
            "name": "Name3",
            "surname": "Surname3",
            "age": 20,
            "exp": 2,
            "address": self.address3,
            "efficiency": Efficiency.SREDNIA,
            "provision": 50
        }

    def tearDown(self) -> None:
        del self.address1
        del self.address2
        del self.address3
        del self.register
        del self.office_worker
        del self.physical_worker
        del self.trader

    def test_add_office_worker(self) -> None:
        office_worker = self.register.add_worker(
            "OfficeWorker", 1, "Name", "Surname", 30, 10, self.address1, office_worker_id=1, iq=80)
        self.assertIn(office_worker, self.register.get_all_workers())

    def test_add_physical_worker(self) -> None:
        physical_worker = self.register.add_worker(
            "PhysicalWorker", 1, "Name", "Surname", 30, 10, self.address1, strength=90)
        self.assertIn(physical_worker, self.register.get_all_workers())

    def test_add_trader(self) -> None:
        trader = self.register.add_worker("Trader", 1, "Name", "Surname", 30, 10, self.address1, efficiency=Efficiency.SREDNIA,
                                          provision=50)
        self.assertIn(trader, self.register.get_all_workers())

    def test_add_wrong_worker_type(self) -> None:
        with self.assertRaises(WrongWorkerTypeException):
            self.register.add_worker(
                "Worker", 1, "Name", "Surname", 30, 10, self.address1)

    def test_add_workers(self) -> None:
        added_workers = self.register.add_workers(
            self.office_worker, self.physical_worker, self.trader)
        self.assertListEqual(added_workers, self.register.get_all_workers())

    def test_delete_worker(self) -> None:
        worker = self.register.add_worker("OfficeWorker", 1, "Name", "Surname", 30, 10, self.address1,
                                          office_worker_id=1, iq=80)
        self.register.delete_worker(1)
        self.assertNotIn(worker, self.register.get_all_workers())

    def test_get_worker(self) -> None:
        worker = self.register.add_worker("OfficeWorker", 1, "Name", "Surname", 30, 10, self.address1,
                                          office_worker_id=1, iq=80)
        found_worker = self.register.get_worker(1)
        self.assertEqual(worker, found_worker)

    def test_sort_workers(self) -> None:
        workers = self.register.add_workers(
            self.office_worker, self.physical_worker, self.trader)
        sorted_workers = self.register.sort_workers(
            lambda worker: (-worker.experience, worker.age, worker.surname))
        self.assertListEqual(
            [workers[1], workers[2], workers[0]], sorted_workers)

    def test_filter_workers(self) -> None:
        workers = self.register.add_workers(
            self.office_worker, self.physical_worker, self.trader)
        filtered_workers = self.register.filter_workers(
            lambda worker: worker.experience < 10)
        self.assertListEqual([workers[0], workers[2]], filtered_workers)

    def test_get_workers_from_city(self) -> None:
        workers = self.register.add_workers(
            self.office_worker, self.physical_worker, self.trader)
        workers[1].address.city = "City2"
        workers_from_city = self.register.get_workers_from_city("City")
        self.assertListEqual([workers[0], workers[2]], workers_from_city)

    def test_get_all_workers(self) -> None:
        workers = self.register.add_workers(
            self.office_worker, self.physical_worker, self.trader)
        worker = self.register.add_worker("OfficeWorker", 4, "Name", "Surname", 30, 10, self.address1,
                                          office_worker_id=2, iq=80)
        all_workers = self.register.get_all_workers()
        self.assertListEqual([*workers, worker], all_workers)

    def test_get_all_workers_dtos(self) -> None:
        workers = self.register.add_workers(
            self.office_worker, self.physical_worker, self.trader)
        new_worker = self.register.add_worker("OfficeWorker", 4, "Name", "Surname", 30, 10, self.address1,
                                              office_worker_id=2, iq=80)
        workers_dtos = list(
            map(lambda worker: worker.dto(), [*workers, new_worker]))
        all_workers_dtos = self.register.get_all_workers_dtos()
        self.assertListEqual(workers_dtos, all_workers_dtos)


if __name__ == "__main__":
    unittest.main()
