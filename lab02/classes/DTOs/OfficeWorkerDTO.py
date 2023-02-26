from dataclasses import dataclass

from classes.DTOs.WorkerDTO import WorkerDTO


@dataclass(frozen=True)
class OfficeWorkerDTO(WorkerDTO):
    office_worker_id: int
    iq: int
