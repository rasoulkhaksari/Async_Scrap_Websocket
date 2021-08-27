from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import asyncio
import os
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    modified_time = os.path.getatime("result.json")
    await websocket.accept()
    while True:
        os.system('scrapy crawl tradingviewspider --nolog')
        # print("WWW...")
        if modified_time != os.path.getatime("result.json"):
            modified_time = os.path.getatime("result.json")
            with open('result.json') as result:
                await websocket.send_json(json.load(result))

        # if result:
        #     print('AAA')
        #     await websocket.send_json(result)
        await asyncio.sleep(5)


