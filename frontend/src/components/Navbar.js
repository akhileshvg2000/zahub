import React from "react";

function Navbar() {
  return (
    <nav className="flex justify-between items-center px-8 py-4 bg-red-600 text-white shadow-md">
      <div className="flex items-center space-x-2">
        <img src="/logo.jpeg" alt="Pizza Shop Logo" className="w-10 h-10" />
        <h1 className="text-2xl font-bold">ZaHub</h1>
      </div>
      <ul className="flex space-x-6 text-lg">
        <li className="hover:text-yellow-300 cursor-pointer">Home</li>
        <li className="hover:text-yellow-300 cursor-pointer">Menu</li>
        <li className="hover:text-yellow-300 cursor-pointer">Recipes</li>
        <li className="hover:text-yellow-300 cursor-pointer">Contact</li>
      </ul>
    </nav>
  );
}

export default Navbar;

