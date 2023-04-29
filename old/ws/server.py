import ast
import asyncio
import websockets
from websockets.server import serve


CLIENTS = set()
MESSAGES = []


async def send(websocket, message):
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        pass


def broadcast(message):
    print("Broadcast>")
    print("     " + message)
    for websocket in CLIENTS:
        asyncio.create_task(send(websocket, message))


async def broadcast_messages():
    print("<Broadcast_Message>")
    while True:
        await asyncio.sleep(1)
        for message in MESSAGES:
            await broadcast(message)


async def handler(websocket):
    queue = asyncio.Queue()
    replay_task = asyncio.create_task(relay(queue, websocket))
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            print('Incoming message: ')
            print(message)
            result = ast.literal_eval(message)
            print(result['data'])
            broadcast()
            pass
    finally:
        CLIENTS.remove(websocket)
        print("Websocket client removed from pool")


async def echo(websocket):

    async for message in websocket:
        print('Incoming message: ')
        print(message)
        result = ast.literal_eval(message)
        print(result['data'])
        # print(result)
        # print(message.player_name + " sends " + message.message)
        # data = {
        #     "player_name": message.player_name,
        #     "message": "Input received",
        #     "success": True,
        # }
        # await websocket.send(data)
        MESSAGES.append(message)
        await broadcast(message)
    print("Client Disconnected")


async def main():
    print("Starting up server...")
    async with serve(handler, "localhost", 8765):
        print("Server started. Awaiting broadcast message")
        await broadcast_messages()  # run forever


if __name__ == "__main__":
    asyncio.run(main())


