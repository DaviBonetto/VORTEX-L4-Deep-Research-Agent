import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

from src.state.graph import AgentState
from src.agents.researcher import research_node

load_dotenv()

def build_graph() -> StateGraph:
    workflow = StateGraph(AgentState)
    
    workflow.add_node("researcher", research_node)
    
    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", END)
    
    return workflow.compile()

def main():
    print("══════════════════════════════════════════════════════════════════════")
    print("🌪️ VORTEX Deep Research Agent")
    print("══════════════════════════════════════════════════════════════════════")
    
    graph = build_graph()
    
    initial_state: AgentState = {
        "task": "Analysis of Quantum Computing trends 2026",
        "research_data": [],
        "report_content": "",
        "revision_count": 0
    }
    
    print(f"\n📋 Task: {initial_state['task']}")
    print("🔍 Researching...\n")
    
    result = graph.invoke(initial_state)
    
    print("══════════════════════════════════════════════════════════════════════")
    print("📊 Research Results:")
    print("══════════════════════════════════════════════════════════════════════")
    
    for i, data in enumerate(result["research_data"], 1):
        print(f"\n[{i}] {data[:500]}...")
    
    print("\n══════════════════════════════════════════════════════════════════════")
    print("✅ Research Complete")
    print("══════════════════════════════════════════════════════════════════════")

if __name__ == "__main__":
    main()
