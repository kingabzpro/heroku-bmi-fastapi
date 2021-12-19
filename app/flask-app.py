from fastapi import FastAPI
from app.custom_function import bmi
import uvicorn
import os


# Get environment variables
PORT = os.getenv('PORT')
HOST = os.environ.get('HOST')

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "Welcome"}


@app.get("/bmi")
def read_item(height: int, weight: int):
    return {"BMI": bmi(height, weight)}

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)