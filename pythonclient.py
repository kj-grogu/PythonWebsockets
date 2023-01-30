import asyncio
from websockets import connect
import json
import random

async def interact(uri):
    async with connect(uri) as websocket:
        while True:
            msg = json.dumps({ "action": "minus" })
            await websocket.send(msg)
            resp = await websocket.recv()
            print(resp)
            await asyncio.sleep(random.random() * 8)


asyncio.run(interact("ws://localhost:6789"))