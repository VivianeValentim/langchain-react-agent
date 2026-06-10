import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from src.tools import calculator

load_dotenv()

def build_agent_executor() -> AgentExecutor:
    """Builds and returns the agent executor configured with the tools."""
    
    # temperature=0 ensures that the AI ​​is deterministic in its decision-making process regarding whether or not to use the tool.
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an AI assistant focused on accuracy. "
            "Rule 1: For historical, scientific, or general knowledge questions, respond directly. "
            "Rule 2: For ANY question involving mathematical calculation, you are REQUIRED to use the 'calculator' tool."
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    tools = [calculator]
    
    # Creates agent intelligence based on tool calling.
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # The AgentExecutor is the background loop that actually executes the tool
    return AgentExecutor(agent=agent, tools=tools, verbose=True)