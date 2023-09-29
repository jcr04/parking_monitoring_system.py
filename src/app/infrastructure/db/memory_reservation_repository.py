# Em infrastructure/db/memory_reservation_repository.py
from ast import List
from domain.repositories import IReservationRepository
from domain.entities import Reservation

class MemoryReservationRepository(IReservationRepository):
    def __init__(self):
        self.reservations = []
    
    def save(self, reservation: Reservation) -> None:
        self.reservations.append(reservation)
    
    def get_all(self) -> List[Reservation]:
        return self.reservations
