from datetime import datetime

class Car:
    def __init__(self, plate: str, model: str, color: str, entry_time: datetime):
        self.plate = plate
        self.model = model
        self.color = color
        self.entry_time = entry_time
