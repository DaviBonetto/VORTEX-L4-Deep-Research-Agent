from langchain_openai import ChatOpenAI

def get_llm(model: str = "gpt-4o-mini", temperature: float = 0.7) -> ChatOpenAI:
    return ChatOpenAI(model=model, temperature=temperature)
