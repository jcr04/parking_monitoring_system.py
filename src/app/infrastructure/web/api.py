from datetime import datetime
from flask import Flask, request
from application.use_cases import RegisterCar
from infrastructure.db import MemoryCarRepository
from application.use_cases import CreateReservation
from infrastructure.db import MemoryCarRepository, MemoryReservationRepository


app = Flask(__name__)
car_repository = MemoryCarRepository()
register_car_use_case = RegisterCar(car_repository)

reservation_repository = MemoryReservationRepository()
create_reservation_use_case = CreateReservation(reservation_repository)


@app.route('/cars', methods=['POST'])
def register_car():
    data = request.json
    plate = data['plate']
    register_car_use_case.execute(plate)
    return {'status': 'success'}, 201

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    car_plate = data['car_plate']
    reserved_at = datetime.strptime(data['reserved_at'], '%Y-%m-%dT%H:%M:%S')
    expires_at = datetime.strptime(data['expires_at'], '%Y-%m-%dT%H:%M:%S')
    create_reservation_use_case.execute(car_plate, reserved_at, expires_at)
    return {'status': 'success'}, 201