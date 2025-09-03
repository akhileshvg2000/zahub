import React, { useState } from "react";

function Hero() {
  const [pizzas, setPizzas] = useState([]);
  const [showPizzas, setShowPizzas] = useState(false);
  const [selectedPizza, setSelectedPizza] = useState(null);
  const [ingredients, setIngredients] = useState(null);

  // Fetch all pizzas
  const fetchPizzas = async () => {
    try {
      const res = await fetch("http://localhost:8000/api/v1/pizza/list/");
      const data = await res.json();
      setPizzas(data.available_pizza);
      setShowPizzas(true);
    } catch (error) {
      console.error("Error fetching pizzas:", error);
    }
  };

  // Fetch ingredients for selected pizza
  const fetchIngredients = async (pizzaId) => {
    try {
      const res = await fetch(
        `http://172.17.0.1:8000/api/v1/pizza/ingredients/${pizzaId}/`
      );
      const data = await res.json();
      setIngredients(data.data.ingredients.split(","));
    } catch (error) {
      console.error("Error fetching ingredients:", error);
    }
  };

  return (
    <section
      className="flex-grow flex items-center justify-center bg-cover bg-center relative text-white"
      style={{ backgroundImage: "url('/pizza-bg.jpeg')" }}
    >
      <div className="bg-black bg-opacity-70 p-8 rounded-2xl text-center shadow-xl w-11/12 md:w-2/3 lg:w-1/2">
        <h2 className="text-4xl md:text-5xl font-bold mb-6">
          Welcome to ZaHub 
        </h2>

        {/* Vibrating Button */}
        {!showPizzas && (
          <button
            onClick={fetchPizzas}
            className="px-6 py-3 bg-yellow-400 text-black font-semibold rounded-lg animate-bounce hover:bg-yellow-500"
          >
            🍕 List All Pizzas
          </button>
        )}

        {/* Pizza List */}
        {showPizzas && !selectedPizza && (
          <div className="mt-6 space-y-3">
            {pizzas.map((pizza) => (
              <button
                key={pizza.id}
                onClick={() => {
                  setSelectedPizza(pizza);
                  setIngredients(null); // reset
                }}
                className="block w-full px-4 py-2 bg-red-600 rounded-lg hover:bg-red-700 transition"
              >
                {pizza.name} — ${pizza.price}
              </button>
            ))}
          </div>
        )}

        {/* Selected Pizza */}
        {selectedPizza && (
          <div className="mt-6">
            <h3 className="text-2xl font-bold">{selectedPizza.name}</h3>

            {!ingredients ? (
              <button
                onClick={() => fetchIngredients(selectedPizza.id)}
                className="mt-4 px-6 py-2 bg-green-400 text-black font-semibold rounded-lg hover:bg-green-500"
              >
                Show Ingredients
              </button>
            ) : (
              <ul className="mt-4 text-lg space-y-1">
                {ingredients.map((ing, i) => (
                  <li key={i}>✅ {ing.trim()}</li>
                ))}
              </ul>
            )}

            <button
              onClick={() => {
                setSelectedPizza(null);
                setIngredients(null);
              }}
              className="mt-6 px-4 py-2 bg-gray-500 rounded-lg hover:bg-gray-600"
            >
              🔙 Back to Pizzas
            </button>
          </div>
        )}
      </div>
    </section>
  );
}

export default Hero;

