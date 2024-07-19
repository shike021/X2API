from fastapi import FastAPI
from fastapi_jsonrpc import API
import logging

from app.api.v1.api_v1 import router as api_router
from app.rpc.methods import rpc_router

from app.websocket.handlers import router as websocket_router
from app.db.base import Base
from app.db.session import engine
from app.base.logger import initialize_logger, create_logger

app = FastAPI()

logger = create_logger(
    log_dir="./logs",
    log_filename="app.log", # 从配置文件读取
    max_bytes=10485760,     # 10 MB
    backup_count=10,
    level=logging.DEBUG     # Set the logging level
)

# RESTful API
app.include_router(api_router, prefix="/api/v1")

# JSON-RPC
# 根据需要开启
app.add_route("/api/jsonrpc", rpc_router)

# WebSocket
# 根据需要开启
app.include_router(websocket_router)

@app.on_event("startup")
def on_startup():
    logger.info("Application started.")
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8864)
