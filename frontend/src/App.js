import React from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Chatbot from "./components/Chatbot";

function App() {
  return (
    <div className="min-h-screen flex flex-col relative">
      <Navbar />
      <Hero />
      <Chatbot />  
    </div>
  );
}

export default App;

