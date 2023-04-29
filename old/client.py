import asyncio
import telnetlib3


async def shell(reader, writer):
    print(" -- Starting shell")
    while True:
        # read stream until '?' mark is found
        print(" -- awaiting reader.read()")
        outp = await reader.read(1024)

        if not outp:
            # End of File
            break

        print(outp)
        inp = input("client :>")
        writer.write(inp)
        # elif '?' in outp:
        # replay all questions with 'y'
        # writer.write('y')

        # display all server output

    # EOF
    print()

print("creating event loop...")
loop = asyncio.get_event_loop()
print("creating telnet service...")
coro = telnetlib3.open_connection('localhost', 5005, shell=shell)
print("starting loop with telnet...")
reader, writer = loop.run_until_complete(coro)
print("starting loopL writer.protocol.waiter_closed...")
loop.run_until_complete(writer.protocol.waiter_closed)
