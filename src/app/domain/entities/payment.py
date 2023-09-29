# Em domain/entities/payment.py
from datetime import datetime


class Payment:
    def __init__(self, reservation_id: str, amount: float, paid_at: datetime):
        self.reservation_id = reservation_id
        self.amount = amount
        self.paid_at = paid_at
