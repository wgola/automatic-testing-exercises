from typing import List

from classes.WorkersClasses.Address import Address
from classes.DTOs.WorkerDTO import WorkerDTO
from classes.WorkersClasses.Efficiency import Efficiency
from classes.Exceptions import WrongWorkerIDException, WrongDataException, WrongWorkerTypeException
from classes.WorkersClasses.OfficeWorker import OfficeWorker
from classes.WorkersClasses.PhysicalWorker import PhysicalWorker
from classes.WorkersClasses.Trader import Trader
from classes.WorkersClasses.Worker import Worker


class Register:
    def __init__(self):
        self.__workers = {}

    @property
    def workers_amount(self) -> int:
        return len(self.__workers)

    def add_worker(self, worker_type: str, worker_id: int, name: str, surname: str, age: int, exp: int,
                   address: Address,
                   office_worker_id: int = None, iq: int = None, strength: int = None, efficiency: Efficiency = None,
                   provision: int = None) -> Worker:
        if worker_type == "OfficeWorker":
            return self.__add_office_worker(worker_id, name, surname, age, exp, address, office_worker_id, iq)
        elif worker_type == "PhysicalWorker":
            return self.__add_physical_worker(worker_id, name, surname, age, exp, address, strength)
        elif worker_type == "Trader":
            return self.__add_trader(worker_id, name, surname, age, exp, address, efficiency, provision)
        else:
            raise WrongWorkerTypeException

    def __add_office_worker(self, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                            office_worker_id: int, iq: int) -> OfficeWorker:
        if office_worker_id is None or iq is None:
            raise WrongDataException
        else:
            self.__workers[worker_id] = OfficeWorker(
                worker_id, name, surname, age, exp, address, office_worker_id, iq)
            return self.__workers[worker_id]

    def __add_physical_worker(self, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                              strength: int) -> PhysicalWorker:
        if strength is None:
            raise WrongDataException
        else:
            self.__workers[worker_id] = PhysicalWorker(
                worker_id, name, surname, age, exp, address, strength)
            return self.__workers[worker_id]

    def __add_trader(self, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                     efficiency: Efficiency,
                     provision: int) -> Trader:
        if efficiency is None or provision is None:
            raise WrongDataException
        else:
            self.__workers[worker_id] = Trader(
                worker_id, name, surname, age, exp, address, efficiency, provision)
            return self.__workers[worker_id]

    def add_workers(self, *workers_dictionaries) -> List[Worker]:
        result = []
        for worker in workers_dictionaries:
            result.append(self.add_worker(worker.get("worker_type"), worker.get("worker_id"), worker.get("name"),
                                          worker.get("surname"), worker.get(
                                              "age"), worker.get("exp"),
                                          worker.get("address"), worker.get(
                                              "office_worker_id"), worker.get("iq"),
                                          worker.get("strength"), worker.get("efficiency"), worker.get("provision")))
        return result

    def delete_worker(self, worker_id: int) -> None:
        if worker_id not in self.__workers.keys():
            raise WrongWorkerIDException
        else:
            del self.__workers[worker_id]

    def get_worker(self, worker_id: int) -> Worker:
        if worker_id not in self.__workers.keys():
            raise WrongWorkerIDException
        else:
            return self.__workers[worker_id]

    def sort_workers(self, sorting_function) -> List[Worker]:
        return list(sorted(self.__workers.values(), key=sorting_function))

    def filter_workers(self, filter_function) -> List[Worker]:
        return list(filter(filter_function, self.__workers.values()))

    def get_workers_from_city(self, city: str) -> List[Worker]:
        return self.filter_workers(lambda worker: worker.address.city == city)

    def get_all_workers(self) -> List[Worker]:
        return list(self.__workers.values())

    def get_all_workers_dtos(self) -> List[WorkerDTO]:
        return list(map(lambda worker: worker.dto(), self.__workers.values()))
