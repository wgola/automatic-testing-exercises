from classes.WorkersClasses.Address import Address
from classes.Exceptions import WrongIQException
from classes.DTOs.OfficeWorkerDTO import OfficeWorkerDTO
from classes.WorkersClasses.Worker import Worker
from classes.Exceptions import OfficeWorkerIDTakenException


class OfficeWorker(Worker):
    __office_workers_ids = []

    def __new__(cls, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                office_worker_id: int, iq: int):
        if office_worker_id in OfficeWorker.__office_workers_ids:
            raise OfficeWorkerIDTakenException
        else:
            return super().__new__(cls, worker_id, name, surname, age, exp, address)

    def __init__(self, worker_id: int, name: str, surname: str, age: int, exp: int, address: Address,
                 office_worker_id: int, iq: int) -> None:
        super().__init__(worker_id, name, surname, age, exp, address)
        self.__office_worker_id = office_worker_id
        OfficeWorker.__office_workers_ids.append(office_worker_id)
        self.iq = iq

    def __del__(self) -> None:
        super().__del__()
        OfficeWorker.__office_workers_ids.remove(self.office_worker_id)

    def __repr__(self) -> str:
        return "OfficeWorker(worker_id={},name={},surname={},age={},exp={},Address={},office_worker_id={},iq={})" \
            .format(self.worker_id, self.name, self.surname, self.age, self.experience, self.address.__repr__(),
                    self.office_worker_id, self.iq)

    def __str__(self) -> str:
        return super().__str__() + ", office worker id: {0}, iq: {1}, company worth: {2}".format(self.office_worker_id,
                                                                                                 self.iq,
                                                                                                 self.company_worth)

    @property
    def office_worker_id(self) -> int:
        return self.__office_worker_id

    @property
    def iq(self) -> int:
        return self.__iq

    @iq.setter
    def iq(self, new_iq) -> None:
        if 70 <= new_iq <= 150:
            self.__iq = new_iq
        else:
            raise WrongIQException

    @property
    def company_worth(self) -> float:
        return self.experience * self.iq

    def dto(self) -> OfficeWorkerDTO:
        return OfficeWorkerDTO(self.worker_id, self.name, self.surname, self.age, self.experience, self.address.dto(),
                               self.company_worth,
                               self.office_worker_id, self.iq)
