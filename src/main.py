import asyncio
from util.config import config_logging
from routes.helius_route import hello_solana
from fastapi import FastAPI


app = FastAPI(title="BigBid", description="tbd", version="0.1")
# app.include_router(xyz_routes, prefix="/xyz", tags["xyz"])
# ...

def main():   
    config_logging()
    hello_solana()


#TODO: healthcheack route
@app.get("/health")
async def health_check():
    return {"status" : "healthy"}
    

if __name__ == "__main__":
    asyncio.run(main())