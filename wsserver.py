#!/usr/bin/env python

import asyncio
import websockets

clients = set()

@asyncio.coroutine
def hello(websocket, path):
    clients.add(websocket)
    while True:
        data = yield from websocket.recv()
        #yield from websocket.send(data)
        for ws in clients:
            if ws.open == False:
                clients.remove(ws)
            else:
                yield from ws.send(str(data))

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
