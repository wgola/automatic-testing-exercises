class Owner:
    def __init__(self, name, surname, date_of_birth, phone, address) -> None:
        self.__name = name
        self.__surname = surname
        self.__date_of_birth = date_of_birth
        self.__phone = phone
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname) -> None:
        self.__surname = new_surname

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth) -> None:
        self.__date_of_birth = new_date_of_birth

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone) -> None:
        self.__phone = new_phone

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address) -> None:
        self.__address = new_address
