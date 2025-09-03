from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel

from app.pizza.models import Pizzas
from .test_data import init_pizza_test_data

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

async def init_db():
    create_db_and_tables()
    init_pizza_test_data(get_session())

