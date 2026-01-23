"""
VORTEX v3 - RAG-Enabled Research Agent
Integrates with NEXUS Vector Database for long-term memory
"""

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
from src.tools.memory import get_nexus_client

load_dotenv()

MAX_REVISIONS = 2
APPROVAL_THRESHOLD = 7


def should_continue(state: AgentState) -> str:
    score = state.get("score", 0)
    revision_count = state.get("revision_count", 0)
    
    if score >= APPROVAL_THRESHOLD:
        print(f"\n   ✅ APPROVED (Score: {score}/10)")
        return "end"
    elif revision_count >= MAX_REVISIONS:
        print(f"\n   ⚠️ MAX REVISIONS ({revision_count})")
        return "end"
    else:
        print(f"\n   🔄 REVISING (Score: {score}/10)")
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
        {"revise": "writer", "end": END}
    )
    
    return workflow.compile()


def demo_rag_integration():
    """Demonstrate RAG integration with NEXUS."""
    print("══════════════════════════════════════════════════════════════════════")
    print("🔗 RAG INTEGRATION DEMO")
    print("══════════════════════════════════════════════════════════════════════")
    
    nexus = get_nexus_client()
    
    # Check NEXUS connection
    if not nexus.health_check():
        print("❌ NEXUS server not running!")
        print("   Start it with: cd ~/NEXUS-L4-HighPerf-Vector-DB && cargo run --release")
        return False
    
    stats = nexus.get_stats()
    print(f"✅ NEXUS Connected: {stats.get('total_vectors', 0)} vectors in memory")
    
    # Insert secret knowledge
    print("\n📥 Inserting secret knowledge into NEXUS...")
    secrets = [
        "Project Titan is classified level 5 and involves quantum AI integration.",
        "The Titan Protocol Initiative consists of 300 autonomous systems.",
        "GENESIS is System 01, VORTEX is System 02, NEXUS is System 03.",
    ]
    
    for secret in secrets:
        nexus.save(secret, {"source": "classified", "level": 5})
    
    print(f"   Inserted {len(secrets)} classified documents\n")
    
    # Test retrieval
    print("🔍 Testing memory retrieval...")
    results = nexus.search("What is Project Titan?", top_k=3)
    
    print("\n📚 Retrieved from NEXUS:")
    for i, r in enumerate(results, 1):
        text = r.get("metadata", {}).get("text", "")
        score = r.get("score", 0)
        print(f"   [{i}] Score: {score:.2f} | {text[:80]}...")
    
    return True


def main():
    print("══════════════════════════════════════════════════════════════════════")
    print("🌪️ VORTEX v3 // RAG-Enabled Research Agent")
    print("   Integrated with NEXUS Vector Memory")
    print("══════════════════════════════════════════════════════════════════════")
    
    # Demo RAG integration
    if not demo_rag_integration():
        return
    
    print("\n══════════════════════════════════════════════════════════════════════")
    print("🚀 Starting Research Pipeline...")
    print("══════════════════════════════════════════════════════════════════════")
    
    graph = build_graph()
    
    # Query that will use BOTH memory and web search
    initial_state: AgentState = {
        "task": "What is Project Titan and how does it relate to autonomous AI systems?",
        "research_data": [],
        "analysis_content": "",
        "report_content": "",
        "critique": "",
        "score": 0,
        "revision_count": 0
    }
    
    print(f"\n📋 Task: {initial_state['task']}")
    print("\n🔍 Stage 1: Research (Memory + Web)...")
    
    result = graph.invoke(initial_state)
    
    print("\n══════════════════════════════════════════════════════════════════════")
    print(f"📊 FINAL SCORE: {result['score']}/10")
    print("══════════════════════════════════════════════════════════════════════")
    
    # Save report
    with open("output_report.md", "w", encoding="utf-8") as f:
        f.write(result["report_content"])
    
    print("\n📄 Report saved to: output_report.md")
    print("✅ Pipeline Complete!")


if __name__ == "__main__":
    main()
