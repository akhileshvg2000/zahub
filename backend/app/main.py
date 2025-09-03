from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import contextlib

from app.core.db import init_db
from app.pizza.views import router as pizza_router
from app.mcp.pizza import mcp as pizza_mcp

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialise shema, add sample data to tables
    await init_db()
    # Loading MCP server
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(pizza_mcp.session_manager.run())
        yield

app = FastAPI(lifespan= lifespan)
@app.get("/health")
async def health_check():
    return {"status": "Ok"}

app.include_router(pizza_router)
# Mounting endpoints of MCP protocol
app.mount("/zahub-pizza-mcp", pizza_mcp.streamable_http_app())


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
