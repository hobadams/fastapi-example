from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.get("/api/python")
def hello_world():
    return {"message": "Hello Worldsssss"}


@app.post("/api/items/{param_name}")
async def create_item(param_name: str, item: Item):
    return {"param_name": param_name, "item": item.dict()}