from dataclasses import dataclass

from classes.DTOs.WorkerDTO import WorkerDTO


@dataclass(frozen=True)
class PhysicalWorkerDTO(WorkerDTO):
    strength: int
