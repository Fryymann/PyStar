import asyncio
from websockets.sync.client import connect

# ACTIVE = True


def shell(player_name):
    with connect("ws://72.110.98.3:8765") as websocket:
        while True:
            inp = input(player_name + ":: ")

            if inp == 'quit':
                print('You log off.')
                break
                # ACTIVE = False

            data = {
                "player_name": player_name,
                "data": inp,
            }
            # print(f"data :: {data}")

            websocket.send(str(data))
            message = websocket.recv()
            print(f"Received: {message}")


name = input('What is your name?')

if name:
    shell(name)




