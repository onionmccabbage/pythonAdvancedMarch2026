import asyncio
import sys

async def myClient(message='default'):
    reader, writer = await asyncio.open_connection('localhost', 9876)
    print('sending a message')
    writer.write(message.encode())
    await writer.drain() # wait for all teh message stram to exhaust
    writer.close()

if __name__ == '__main__':
    if len(sys.argv)>1:
        msg = ' '.join(sys.argv[1:])
    else:
        msg = 'hello'
    asyncio.run( myClient(msg) )