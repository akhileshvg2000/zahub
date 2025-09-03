from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.chat.views import router as chat_router
from app.core.config import settings
from app.agent import graph

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup and shutdown script
    """
    print("Building graph...")
    await graph.init_graph()
    # Verifying whether the graph object created, otherwise application will get shutdown
    if graph.graph:
        yield
    print("server stoping.....")

app= FastAPI(lifespan=lifespan)
app.include_router(chat_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
        SessionMiddleware,
        secret_key= settings.secret_key,
        max_age=15*60, # In seconds
#        same_site="none",
#        https_only=True,        
        )
