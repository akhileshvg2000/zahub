# zahub
Pizza delivery web integrated with AI chatbot

curl -X "POST" -c cookie.txt localhost:8001/api/v1/chat/ -H 'Content-type: application/json' -d '{"human_message": "Hi"}'
curl -X "POST" -b cookie.txt localhost:8001/api/v1/chat/ -H 'Content-type: application/json' -d '{"human_message": "What pizzas are available now ?"}'
curl -X "POST" -b cookie.txt localhost:8001/api/v1/chat/ -H 'Content-type: application/json' -d '{"human_message": "What ingredients are using for Margherita?"}'
curl -X "POST" -b cookie.txt localhost:8001/api/v1/chat/ -H 'Content-type: application/json' -d '{"human_message": "What are the questiions I asked so far?"}'
const API_URL = process.env.REACT_APP_API_URL;

