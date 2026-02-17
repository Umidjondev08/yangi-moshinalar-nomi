from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Addcars(BaseModel):
    nomi:str
    modeli:int
    narxi:int | float
    rasmi:str
cars = [
    {
        "nomi": "Chevrolet Spark",
        "modeli": 2020,
        "narxi": "7000 - 9000 USD",
        "rasmi": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Chevrolet_Spark_2020.jpg"
    },
    {
        "nomi": "Daewoo Matiz",
        "modeli": 2010,
        "narxi": "3000 - 4500 USD",
        "rasmi": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Daewoo_Matiz_front.jpg"
    },
    {
        "nomi": "Chevrolet Nexia",
        "modeli": 2014,
        "narxi": "6000 - 8000 USD",
        "rasmi": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Chevrolet_Nexia_2.jpg"
    },
    {
        "nomi": "Lada Granta",
        "modeli": 2019,
        "narxi": "7500 - 9500 USD",
        "rasmi": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Lada_Granta_sedan.jpg"
    },
    {
        "nomi": "Hyundai i10",
        "modeli": 2018,
        "narxi": "8000 - 10000 USD",
        "rasmi": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Hyundai_i10_2018.jpg"
    }
]

@app.get("/api")
def takeUser():
    return cars
@app.post("/api/add")
def addcar(carsAdd:Addcars):
    cars.append(Addcars.dict())
    return f"{cars}Q'shildi"
@app.put("/api-pan/{cars}")
def updata(cars:int,updateUser:Addcars):
    for u in cars:
        if u ["id"] == cars:
           u ["id"] = updateUser.id
           u ["nomi"] = updateUser.nomi
           u ["modeli"] = updateUser.modeli
           u ["narxi"] = updateUser.narxi
           u ["rasm"] = updateUser.rasmi
    return F"{cars.cars} yangilandi"