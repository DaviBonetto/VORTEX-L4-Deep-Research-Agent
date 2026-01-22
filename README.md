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
[![Status](https://img.shields.io/badge/Status-Alpha-orange?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

**Part of the Titan Protocol Initiative — System 02/300**

*Multi-Agent Research System with Autonomous Information Gathering*

</div>

---

## 🏗️ Architecture

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'fontSize': '14px'}}}%%
flowchart TD
    subgraph UserSpace ["📱 User Space"]
        A["👤 User Query"]
        H["📄 Final Report"]
    end

    subgraph AgentSpace ["🤖 Agent Space"]
        B["🎯 Supervisor"]
        C["🔍 Researcher"]
        D["📊 Analyst"]
        E["✍️ Writer"]
    end

    subgraph ToolSpace ["🔧 Tools"]
        F["🌐 Tavily Search"]
        G["🧠 GPT-4"]
    end

    A --> B
    B -->|delegate| C
    C --> F
    F --> C
    C -->|data| D
    D --> G
    G --> D
    D -->|insights| E
    E --> G
    E -->|report| H

    style A fill:#1e3a5f,stroke:#4a90d9,color:#fff
    style H fill:#1e5f3a,stroke:#4ad97a,color:#fff
    style B fill:#5f1e3a,stroke:#d94a7a,color:#fff
    style C fill:#3a5f1e,stroke:#7ad94a,color:#fff
    style D fill:#3a1e5f,stroke:#7a4ad9,color:#fff
    style E fill:#5f3a1e,stroke:#d97a4a,color:#fff
```

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
│   └── researcher.py    # Research node implementation
├── tools/
│   └── search.py        # Tavily search integration
├── state/
│   └── graph.py         # AgentState definition
└── main.py              # LangGraph orchestration
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Orchestration | LangGraph |
| LLM | OpenAI GPT-4 |
| Search | Tavily API |
| Validation | Pydantic |

---

<div align="center">

**Built with 🐍 Python by [Davi Bonetto](https://github.com/DaviBonetto)**

</div>
