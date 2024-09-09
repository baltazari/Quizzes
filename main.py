from Data.Db_Conection import engine
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from Routers import R_User

app = FastAPI()

app.include_router(R_User.router)
