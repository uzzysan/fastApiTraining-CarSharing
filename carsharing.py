import uvicorn
from fastapi import FastAPI, HTTPException
from schemas import load_db, CarInput, CarOutput, save_db

app = FastAPI()
db = load_db()

@app.get("/")
async def welcome(name):
    """Return a friendly welcome message"""
    return {"message":f"Welcome, {name} to the Car Sharing API"}


@app.get("/api/cars/")
def get_cars(size: str|None = None, doors: int|None = None) -> list[CarOutput]:
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors >= doors]
    return result


@app.get("/api/cars/{id}")
def car_by_id(id: int) -> CarOutput:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"Car with id={id} not found")


@app.post("/api/cars/")
def add_car(car: CarInput) -> CarOutput:
    new_car = CarOutput(
        id=len(db) + 1, 
        size=car.size, 
        fuel=car.fuel, 
        doors=car.doors, 
        transmission=car.transmission)
    db.append(new_car)
    save_db(db)
    return new_car



if __name__ == "__main__":
    uvicorn.run("carsharing:app", host="127.0.0.1", port=8000, reload=True)