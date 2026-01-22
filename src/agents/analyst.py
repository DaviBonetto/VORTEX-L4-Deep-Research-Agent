from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage

from src.state.graph import AgentState
from src.utils.llm import get_llm

SYSTEM_PROMPT = """You are a Senior Data Analyst at a top-tier research firm.
Your task is to synthesize raw search results into clear, actionable insights.

Guidelines:
- Extract the most important facts and trends
- Identify patterns and connections
- Organize insights by theme
- Be concise but comprehensive
- Use bullet points for clarity"""

def analyst_node(state: AgentState) -> Dict[str, Any]:
    llm = get_llm()
    
    research_text = "\n\n".join(state["research_data"])
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Analyze the following research data and provide key insights:\n\n{research_text}")
    ]
    
    response = llm.invoke(messages)
    
    return {"analysis_content": response.content}
