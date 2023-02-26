from classes.WorkersClasses.Address import Address
from classes.DTOs.TraderDTO import TraderDTO
from classes.WorkersClasses.Efficiency import Efficiency
from classes.Exceptions import WrongNumberArgumentException
from classes.WorkersClasses.Worker import Worker


class Trader(Worker):
    def __new__(cls, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                efficiency: Efficiency,
                provision: int):
        return super().__new__(cls, worker_id, name, surname, age, exp, address)

    def __init__(self, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                 efficiency: Efficiency,
                 provision: int) -> None:
        super().__init__(worker_id, name, surname, age, exp, address)
        self.efficiency = efficiency
        self.provision = provision

    def __repr__(self) -> str:
        return "Trader(worker_id={},name={},surname={},age={},exp={},Address={},efficiency={},provision={})".format(
            self.worker_id, self.name, self.surname, self.age, self.experience, self.address, self.efficiency,
            self.provision
        )

    def __str__(self) -> str:
        return super().__str__() + ", efficiency: {}, provision: {}%, company worth: {}".format(self.efficiency.name,
                                                                                                self.provision,
                                                                                                self.company_worth)

    @property
    def efficiency(self) -> Efficiency:
        return self.__efficiency

    @efficiency.setter
    def efficiency(self, new_efficiency: Efficiency) -> None:
        self.__efficiency = new_efficiency

    @property
    def provision(self) -> int:
        return self.__provision

    @provision.setter
    def provision(self, new_provision: int) -> None:
        if 0 <= new_provision:
            self.__provision = new_provision
        else:
            raise WrongNumberArgumentException

    @property
    def company_worth(self) -> float:
        return self.experience * self.efficiency.value

    def dto(self) -> TraderDTO:
        return TraderDTO(self.worker_id, self.name, self.surname, self.age, self.experience, self.address.dto(),
                         self.company_worth, self.efficiency, self.provision)
