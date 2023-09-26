from abc import ABC, abstractmethod
from typing import List
from domain.entities import car

class ICarRepository(ABC):
    @abstractmethod
    def save(self, car: car.Car) -> None:
        pass
    
    @abstractmethod
    def get_all(self) -> List[car.Car]:
        pass
