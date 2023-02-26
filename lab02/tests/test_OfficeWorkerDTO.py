import unittest

from classes.DTOs.AddressDTO import AddressDTO
from classes.DTOs.OfficeWorkerDTO import OfficeWorkerDTO


class TestOfficeWorkerDTO(unittest.TestCase):
    def test_office_worker_dto_init(self) -> None:
        address_dto = AddressDTO("Street", 1, 2, "City")
        office_worker_dto = OfficeWorkerDTO(
            1, "Name", "Surname", 20, 0, address_dto, 1, 1, 80)
        self.assertListEqual([1, "Name", "Surname", 20, 0, address_dto, 1, 1, 80],
                             [office_worker_dto.worker_id, office_worker_dto.name, office_worker_dto.surname,
                              office_worker_dto.age, office_worker_dto.experience, office_worker_dto.address,
                              office_worker_dto.company_worth, office_worker_dto.office_worker_id,
                              office_worker_dto.iq])


if __name__ == "__main__":
    unittest.main()
