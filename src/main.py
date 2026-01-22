import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

from src.state.graph import AgentState
from src.agents.researcher import research_node
from src.agents.analyst import analyst_node
from src.agents.writer import writer_node
from src.agents.reviewer import reviewer_node

load_dotenv()

MAX_REVISIONS = 3
APPROVAL_THRESHOLD = 8

def should_continue(state: AgentState) -> str:
    score = state.get("score", 0)
    revision_count = state.get("revision_count", 0)
    
    if score >= APPROVAL_THRESHOLD:
        print(f"\n   ✅ APPROVED (Score: {score}/10)")
        return "end"
    elif revision_count >= MAX_REVISIONS:
        print(f"\n   ⚠️ MAX REVISIONS REACHED ({revision_count})")
        return "end"
    else:
        print(f"\n   🔄 REVISING (Score: {score}/10, Attempt: {revision_count}/{MAX_REVISIONS})")
        return "revise"

def build_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("researcher", research_node)
    workflow.add_node("analyst", analyst_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("reviewer", reviewer_node)
    
    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "analyst")
    workflow.add_edge("analyst", "writer")
    workflow.add_edge("writer", "reviewer")
    
    workflow.add_conditional_edges(
        "reviewer",
        should_continue,
        {
            "revise": "writer",
            "end": END
        }
    )
    
    return workflow.compile()

def save_report(content: str, filename: str = "output_report.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n📄 Report saved to: {filename}")

def main():
    print("══════════════════════════════════════════════════════════════════════")
    print("🌪️ VORTEX v2 // Autonomous Research Agent")
    print("   Cyclic Pipeline: Researcher -> Analyst -> Writer <-> Reviewer")
    print("══════════════════════════════════════════════════════════════════════")
    
    graph = build_graph()
    
    initial_state: AgentState = {
        "task": "Current state of Quantum Computing in 2026",
        "research_data": [],
        "analysis_content": "",
        "report_content": "",
        "critique": "",
        "score": 0,
        "revision_count": 0
    }
    
    print(f"\n📋 Task: {initial_state['task']}")
    print(f"⚙️ Settings: Approval >= {APPROVAL_THRESHOLD}/10, Max Revisions: {MAX_REVISIONS}")
    print("\n🔍 Stage 1: Researching...")
    
    result = graph.invoke(initial_state)
    
    print("\n══════════════════════════════════════════════════════════════════════")
    print(f"📊 FINAL SCORE: {result['score']}/10")
    print(f"🔄 TOTAL REVISIONS: {result['revision_count']}")
    print("══════════════════════════════════════════════════════════════════════")
    print("\n📄 FINAL REPORT:")
    print("══════════════════════════════════════════════════════════════════════")
    print(result["report_content"][:2000])
    if len(result["report_content"]) > 2000:
        print("\n... [truncated for display]")
    print("══════════════════════════════════════════════════════════════════════")
    
    save_report(result["report_content"])
    
    print("\n✅ Pipeline Complete!")

if __name__ == "__main__":
    main()
