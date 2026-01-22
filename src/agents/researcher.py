from typing import Dict, Any
from src.state.graph import AgentState
from src.tools.search import get_search_tool

def research_node(state: AgentState) -> Dict[str, Any]:
    task = state["task"]
    search_tool = get_search_tool()
    
    results = search_tool.invoke(task)
    
    research_data = []
    for result in results:
        if isinstance(result, dict):
            content = result.get("content", str(result))
        else:
            content = str(result)
        research_data.append(content)
    
    return {"research_data": research_data}
