from dataclasses import dataclass

from classes.DTOs.AddressDTO import AddressDTO


@dataclass(frozen=True)
class WorkerDTO:
    worker_id: int
    name: str
    surname: str
    age: int
    experience: int
    address: AddressDTO
    company_worth: float
