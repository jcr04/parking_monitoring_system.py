# Em application/use_cases/process_payment.py
from datetime import datetime
from domain.repositories import IPaymentRepository, IReservationRepository
from domain.entities import Payment

class ProcessPayment:
    def __init__(self, payment_repository: IPaymentRepository, reservation_repository: IReservationRepository):
        self.payment_repository = payment_repository
        self.reservation_repository = reservation_repository
    
    def execute(self, reservation_id: str, amount: float) -> None:
        reservation = self.reservation_repository.get_by_id(reservation_id)
        if not reservation:
            raise ValueError("Reservation not found.")
        
        payment = Payment(reservation_id, amount, datetime.now())
        self.payment_repository.save(payment)
