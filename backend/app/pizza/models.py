from typing import Annotated

from sqlmodel import Field, SQLModel


class Pizzas(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    price: int | None = Field(default=None, index=True)
    ingredients: str = Field(index=True)
