from dataclasses import dataclass


@dataclass(frozen=True)
class AddressDTO:
    street: str
    building_nr: int
    local_nr: int
    city: str
