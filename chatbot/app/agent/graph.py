from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from .state import State
from . import db, llm_provider
from .tools import load_tools
from .prompts import system_prompt



graph= None

async def init_graph():
    """
    Create the agent graph and assign it to the global variable `graph`.
    """
    global graph

    tools= await load_tools()
    llm_agent= llm_provider.llm.bind_tools(tools, parallel_tool_calls= True)
    async def agent_node(state: State):
        system_message= SystemMessage(content= system_prompt)
        llm_response= await llm_agent.ainvoke([system_message] + state["messages"])
        return {"messages": [llm_response]}

    tool_node= ToolNode(tools)
    checkpointer= db.memory

    graph_builder= StateGraph(State)
    graph_builder.add_node("agent", agent_node)
    graph_builder.add_node("tools", tool_node)

    graph_builder.add_edge(START, "agent")
    graph_builder.add_conditional_edges("agent", tools_condition)
    graph_builder.add_edge("tools", "agent")

    graph= graph_builder.compile(checkpointer=checkpointer)




