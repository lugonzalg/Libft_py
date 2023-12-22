import os
import asyncio
from Logger import Logger

from typing import AsyncIterator, Dict, Tuple

CHUNK_SIZE = 100
HOST = "127.0.0.1"
PORT = 6667
logger = Logger(name="chat")
users = Dict[Tuple[str,int], asyncio.StreamWriter] = {}

CHUNK_SIZE = 100


async def readlines(reader: asyncio.StreamReader) -> AsyncIterator[bytes]:

    while line := await read_until_eol(reader):
        yield line

async def read_until_eol(reader: asyncio.StreamReader) -> bytes:

    data = b''
    end = os.linesep.encode()

    while data := data + await reader.read(CHUNK_SIZE):
        if end in data:
            message, _, data = data.partition(end)
            return message + end

async def listen_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    
    addr = writer.get_extra_info("peername")
    users[addr] = writer
    logger.info("Connection!")
    async for data in readlines(reader):

        message = data.decode()
        logger.info(f"{addr}: {message}")
        writes = [writer(writer, data) for user, writer in users.items() if user != addr]
        asyncio.gather(*writes)

    del users[addr]

async def main() -> int:

    server = await asyncio.start_server(listen_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    logger.info(f"Server on {addr}")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())