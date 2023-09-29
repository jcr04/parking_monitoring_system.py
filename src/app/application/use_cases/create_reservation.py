import datetime
from domain.repositories import IReservationRepository
from domain.entities import Reservation

class CreateReservation:
    def __init__(self, reservation_repository: IReservationRepository):
        self.reservation_repository = reservation_repository
    
    def execute(self, car_plate: str, reserved_at: datetime, expires_at: datetime) -> None:
        existing_reservation = [r for r in self.reservation_repository.get_all() if r.car_plate == car_plate and r.expires_at > datetime.now()]
        if existing_reservation:
            raise ValueError(f"A reservation for car with plate {car_plate} already exists.")
        
        reservation = Reservation(car_plate, reserved_at, expires_at)
        self.reservation_repository.save(reservation)
