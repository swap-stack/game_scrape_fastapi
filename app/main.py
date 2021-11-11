from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import json
import os

app = FastAPI()

class GameItem(BaseModel):
    name: str
    id: str
    price: str

class GameItemList(BaseModel):
    data: List[GameItem]

@app.get("/all_prices")
async def get_all_game_items():
    if os.path.exists("../data/output.json"):
        os.remove("../data/output.json")
    with open("../data/game_ids.csv", 'r') as f:
        ids = f.read()
    if ids:
        game_ids = str(ids)
        cmd = f'scrapy crawl game -a game_ids={game_ids} -o output.json'
        subprocess.check_output(cmd)
        data = None
        with open('../data/output.json') as file:
            data = json.load(file)
    return {'message': data}

@app.post("/add", status_code=201)
async def add_an_item(game_id):
    with open("../data/game_ids.csv", "a") as f:
        f.write(f",{game_id}")

    return {"message": "OK"}

@app.delete("/delete", status_code=204)
async def delete_an_item(game_id):
    with open("../data/game_ids.csv", "r") as f:
        ids = f.read()
        ids = ids.split(',')
        if game_id not in ids:
            return {"message": "Could not locate"}
        ids.remove(game_id)
    updated_ids = ','.join(ids)

    with open("../data/game_ids.csv", "w") as f:
        f.write(updated_ids)

    return {"message": "OK"}
