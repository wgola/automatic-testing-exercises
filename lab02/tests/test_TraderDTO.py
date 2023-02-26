import unittest

from classes.DTOs.AddressDTO import AddressDTO
from classes.DTOs.TraderDTO import TraderDTO
from classes.WorkersClasses.Efficiency import Efficiency


class TestTraderDTO(unittest.TestCase):
    def test_trader_dto_init(self) -> None:
        address_dto = AddressDTO("Street", 1, 2, "City")
        trader_dto = TraderDTO(1, "Name", "Surname", 20,
                               0, address_dto, 1, Efficiency.WYSOKA, 50)
        self.assertListEqual([1, "Name", "Surname", 20, 0, address_dto, 1, Efficiency.WYSOKA, 50],
                             [trader_dto.worker_id, trader_dto.name, trader_dto.surname, trader_dto.age,
                              trader_dto.experience, trader_dto.address, trader_dto.company_worth,
                              trader_dto.efficiency, trader_dto.provision])


if __name__ == "__main__":
    unittest.main()
