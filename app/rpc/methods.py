from fastapi_jsonrpc import Entrypoint
from pydantic import BaseModel
from app.schemas.item import ItemCreate, Item

rpc_router = Entrypoint('/api/jsonrpc')

class SayHelloParams(BaseModel):
    name: str

class CreateItemParams(BaseModel):
    item: ItemCreate

@rpc_router.method()
async def say_hello(params: SayHelloParams) -> str:
    print(f".. rpc method -> say_hello")
    return f"Hello, {params.name}!"

@rpc_router.method()
async def create_item(params: CreateItemParams) -> Item:
    print(f".. rpc method -> create_item")
    item = params.item
    return Item(id=1, name=item.name, description=item.description)
