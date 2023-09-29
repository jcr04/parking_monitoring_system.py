from datetime import datetime
from domain.repositories import ICarRepository
from domain.entities import Car

class RegisterCar:
    def __init__(self, car_repository: ICarRepository):
        self.car_repository = car_repository
    
    def execute(self, plate: str, model: str, color: str) -> None:
        existing_car = self.car_repository.get_by_plate(plate)
        if existing_car:
            raise ValueError(f"A car with plate {plate} is already registered.")
        
        car = Car(plate, model, color, datetime.now())
        self.car_repository.save(car)
