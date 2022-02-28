from fastapi import APIRouter, HTTPException
from models.car import cars
from config.db import conn
from schemas.car import Car, UpdateCar
from uuid import uuid4 as uuid

car = APIRouter()

@car.get('/', tags=['Home'])
def home():
    return {'message': 'Welcome to my API'}

@car.get('/cars', tags=['Get Cars'])
def get_cars():
    return conn.execute(cars.select()).fetchall()

@car.get('/cars/{id_car}', tags=['Get Car'])
def get_car(id_car: str):
    result = conn.execute(cars.select().where(cars.c.id == id_car)).first()
    if not (result == None):
        return result
    raise HTTPException(status_code=404, detail='Item not found')

@car.post('/cars', tags=['Add New Car'])
def add_car(newCar: Car):
    newCar.id = str(uuid())
    conn.execute(cars.insert().values(newCar.dict()))
    return conn.execute(cars.select().where(cars.c.id == newCar.id)).first()

@car.put('/cars/{id_car}', tags=['Update Car'])
def update_car(id_car: str, updateData: UpdateCar):
    result = conn.execute(cars.select().where(cars.c.id == id_car)).first()
    if not (result == None):
        conn.execute(cars.update().values(precio=updateData.precio).where(cars.c.id == id_car))
        return {'message': 'Car has been updated successfully'}
    raise HTTPException(status_code=404, detail='Item not found')

@car.delete('/cars/{id_car}', tags=['Delete car'])
def delete_car(id_car: str):
    result = conn.execute(cars.select().where(cars.c.id == id_car)).first()
    if not (result == None):
        conn.execute(cars.delete().where(cars.c.id == id_car))
        return {'message': 'Car has been deleted successfully'}
    raise HTTPException(status_code=404, detail='Item not found')