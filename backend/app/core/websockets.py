from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connection has been established")
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

@app.get("/")
async def get():
    return {"message": "Hello World"}