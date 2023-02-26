import unittest

from classes.DTOs.AddressDTO import AddressDTO
from classes.DTOs.PhysicalWorkerDTO import PhysicalWorkerDTO


class TestPhysicalWorkerDTO(unittest.TestCase):
    def test_physical_worker_dto_init(self) -> None:
        address_dto = AddressDTO("Street", 1, 2, "City")
        physical_worker_dto = PhysicalWorkerDTO(
            1, "Name", "Surname", 20, 0, address_dto, 1, 1)
        self.assertListEqual([1, "Name", "Surname", 20, 0, address_dto, 1, 1],
                             [physical_worker_dto.worker_id, physical_worker_dto.name, physical_worker_dto.surname,
                              physical_worker_dto.age, physical_worker_dto.experience, physical_worker_dto.address,
                              physical_worker_dto.company_worth, physical_worker_dto.strength])


if __name__ == "__main__":
    unittest.main()
