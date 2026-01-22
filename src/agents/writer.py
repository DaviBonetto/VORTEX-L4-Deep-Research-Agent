from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage

from src.state.graph import AgentState
from src.utils.llm import get_llm

SYSTEM_PROMPT = """You are a Technical Writer specializing in research reports.
Write a comprehensive, well-structured report in Markdown format.

Report Structure:
1. Executive Summary (2-3 sentences)
2. Key Findings (bullet points)
3. Detailed Analysis (with headers)
4. Conclusion and Implications

Guidelines:
- Use proper Markdown formatting
- Be professional and objective
- Include actionable takeaways"""

REVISION_PROMPT = """You are a Technical Writer revising a report based on editorial feedback.

PREVIOUS REPORT:
{previous_report}

EDITOR CRITIQUE:
{critique}

Write an IMPROVED version addressing ALL the critique points.
Make substantial improvements, not minor tweaks."""

def writer_node(state: AgentState) -> Dict[str, Any]:
    llm = get_llm()
    
    task = state["task"]
    analysis = state["analysis_content"]
    critique = state.get("critique", "")
    previous_report = state.get("report_content", "")
    revision_count = state.get("revision_count", 0)
    
    if critique and previous_report and revision_count > 0:
        print(f"   ✍️ Revision #{revision_count}: Incorporating feedback...")
        messages = [
            SystemMessage(content="You are a Technical Writer improving a report based on critique."),
            HumanMessage(content=REVISION_PROMPT.format(
                previous_report=previous_report,
                critique=critique
            ))
        ]
    else:
        print("   ✍️ Writing initial draft...")
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Write a research report on: {task}\n\nBased on analysis:\n\n{analysis}")
        ]
    
    response = llm.invoke(messages)
    
    return {"report_content": response.content}
