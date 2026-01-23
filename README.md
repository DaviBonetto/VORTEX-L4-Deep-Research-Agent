<div align="center">

```
  ██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
  ██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
  ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
  ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
   ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
    ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

### 🌪️ L4 RAG-Enabled Research Agent

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-00ADD8?style=for-the-badge)](https://github.com/langchain-ai/langgraph)
[![RAG](https://img.shields.io/badge/RAG-Enabled-blueviolet?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)

**Part of the Titan Protocol Initiative — System 02/300**

*Multi-Agent Research with Long-Term Vector Memory (NEXUS Integration)*

</div>

---

## 🔗 System Integration

```
┌─────────────────────────────────────────────────────────────────┐
│                    VORTEX (System 02)                           │
│                    Research Agent                               │
├─────────────────────────────────────────────────────────────────┤
│  Memory Retrieval ←──┐                                          │
│        ↓             │                                          │
│  Web Search ────────→ Save to Memory                            │
└────────────┬────────────────────────────────────────────────────┘
             │ HTTP
             ↓
┌─────────────────────────────────────────────────────────────────┐
│                    NEXUS (System 03)                            │
│                    Vector Database                              │
│                    http://localhost:8081                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Start NEXUS (Terminal 1)
```bash
cd ~/NEXUS-L4-HighPerf-Vector-DB
cargo run --release
```

### 2. Run VORTEX (Terminal 2)
```bash
cd ~/VORTEX-L4-Deep-Research-Agent
source venv/bin/activate
python src/main.py
```

---

## 🧠 RAG Flow

1. **Query** → Agent receives research task
2. **Memory Check** → Search NEXUS for existing knowledge
3. **Web Search** → Query Tavily for new information
4. **Memory Save** → Store new findings in NEXUS
5. **Analysis** → Synthesize all data
6. **Report** → Generate final output

---

## 📁 Project Structure

```
src/
├── agents/
│   ├── researcher.py   # RAG-enabled research
│   ├── analyst.py      # Data synthesis
│   ├── writer.py       # Report generation
│   └── reviewer.py     # Quality control
├── tools/
│   ├── search.py       # Tavily web search
│   └── memory.py       # NEXUS client (RAG)
└── main.py             # RAG demo + pipeline
```

---

<div align="center">

**Built with 🐍 Python by [Davi Bonetto](https://github.com/DaviBonetto)**

</div>
