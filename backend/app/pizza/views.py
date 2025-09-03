from fastapi import APIRouter, Request
from .services import *

router = APIRouter()

class PizzaView:
    @router.get("/api/v1/pizza/list/", status_code=200)
    async def get_pizza(page: int= 1, page_size: int= 4):
        """
        page-> page number, starts from 1.
        """
        pizzas= await list_available_pizza(offset= (page_size * (page -1)), limit= page_size)
        return {
                "available_pizza": pizzas
                }

    @router.get("/api/v1/pizza/ingredients/{pizza_id}/", status_code=200)
    async def get_ingredients_of_pizza(pizza_id: int):
        ingredients= await ingredients_for_a_pizza(pizza_id)
        return {
                "message": "Successfully retrieved ingredients.." if ingredients else "Invalid pizza_id or no data present..",
                "data": {"pizza_id": pizza_id, "ingredients": ingredients} if ingredients else {}
                }

