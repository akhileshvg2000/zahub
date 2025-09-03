from typing import List, Any, Optional, Dict, Union
from .services import list_available_pizza, ingredients_for_a_pizza

async def get_available_pizza(
        page_no: int= 1,
        page_size: int= 3,
        ) -> Union[List[Dict[str, Any]], str]:
    """
    Retrieve a paginated list of pizza available in ZaHub shop.
    Args:
        page_no (int, optional): Page number
        page_size (int, optional): Page size
    Returns (list): List of dictionary. Each dictionary represents a pizza object.
        Number of pizza items included depends on `page_size`.
        Output schema:
            [
             {
              "pizza_id": int,
              "pizza_name": str
             }
            ]
    """
    available_pizza= await list_available_pizza(offset= (page_no-1)* page_size, limit= page_size)
    response= [{"pizza_id": pizza.id, "pizza_name": pizza.name} for pizza in available_pizza]
    if not response:
        response= "No pizza available for the given pagination param..."
    return response

async def get_ingredients(
        pizza_id: int,
        ) -> Dict[str, Any] | str:
    """
    Retrieve the ingredients used to prepare given pizza.
    Args:
        pizza_id (int, required): Unique identifier (ID) for the pizza.
    Returns (str):
        Names of ingredients.
    """
    if not pizza_id:
        return "ErrorMessage: Value for `pizza_id` is required..."
    ingredients= await ingredients_for_a_pizza(pizza_id)
    response= {"pizza_id": pizza_id, "ingredients": ingredients} if ingredients else f"Message: Given pizza_id, {pizza_id} is not valid, or no data of ingredients for the pizza..."
    return response



