from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome(name):
    """Return a friendly welcome message"""
    return {"message":f"Welcome, {name} to the Car Sharing API"}
