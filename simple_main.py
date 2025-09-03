"""
Simple test version without OpenAI Agents SDK to validate our setup
"""
import os
from config.settings import settings

def main():
    """Simple test of our configuration"""
    print(f"🤖 Welcome to {settings.company_name} Customer Support!")
    print(f"📧 Contact: {settings.company_email}")
    print(f"🌐 Website: {settings.company_website}")
    
    # Test knowledge base
    from tools.knowledge_search import search_knowledge_base
    from tools.company_info import get_company_overview
    
    print("\n--- Testing Tools ---")
    print("Company Overview:")
    print(get_company_overview())
    
    print("\nKnowledge Base Test:")
    result = search_knowledge_base("AI development", "ai_development")
    print(result)
    
    print("\n✅ All systems working!")

if __name__ == "__main__":
    main()
