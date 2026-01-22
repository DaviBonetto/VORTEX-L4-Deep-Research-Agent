from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage

from src.state.graph import AgentState
from src.utils.llm import get_llm

SYSTEM_PROMPT = """You are a Technical Writer specializing in research reports.
Your task is to write a comprehensive, well-structured report in Markdown format.

Report Structure:
1. Executive Summary (2-3 sentences)
2. Key Findings (bullet points)
3. Detailed Analysis (paragraphs with headers)
4. Conclusion and Implications
5. References (if applicable)

Guidelines:
- Use proper Markdown formatting (headers, bullets, bold)
- Be professional and objective
- Make it scannable with clear sections
- Include actionable takeaways"""

def writer_node(state: AgentState) -> Dict[str, Any]:
    llm = get_llm()
    
    task = state["task"]
    analysis = state["analysis_content"]
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Write a comprehensive research report on: {task}\n\nBased on this analysis:\n\n{analysis}")
    ]
    
    response = llm.invoke(messages)
    
    return {"report_content": response.content}
