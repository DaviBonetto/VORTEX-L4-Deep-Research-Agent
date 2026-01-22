<div align="center">

```
  ██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
  ██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
  ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
  ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
   ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
    ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

### 🌪️ L4 Deep Research Agent

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-00ADD8?style=for-the-badge)](https://github.com/langchain-ai/langgraph)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai)](https://openai.com/)
[![Status](https://img.shields.io/badge/Status-Beta-green?style=for-the-badge)](#)

**Part of the Titan Protocol Initiative — System 02/300**

*Autonomous Research Pipeline: Search → Analyze → Report*

</div>

---

## 🏗️ Architecture

```mermaid
%%{init: {'theme': 'dark'}}%%
flowchart TD
    subgraph Input ["📥 Input"]
        A["👤 Research Query"]
    end
    
    subgraph Pipeline ["🤖 Cognitive Pipeline"]
        B["🔍 Researcher"]
        C["📊 Analyst"]
        D["✍️ Writer"]
    end
    
    subgraph Tools ["🔧 External Tools"]
        E["🌐 Tavily Search"]
        F["🧠 GPT-4"]
    end
    
    subgraph Output ["📤 Output"]
        G["📄 Markdown Report"]
    end

    A --> B
    B <--> E
    B -->|research_data| C
    C <--> F
    C -->|analysis_content| D
    D <--> F
    D -->|report_content| G

    style A fill:#1a365d,stroke:#4299e1,color:#fff
    style B fill:#22543d,stroke:#48bb78,color:#fff
    style C fill:#553c9a,stroke:#9f7aea,color:#fff
    style D fill:#744210,stroke:#ed8936,color:#fff
    style G fill:#1a365d,stroke:#4299e1,color:#fff
```

---

## 🔄 Pipeline Flow

| Stage | Agent | Input | Output | Tool |
|-------|-------|-------|--------|------|
| 1 | 🔍 Researcher | `task` | `research_data` | Tavily |
| 2 | 📊 Analyst | `research_data` | `analysis_content` | GPT-4 |
| 3 | ✍️ Writer | `analysis_content` | `report_content` | GPT-4 |

---

## 🚀 Quick Start

```bash
cd ~/VORTEX-L4-Deep-Research-Agent
source venv/bin/activate
python src/main.py
```

Output: `output_report.md` with full research report.

---

## 📁 Project Structure

```
src/
├── agents/
│   ├── researcher.py   # Tavily search node
│   ├── analyst.py      # GPT-4 analysis node
│   └── writer.py       # GPT-4 report generation
├── tools/
│   └── search.py       # Tavily integration
├── state/
│   └── graph.py        # AgentState TypedDict
├── utils/
│   └── llm.py          # LLM factory
└── main.py             # LangGraph orchestration
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Orchestration | LangGraph |
| LLM | OpenAI GPT-4 |
| Search | Tavily API |
| State | TypedDict |

---

<div align="center">

**Built with 🐍 Python by [Davi Bonetto](https://github.com/DaviBonetto)**

*Part of the Titan Protocol Initiative — System 02/300*

</div>
