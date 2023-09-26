from datetime import datetime

class Reservation:
    def __init__(self, car_plate: str, reserved_at: datetime, expires_at: datetime):
        self.car_plate = car_plate
        self.reserved_at = reserved_at
        self.expires_at = expires_at
