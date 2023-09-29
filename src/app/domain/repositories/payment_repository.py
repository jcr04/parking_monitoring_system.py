# Em domain/repositories/payment_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities import Payment

class IPaymentRepository(ABC):
    @abstractmethod
    def save(self, payment: Payment) -> None:
        pass
    
    @abstractmethod
    def get_by_reservation_id(self, reservation_id: str) -> Payment:
        pass
