from fastapi import FastAPI
import requests


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/exp_date/{hashed_id}")
async def get_exp_date(hashed_id: str):
    url = "http://193.168.147.19:8080/api/v2/tables/mrhmckd3wail7m7/records"
    params = {
        "viewId": "vwc0b9bld9wt63eq",
        "where": f"(hashed_id,eq,{hashed_id})",
        "limit": 25,
        "shuffle": 0,
        "offset": 0
    }
    headers = {
        "accept": "application/json",
        "xc-token": "ftUY9BEfapo6uF5U8iR4PapxJ58ITtNCyyJm12hm"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['list'] != []:
            return data['list'][0]['expiration_date']
        else:
            return "2025-08-30"
    else:
        print(f"Request failed with status code {response.status_code}")

