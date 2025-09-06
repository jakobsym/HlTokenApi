import asyncio
import os
from websockets.asyncio.client import connect
from dotenv import load_dotenv

load_dotenv()

HELIUS_WS_CONNECTION = f"{os.getenv('HELIUS_MAINNET_CONNECTION_STR') + os.getenv('HELIUS_API_KEY')}"

async def hello_solana():
    async with connect(HELIUS_WS_CONNECTION) as websocket:
        await websocket.send("hello world!")
        message = await websocket.recv()
        print(message)