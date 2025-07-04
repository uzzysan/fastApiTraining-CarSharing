import json
from pydantic import BaseModel

class CarInput(BaseModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"
    
class CarOutput(CarInput):
    id: int

def load_db() -> list[CarOutput]:
    """Load the database from the JSON file"""
    with open("cars.json", "r") as f:
        return [CarOutput.model_validate(car) for car in json.load(f)]
    
def save_db(cars: list[CarOutput]):
    """Save the database to the JSON file"""
    with open("cars.json", "w") as f:
        json.dump([car.model_dump() for car in cars], f, indent=4)