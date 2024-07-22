from fastapi import WebSocket, APIRouter
from app.base.logger import get_module_logger
from app.core.config import config


logger = get_module_logger(__name__)

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
