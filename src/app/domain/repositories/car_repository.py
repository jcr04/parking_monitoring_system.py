from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities import car

class ICarRepository(ABC):
    
    @abstractmethod
    def save(self, car: car.Car) -> None:
        pass
    
    @abstractmethod
    def get_all(self) -> List[car.Car]:
        pass
    
    @abstractmethod
    def get_by_plate(self, plate: str) -> Optional[car.Car]:
        pass
    
    @abstractmethod
    def remove(self, car: car.Car) -> None:
        pass
