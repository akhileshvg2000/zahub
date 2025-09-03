from .main import mcp
from app.pizza.tools import get_available_pizza, get_ingredients

mcp.add_tool(get_available_pizza)
mcp.add_tool(get_ingredients)
