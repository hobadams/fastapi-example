from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.get("/api/python")
def hello_world():
    return {"message": "Hello Worldsssss"}


@app.post("/api/items/")
async def create_item(item: Item):
    return item