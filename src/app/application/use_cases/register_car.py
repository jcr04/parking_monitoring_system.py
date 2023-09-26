from domain.repositories import ICarRepository
from domain.entities import Car

class RegisterCar:
    def __init__(self, car_repository: ICarRepository):
        self.car_repository = car_repository
    
    def execute(self, plate: str) -> None:
        car = Car(plate)
        self.car_repository.save(car)
