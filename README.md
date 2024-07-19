## 开发环境启动：
uvicorn app.main:app --reload --host 0.0.0.0 --port 8864
## 发送测试请求
### restful api
```
    curl -X GET "http://localhost:8864/api/v1/items/123"
    curl -X POST "http://localhost:8864/api/v1/items/" -H "Content-Type: application/json" -d '{"name": "Item1", "description": "This is item 1"}'
```
### rpc
```
    curl -X POST "http://localhost:8864/api/jsonrpc" -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "say_hello", "params":{"params": {"name": "John"}}, "id": 1}'
    curl -X POST "http://localhost:8864/api/jsonrpc" -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "create_item", "params":{"params": {"item": {"name": "Item1", "description": "This is item 1"}}}, "id": 1}'
```
### websocket
```
    import asyncio
    import websockets
    import json

    async def websocket_client():
        uri = "ws://localhost:8864/ws"
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"action": "join", "data": {"room": "room1"}}))
            response = await websocket.recv()
            print(response)

    asyncio.run(websocket_client())
```