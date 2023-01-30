#!/usr/bin/env python

import asyncio
import json
import websockets

Users_ws = set()

VALUE = 0

def users_message():
    return json.dumps({"type": "users", "count": len(Users_ws)})

def value_message():
    return json.dumps({"type": "value", "value": VALUE})

async def counter(websocket):
    print(type(websocket))
    global Users_ws, VALUE
    try:
        # Register user
        Users_ws.add(websocket)
        print("Users_ws : ", Users_ws)
        websockets.broadcast(Users_ws, users_message())
        # Send current state to the newly joined user
        await websocket.send(value_message())
        # Manage operation 
        async for message in websocket:
            event = json.loads(message)
            if event["action"] == "minus":
                VALUE -= 1
                websockets.broadcast(Users_ws, value_message())
            elif event["action"] == "plus":
                VALUE += 1
                websockets.broadcast(Users_ws, value_message())
            else:
                print("unsupported event")
    finally:
        # Unregister user
        Users_ws.remove(websocket)
        websockets.broadcast(Users_ws, users_message())
        print("Users_ws : ", Users_ws)

async def main():
    print("Starting up Server @ 6789...")
    async with websockets.serve(counter, "localhost", 6789):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
