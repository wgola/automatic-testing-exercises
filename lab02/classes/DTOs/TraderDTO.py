from dataclasses import dataclass

from classes.DTOs.WorkerDTO import WorkerDTO
from classes.WorkersClasses.Efficiency import Efficiency


@dataclass(frozen=True)
class TraderDTO(WorkerDTO):
    efficiency: Efficiency
    provision: int
