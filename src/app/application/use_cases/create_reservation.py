import datetime
from domain.repositories import IReservationRepository
from domain.entities import Reservation

class CreateReservation:
    def __init__(self, reservation_repository: IReservationRepository):
        self.reservation_repository = reservation_repository
    
    def execute(self, car_plate: str, reserved_at: datetime, expires_at: datetime) -> None:
        reservation = Reservation(car_plate, reserved_at, expires_at)
        self.reservation_repository.save(reservation)
