from fastapi import FastAPI, HTTPException
import uvicorn
from schemas import load_db

app = FastAPI()
db = load_db()

@app.get("/")
async def welcome(name):
    """Return a friendly welcome message"""
    return {"message":f"Welcome, {name} to the Car Sharing API"}


@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None):
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors >= doors]
    return result


@app.get("/api/cars/{id}")
def car_by_id(id: int):
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"Car with id {id} not found")


if __name__ == "__main__":
    uvicorn.run("carsharing:app", host="127.0.0.1", port=8000, reload=True)