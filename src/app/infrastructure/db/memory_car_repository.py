from ast import List
from domain.repositories import ICarRepository
from domain.entities import Car

class MemoryCarRepository(ICarRepository):
    def __init__(self):
        self.cars = []
    
    def save(self, car: Car) -> None:
        self.cars.append(car)
    
    def get_all(self) -> List[Car]:
        return self.cars
