import React, { useState } from "react";
import { MessageCircle, X } from "lucide-react";
import ReactMarkdown from "react-markdown";

function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hi! 🍕 How can I help you today?" },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages([...messages, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8001/api/v1/chat/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include", // important if cookies/session are used
        body: JSON.stringify({ human_message: input }),
      });

      const data = await response.json();

      if (data.ai_message) {
        setMessages((prev) => [
          ...prev,
          { sender: "bot", text: data.ai_message },
        ]);
      } else {
        setMessages((prev) => [
          ...prev,
          { sender: "bot", text: "⚠️ Sorry, no response from server." },
        ]);
      }
    } catch (error) {
      console.error("Chatbot error:", error);
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "❌ Error connecting to chatbot server." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Floating Chat Button */}
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          className="fixed bottom-6 right-6 bg-red-600 hover:bg-red-700 text-white rounded-full p-4 shadow-lg transition-all"
        >
          <MessageCircle size={28} />
        </button>
      )}

      {/* Chatbot UI */}
      {isOpen && (
        <div className="fixed bottom-6 right-6 w-[400px] h-[450px] bg-white rounded-2xl shadow-2xl flex flex-col overflow-hidden">
          {/* Header */}
          <div className="bg-red-600 text-white flex justify-between items-center p-3">
            <div className="flex items-center space-x-2">
              <img src="/logo.jpeg" alt="Bot Logo" className="w-8 h-8 rounded-full" />
              <h3 className="font-semibold">PizzaBot</h3>
            </div>
            <button onClick={() => setIsOpen(false)}>
              <X size={20} />
            </button>
          </div>

          {/* Messages */}
          <div className="flex-1 p-3 overflow-y-auto space-y-2 bg-gray-50">
            {messages.map((msg, idx) => (
              <div
                key={idx}
                className={`p-2 rounded-lg max-w-[75%] whitespace-pre-line ${
                  msg.sender === "user"
                    ? "bg-yellow-300 ml-auto text-black"
                    : "bg-gray-200 mr-auto text-gray-800"
                }`}
              >
                {msg.sender === "bot" ? (
                  <ReactMarkdown>{msg.text}</ReactMarkdown>
                ) : (
                  msg.text
                )}
              </div>
            ))}
            {loading && (
              <div className="p-2 rounded-lg bg-gray-200 mr-auto text-gray-600 italic">
                Typing...
              </div>
            )}
          </div>

          {/* Input */}
          <div className="p-3 flex items-center border-t">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type a message..."
              className="flex-1 px-3 py-2 border rounded-lg text-sm outline-none"
              onKeyDown={(e) => e.key === "Enter" && handleSend()}
            />
            <button
              onClick={handleSend}
              className="ml-2 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 disabled:opacity-50"
              disabled={loading}
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Chatbot;

