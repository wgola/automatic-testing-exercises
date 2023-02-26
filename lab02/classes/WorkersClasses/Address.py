from classes.DTOs.AddressDTO import AddressDTO
from classes.Exceptions import WrongNumberArgumentException, EmptyStringArgumentException


class Address:
    def __init__(self, street: str, building_nr: int, local_nr: int, city: str) -> None:
        self.street = street
        self.building_nr = building_nr
        self.local_nr = local_nr
        self.city = city

    def __repr__(self) -> str:
        return "Address(street={},building_nr={},local_nr={},city={})".format(self.street, self.building_nr,
                                                                              self.local_nr, self.city)

    def __str__(self) -> str:
        return "Street: {}, building number: {}, local number: {}, city: {}".format(self.street, self.building_nr,
                                                                                    self.local_nr, self.city)

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, new_street: str) -> None:
        if new_street == "":
            raise EmptyStringArgumentException
        else:
            self.__street = new_street

    @property
    def building_nr(self) -> int:
        return self.__building_nr

    @building_nr.setter
    def building_nr(self, new_building_nr: int) -> None:
        if new_building_nr > 0:
            self.__building_nr = new_building_nr
        else:
            raise WrongNumberArgumentException

    @property
    def local_nr(self) -> int:
        return self.__local_nr

    @local_nr.setter
    def local_nr(self, new_local_nr: int) -> None:
        if new_local_nr > 0:
            self.__local_nr = new_local_nr
        else:
            raise WrongNumberArgumentException

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, new_city: str) -> None:
        if new_city == "":
            raise EmptyStringArgumentException
        else:
            self.__city = new_city

    def dto(self) -> AddressDTO:
        return AddressDTO(self.street, self.building_nr, self.local_nr, self.city)
