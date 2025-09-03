from app.pizza.models import Pizzas
from sqlmodel import Session

# Example records
sample_pizzas = [
    Pizzas(
        name="Margherita",
        price=8,
        ingredients="Tomato sauce, Mozzarella, Fresh basil, Olive oil"
    ),
    Pizzas(
        name="Pepperoni",
        price=10,
        ingredients="Tomato sauce, Mozzarella, Pepperoni"
    ),
    Pizzas(
        name="BBQ Chicken",
        price=12,
        ingredients="BBQ sauce, Mozzarella, Grilled chicken, Red onion, Cilantro"
    ),
    Pizzas(
        name="Veggie Supreme",
        price=11,
        ingredients="Tomato sauce, Mozzarella, Bell peppers, Onions, Mushrooms, Olives"
    ),
    Pizzas(
        name="Hawaiian",
        price=10,
        ingredients="Tomato sauce, Mozzarella, Ham, Pineapple"
    ),
]

def init_pizza_test_data(session: Session):
    session= next(session) # Generator
    for pizza in sample_pizzas:
        session.add(pizza)
    session.commit()
