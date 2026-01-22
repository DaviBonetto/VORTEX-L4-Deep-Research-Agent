<div align="center">

```
  ██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
  ██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
  ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
  ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
   ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
    ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

### 🌪️ L4 Autonomous Research Agent

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-00ADD8?style=for-the-badge)](https://github.com/langchain-ai/langgraph)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai)](https://openai.com/)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)

**Part of the Titan Protocol Initiative — System 02/300**

*Self-Improving Research Pipeline with Autonomous Quality Control*

</div>

---

## 🏗️ Architecture v2 — Cyclic Review Loop

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
        E["🎯 Reviewer"]
    end

    subgraph Decision ["⚖️ Quality Gate"]
        F{"Score >= 8?"}
    end

    subgraph Output ["📤 Output"]
        G["📄 Final Report"]
    end

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F -->|"❌ No: Refine"| D
    F -->|"✅ Yes: Approve"| G

    style A fill:#1a365d,stroke:#4299e1,color:#fff
    style B fill:#22543d,stroke:#48bb78,color:#fff
    style C fill:#553c9a,stroke:#9f7aea,color:#fff
    style D fill:#744210,stroke:#ed8936,color:#fff
    style E fill:#742a2a,stroke:#fc8181,color:#fff
    style F fill:#2d3748,stroke:#a0aec0,color:#fff
    style G fill:#1a365d,stroke:#4299e1,color:#fff
```

---

## 🔄 Self-Improvement Loop

| Condition | Action |
|-----------|--------|
| `score < 8` | Reviewer sends critique → Writer revises |
| `score >= 8` | Report approved → Output |
| `revisions >= 3` | Force output (safety limit) |

---

## 🚀 Quick Start

```bash
cd ~/VORTEX-L4-Deep-Research-Agent
source venv/bin/activate
python src/main.py
```

---

## 📁 Project Structure

```
src/
├── agents/
│   ├── researcher.py   # Tavily search
│   ├── analyst.py      # Data synthesis
│   ├── writer.py       # Report generation (revision-aware)
│   └── reviewer.py     # Quality scoring & critique
├── state/
│   └── graph.py        # AgentState with score/critique
├── utils/
│   └── llm.py          # LLM factory
└── main.py             # Cyclic LangGraph orchestration
```

---

## ⚙️ Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `APPROVAL_THRESHOLD` | 8 | Minimum score to approve |
| `MAX_REVISIONS` | 3 | Maximum revision attempts |

---

<div align="center">

**Built with 🐍 Python by [Davi Bonetto](https://github.com/DaviBonetto)**

*Part of the Titan Protocol Initiative — System 02/300*

</div>
