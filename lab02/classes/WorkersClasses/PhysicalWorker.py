from classes.WorkersClasses.Address import Address
from classes.DTOs.PhysicalWorkerDTO import PhysicalWorkerDTO
from classes.Exceptions import WrongStrengthException
from classes.WorkersClasses.Worker import Worker


class PhysicalWorker(Worker):
    def __new__(cls, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address, strength: int):
        return super().__new__(cls, worker_id, name, surname, age, exp, address)

    def __init__(self, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                 strength: int) -> None:
        super().__init__(worker_id, name, surname, age, exp, address)
        self.strength = strength

    def __repr__(self) -> str:
        return "PhysicalWorker(worker_id={},name={},surname={},age={},exp={},Address={},strength={}".format(
            self.worker_id, self.name, self.surname, self.age, self.experience, self.address.__repr__(), self.strength)

    def __str__(self) -> str:
        return super().__str__() + ", strength: {}, company worth: {}".format(self.strength, self.company_worth)

    @property
    def strength(self) -> int:
        return self.__strength

    @strength.setter
    def strength(self, new_strength: int) -> None:
        if 1 <= new_strength <= 100:
            self.__strength = new_strength
        else:
            raise WrongStrengthException

    @property
    def company_worth(self) -> float:
        return self.experience * (self.strength / self.age)

    def dto(self) -> PhysicalWorkerDTO:
        return PhysicalWorkerDTO(self.worker_id, self.name, self.surname, self.age, self.experience, self.address.dto(),
                                 self.company_worth, self.strength)
