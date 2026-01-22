import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

from src.state.graph import AgentState
from src.agents.researcher import research_node
from src.agents.analyst import analyst_node
from src.agents.writer import writer_node

load_dotenv()

def build_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("researcher", research_node)
    workflow.add_node("analyst", analyst_node)
    workflow.add_node("writer", writer_node)
    
    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "analyst")
    workflow.add_edge("analyst", "writer")
    workflow.add_edge("writer", END)
    
    return workflow.compile()

def save_report(content: str, filename: str = "output_report.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"📄 Report saved to: {filename}")

def main():
    print("══════════════════════════════════════════════════════════════════════")
    print("🌪️ VORTEX Deep Research Agent")
    print("   Complete Cognitive Pipeline: Researcher -> Analyst -> Writer")
    print("══════════════════════════════════════════════════════════════════════")
    
    graph = build_graph()
    
    initial_state: AgentState = {
        "task": "Current state of Quantum Computing in 2026",
        "research_data": [],
        "analysis_content": "",
        "report_content": "",
        "revision_count": 0
    }
    
    print(f"\n📋 Task: {initial_state['task']}")
    print("\n🔍 Stage 1: Researching...")
    print("📊 Stage 2: Analyzing...")
    print("✍️  Stage 3: Writing Report...\n")
    
    result = graph.invoke(initial_state)
    
    print("══════════════════════════════════════════════════════════════════════")
    print("📄 FINAL REPORT")
    print("══════════════════════════════════════════════════════════════════════")
    print(result["report_content"])
    print("══════════════════════════════════════════════════════════════════════")
    
    save_report(result["report_content"])
    
    print("\n✅ Pipeline Complete!")

if __name__ == "__main__":
    main()
