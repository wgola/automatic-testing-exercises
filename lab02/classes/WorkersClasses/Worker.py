from abc import ABC, abstractmethod

from classes.WorkersClasses.Address import Address
from classes.Exceptions import EmptyStringArgumentException, WrongAgeException, WorkerIDTakenException
from classes.DTOs.WorkerDTO import WorkerDTO


class Worker(ABC):
    __workers_ids = []

    def __new__(cls, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address):
        if worker_id in Worker.__workers_ids:
            raise WorkerIDTakenException
        else:
            return object.__new__(cls)

    def __init__(self, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address) -> None:
        self.__worker_id = worker_id
        Worker.__workers_ids.append(worker_id)
        self.name = name
        self.surname = surname
        self.age = age
        self.experience = exp
        self.address = address

    def __del__(self) -> None:
        Worker.__workers_ids.remove(self.worker_id)

    def __repr__(self) -> str:
        return "Worker(worker_id={},name={},surname={},age={},exp={},Address={})".format(self.worker_id, self.name,
                                                                                         self.surname, self.age,
                                                                                         self.experience,
                                                                                         self.address.__repr__())

    def __str__(self) -> str:
        return "{0}. {1} {2}: age: {3}, experience: {4}, address: {5}".format(self.worker_id, self.name, self.surname,
                                                                              self.age,
                                                                              self.experience, self.address)

    @property
    def worker_id(self) -> int:
        return self.__worker_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if new_name == "":
            raise EmptyStringArgumentException
        else:
            self.__name = new_name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, new_surname: str) -> None:
        if new_surname == "":
            raise EmptyStringArgumentException
        else:
            self.__surname = new_surname

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age < 18:
            raise WrongAgeException
        else:
            self.__age = new_age

    @property
    def experience(self) -> int:
        return self.__experience

    @experience.setter
    def experience(self, new_exp: int) -> None:
        self.__experience = new_exp if new_exp >= 0 else 0

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, new_address: Address) -> None:
        self.__address = new_address

    @property
    @abstractmethod
    def company_worth(self) -> float:
        pass

    @abstractmethod
    def dto(self) -> WorkerDTO:
        pass
