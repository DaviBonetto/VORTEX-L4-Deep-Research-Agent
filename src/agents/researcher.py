"""
Researcher Agent - Web Search + Memory Retrieval
Integrates Tavily Search with NEXUS Vector Memory
"""

from typing import Dict, Any, List
from src.state.graph import AgentState
from src.tools.search import get_search_tool
from src.tools.memory import get_nexus_client


def research_node(state: AgentState) -> Dict[str, Any]:
    """
    Research node with RAG integration.
    1. Check NEXUS memory for existing knowledge
    2. Search web for new information
    3. Save new findings to NEXUS for future use
    """
    task = state["task"]
    nexus = get_nexus_client()
    search_tool = get_search_tool()
    
    research_data: List[str] = []
    
    # =========================================================================
    # Stage 1: Memory Retrieval (NEXUS)
    # =========================================================================
    print("   🧠 Checking long-term memory (NEXUS)...")
    
    memories = nexus.search(task, top_k=3)
    
    for mem in memories:
        metadata = mem.get("metadata", {})
        text = metadata.get("text", "")
        score = mem.get("score", 0)
        
        if text and score > 0.7:
            research_data.append(f"[MEMORY - Score: {score:.2f}] {text}")
    
    if memories:
        print(f"   📚 Retrieved {len(memories)} memories from NEXUS")
    
    # =========================================================================
    # Stage 2: Web Search (Tavily)
    # =========================================================================
    print("   🌐 Searching web (Tavily)...")
    
    try:
        results = search_tool.invoke(task)
        
        web_findings = []
        for result in results:
            if isinstance(result, dict):
                content = result.get("content", str(result))
            else:
                content = str(result)
            
            web_findings.append(content)
            research_data.append(f"[WEB] {content}")
        
        print(f"   🌐 Found {len(web_findings)} web results")
        
        # =====================================================================
        # Stage 3: Save to Memory (NEXUS)
        # =====================================================================
        if web_findings and nexus.health_check():
            print("   💾 Saving new findings to NEXUS memory...")
            
            # Save consolidated findings
            consolidated = f"Research on '{task}': " + " | ".join(web_findings[:2])
            nexus.save(consolidated, {"source": "tavily", "task": task})
            
    except Exception as e:
        print(f"   ⚠️ Web search error: {e}")
    
    return {"research_data": research_data}
