import json
import re
from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage

from src.state.graph import AgentState
from src.utils.llm import get_llm

SYSTEM_PROMPT = """You are a Senior Editor and Quality Assurance Specialist.
Your job is to critically evaluate research reports with high standards.

Evaluate the report on:
1. Technical Depth (0-10): Is the content substantive and well-researched?
2. Clarity (0-10): Is it well-organized and easy to understand?
3. Completeness (0-10): Does it cover the topic comprehensively?
4. Actionability (0-10): Are there clear takeaways?

Calculate the average score (0-10).
If score < 8, provide specific critique for improvement.

RESPOND IN THIS EXACT JSON FORMAT:
{
    "score": <number 0-10>,
    "critique": "<specific feedback for improvement or 'Approved' if score >= 8>"
}

BE HARSH. Only award 8+ for truly excellent reports."""

def reviewer_node(state: AgentState) -> Dict[str, Any]:
    llm = get_llm(temperature=0.3)
    
    report = state["report_content"]
    revision_count = state.get("revision_count", 0)
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Evaluate this report (Revision #{revision_count}):\n\n{report}")
    ]
    
    response = llm.invoke(messages)
    content = response.content
    
    try:
        json_match = re.search(r'\{[^{}]*\}', content, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            score = int(result.get("score", 5))
            critique = result.get("critique", "No specific feedback")
        else:
            score = 5
            critique = content
    except (json.JSONDecodeError, ValueError):
        score = 5
        critique = content
    
    print(f"   📊 Review Score: {score}/10")
    print(f"   📝 Critique: {critique[:100]}...")
    
    return {
        "score": score,
        "critique": critique,
        "revision_count": revision_count + 1
    }
