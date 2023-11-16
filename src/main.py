import os

from dotenv import load_dotenv
from fastapi import FastAPI
from prisma import Prisma
from web3 import Web3, HTTPProvider

import uvicorn

from src.api.routers.TokenController import TokenController
from src.db.TokenDatabase import TokenDatabase
from src.service.TokenService import TokenService
from src.service.web3.Contract import Contract

load_dotenv()

app = FastAPI()
prisma = Prisma()
w3 = Web3(HTTPProvider(os.getenv("INFURA_URL")))

contract = Contract(w3, os.getenv("CONTRACT_ADDRESS"), os.getenv("PUBLIC_KEY"), os.getenv("PRIVATE_KEY"))

tokenDatabase = TokenDatabase(prisma=prisma)
tokenService = TokenService(db=tokenDatabase, token_contract=contract)

app.include_router(TokenController(tokenService=tokenService).router)


@app.on_event("startup")
async def startup_event():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown_event():
    await prisma.disconnect()


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host='0.0.0.0',
        port=8000,
    )
