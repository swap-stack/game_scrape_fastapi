from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import json
import os
from dotenv import load_dotenv

load_dotenv()

data_file_path = os.getenv('DATA_FILE')
output_file_path = os.getenv('OUTPUT_FILE')

app = FastAPI()


class GameItem(BaseModel):
    name: str
    id: str
    price: str


class GameItemList(BaseModel):
    data: List[GameItem]


@app.get("/items_prices")
async def get_all_game_items():
    data = None

    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    try:
        with open(data_file_path, 'r') as f:
            ids = f.read()
        if ids:
            game_ids = str(ids)
            cmd = f'scrapy crawl game -a game_ids={game_ids} -o output.json'
            subprocess.check_output(cmd)
            with open(output_file_path) as file:
                data = json.load(file)
    except:
        # TODO
        print('Error')
        # return appropriate response
    return {'message': data}


@app.get("/games", status_code=200)
async def view_item():
    try:
        with open(data_file_path, 'r') as f:
            ids = f.read()

        game_ids = str(ids)

        return {"message": game_ids}
    except:
        # TODO
        print('Error')
        # return appropriate response
        return {"message": "Error"}



@app.post("/add", status_code=201)
async def add_an_item(game_id):
    try:
        with open(data_file_path, "a") as f:
            f.write(f",{game_id}")
        return {"message": "OK"}
    except:
        # TODO
        print('Error')
        # return appropriate response
        return {"message": "Error"}


@app.delete("/delete", status_code=204)
async def delete_an_item(game_id):
    try:
        with open(data_file_path, "r") as f:
            ids = f.read()
            ids = ids.split(',')
            if game_id not in ids:
                return {"message": "Could not locate"}
            ids.remove(game_id)
        updated_ids = ','.join(ids)

        with open(data_file_path, "w") as f:
            f.write(updated_ids)
        return {"message": "OK"}

    except:
        # TODO
        print('Error')
        # return appropriate response
        return {"message": "Error"}
