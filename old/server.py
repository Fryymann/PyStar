import asyncio
import telnetlib3

player_name = ""

messages = ['\r\nWhat is your name?\r\n', 'What is your quest?\r\n']


async def shell(reader, writer):
    print(" -- Starting shell")
    print(" -- - loopnumber = 0")
    loopnumber = 0
    inp_string = ""

    while loopnumber < 10:
        print(' -- loop number ' + str(loopnumber) + "\r\n")
        # print(' -- awaiting reader.read(1)')
        inp = await reader.read(1)
        writer.write("Loop Number: " + str(loopnumber))
        if inp:
            inp_string += inp
            print(" - dev - inp_string: " + inp_string)
            if "\r\n" in inp_string:
                writer.echo(inp_string)
                print(inp_string)
                inp_string = ""

                # writer.write('\r\nThey say the only way to win is to not play at all.\r\n')
                await writer.drain()

        loopnumber += 1
    writer.close()


print("Starting server...")
loop = asyncio.get_event_loop()
print("creating event loop...")
coro = telnetlib3.create_server(port=5005, shell=shell)
print("creating telnet service...")
server = loop.run_until_complete(coro)
print("creating loop: server.wait_closed()")
loop.run_until_complete(server.wait_closed())
