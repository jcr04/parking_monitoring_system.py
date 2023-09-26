from flask import Flask, request
from application.use_cases import RegisterCar
from infrastructure.db import MemoryCarRepository

app = Flask(__name__)
car_repository = MemoryCarRepository()
register_car_use_case = RegisterCar(car_repository)

@app.route('/cars', methods=['POST'])
def register_car():
    data = request.json
    plate = data['plate']
    register_car_use_case.execute(plate)
    return {'status': 'success'}, 201
