import unittest

from classes.DTOs.AddressDTO import AddressDTO


class TestAddressDTO(unittest.TestCase):

    def test_address_dto_init(self) -> None:
        address_dto = AddressDTO("Street", 1, 2, "City")
        self.assertListEqual(["Street", 1, 2, "City"],
                             [address_dto.street, address_dto.building_nr, address_dto.local_nr,
                              address_dto.city])


if __name__ == "__main__":
    unittest.main()
