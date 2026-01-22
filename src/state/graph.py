from typing import TypedDict, List

class AgentState(TypedDict):
    task: str
    research_data: List[str]
    analysis_content: str
    report_content: str
    revision_count: int
