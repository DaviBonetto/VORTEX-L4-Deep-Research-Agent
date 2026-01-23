"""
NEXUS Vector DB Client - Long-term Memory for VORTEX
Connects to NEXUS-L4 Vector Database for RAG operations
"""

import httpx
import uuid
from typing import List, Dict, Any, Optional
from langchain_openai import OpenAIEmbeddings

NEXUS_BASE_URL = "http://127.0.0.1:8081"
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMENSION = 1536


class NexusClient:
    """Client for NEXUS Vector Database - Provides long-term memory for agents."""
    
    def __init__(self, base_url: str = NEXUS_BASE_URL):
        self.base_url = base_url
        self.embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
        self.http_client = httpx.Client(timeout=30.0)
    
    def embed_text(self, text: str) -> List[float]:
        """Generate embedding vector from text using OpenAI."""
        return self.embeddings.embed_query(text)
    
    def save(self, text: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Save text to NEXUS memory.
        Generates embedding and stores with metadata.
        """
        doc_id = f"mem-{uuid.uuid4().hex[:8]}"
        embedding = self.embed_text(text)
        
        payload = {
            "id": doc_id,
            "embedding": embedding,
            "metadata": {
                "text": text,
                **(metadata or {})
            }
        }
        
        response = self.http_client.post(
            f"{self.base_url}/upsert",
            json=payload
        )
        response.raise_for_status()
        
        print(f"   💾 NEXUS: Saved memory [{doc_id}]")
        return response.json()
    
    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Search NEXUS memory for relevant information.
        Returns list of matching memories with scores.
        """
        embedding = self.embed_text(query)
        
        payload = {
            "embedding": embedding,
            "top_k": top_k
        }
        
        try:
            response = self.http_client.post(
                f"{self.base_url}/query",
                json=payload
            )
            response.raise_for_status()
            
            data = response.json()
            results = data.get("results", [])
            
            # Filter by relevance threshold
            relevant = [r for r in results if r.get("score", 0) > 0.7]
            
            if relevant:
                print(f"   🔍 NEXUS: Found {len(relevant)} relevant memories")
            
            return relevant
            
        except httpx.ConnectError:
            print("   ⚠️ NEXUS: Connection failed (is server running?)")
            return []
        except Exception as e:
            print(f"   ⚠️ NEXUS: Search error - {e}")
            return []
    
    def health_check(self) -> bool:
        """Check if NEXUS server is available."""
        try:
            response = self.http_client.get(f"{self.base_url}/health")
            return response.status_code == 200
        except:
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get NEXUS database statistics."""
        try:
            response = self.http_client.get(f"{self.base_url}/stats")
            return response.json()
        except:
            return {"error": "Unable to connect"}


# Singleton instance for shared use
_nexus_client: Optional[NexusClient] = None

def get_nexus_client() -> NexusClient:
    """Get or create singleton NexusClient instance."""
    global _nexus_client
    if _nexus_client is None:
        _nexus_client = NexusClient()
    return _nexus_client
