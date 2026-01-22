"""
VORTEX - Deep Research Agent
============================
L4 System - Part of the Titan Protocol Initiative

This module initializes the VORTEX system and validates API connections.
"""

import os
from dotenv import load_dotenv

def initialize():
    """Initialize VORTEX system and validate environment."""
    load_dotenv()
    
    print("══════════════════════════════════════════════════════════════════════")
    print("🌪️ VORTEX System Initializing...")
    print("══════════════════════════════════════════════════════════════════════")
    
    # Validate API Keys
    openai_key = os.getenv("OPENAI_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")
    
    if openai_key and openai_key.startswith("sk-"):
        print("✅ OpenAI Key Loaded")
    else:
        print("❌ OpenAI Key Missing or Invalid")
    
    if tavily_key and tavily_key.startswith("tvly-"):
        print("✅ Tavily Key Loaded")
    else:
        print("❌ Tavily Key Missing or Invalid")
    
    print("══════════════════════════════════════════════════════════════════════")
    print("🚀 VORTEX Ready for Deep Research Operations")
    print("══════════════════════════════════════════════════════════════════════")

if __name__ == "__main__":
    initialize()
