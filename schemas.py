from pydantic import BaseModel

class Car(BaseModel):
    id: int
    size: str
    fuel: str
    doors: int
    transmission: str
