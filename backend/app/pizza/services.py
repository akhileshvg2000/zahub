from sqlmodel import select

from app.core.db import get_session
from .models import Pizzas
from typing import List, Any, Optional

async def list_available_pizza(offset: int, limit: int) -> List[Pizzas] | None:
    session= next(get_session())
    available_pizzas= session.exec(select(Pizzas).offset(offset).limit(limit)).all()
    return available_pizzas
async def ingredients_for_a_pizza(pizza_id: int) -> str | None:
    session= next(get_session())
    pizza= session.get(Pizzas, pizza_id)
    ingredients= pizza.ingredients if pizza else None
    return ingredients
