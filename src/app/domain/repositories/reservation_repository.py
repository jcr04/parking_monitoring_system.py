# Em domain/repositories/reservation_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities import Reservation

class IReservationRepository(ABC):
    @abstractmethod
    def save(self, reservation: Reservation) -> None:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Reservation]:
        pass
