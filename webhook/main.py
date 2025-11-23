from typing import Union
from fastapi import FastAPI, Request, Response, status
from os import getenv
import json

VERIFY_TOKEN = getenv("VERIFY_TOKEN")
app = FastAPI()

app.get("/")
def get_root(request: Request, response: Response):
    mode = request.query_params.get('hub.mode')
    challenge = request.query_params.get('hub.challenge')
    token = request.query_params.get('hub.verify_token')
    
    if mode == "subscribe" and token == VERIFY_TOKEN:
        print('WEBHOOK VERIFIED')
        response.status_code = status.HTTP_200_OK
        return challenge
    else:
        response.status_code = status.HTTP_403_FORBIDDEN

app.post("/")
def post_root(request: Request, response: Response):
    print(json.dumps(request.body()))
    response.status_code = status.HTTP_200_OK  
