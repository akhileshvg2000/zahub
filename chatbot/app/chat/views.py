from langchain_core.messages import HumanMessage
from fastapi import APIRouter, Request
from pydantic import BaseModel
import uuid
from app.agent import graph


class ChatRequest(BaseModel):
    human_message: str

router= APIRouter()

class ChatView:
    @router.post("/api/v1/chat/", status_code=200)
    async def bot_chat_completion(request: Request, body: ChatRequest):
        session= request.session
        if "user_id" not in session:
            session["user_id"]= str(uuid.uuid4())
        user_id= session["user_id"]
        human_message= body.human_message

        # Grpah invokation
        config = {"configurable": {"thread_id": user_id}}
        payload= {"messages": [HumanMessage(content= human_message)]}
        ai_message= None
        
        # Logging graph execution, internall calls and capturing output message to the user.
        async for update in  graph.graph.astream(payload, config, stream_mode="updates"):
            print(update)
            if 'agent' in update:
                for agent_message in update.get("agent").get("messages"):
                    print(agent_message.pretty_repr())
                    if 'tool_calls' not in agent_message.additional_kwargs:
                        ai_message= agent_message.content
            if 'tools' in update:
                for tool_message in update.get("tools").get("messages"):
                    print(tool_message.pretty_repr())
        return {
                "ai_message": ai_message 
                }
