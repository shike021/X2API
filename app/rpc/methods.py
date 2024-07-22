from fastapi_jsonrpc import Entrypoint
from pydantic import BaseModel
from app.schemas.item import ItemCreate, Item
from app.base.logger import get_module_logger
from app.core.config import config

logger = get_module_logger(__name__)

rpc_router = Entrypoint('/api/jsonrpc')

class SayHelloParams(BaseModel):
    name: str

class CreateItemParams(BaseModel):
    item: ItemCreate

@rpc_router.method()
async def say_hello(params: SayHelloParams) -> str:
    logger.info(f".. rpc method -> say_hello")
    return f"Hello, {params.name}!"

@rpc_router.method()
async def create_item(params: CreateItemParams) -> Item:
    logger.info(f".. rpc method -> create_item")
    item = params.item
    return Item(id=1, name=item.name, description=item.description)
