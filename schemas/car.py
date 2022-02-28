from pydantic import BaseModel
from typing import Optional


class Car(BaseModel):
    id: Optional[str]
    marca: str
    modelo: str
    precio: int

class UpdateCar(BaseModel):
    precio: int