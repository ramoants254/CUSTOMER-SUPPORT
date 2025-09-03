import json
import os
from typing import List, Dict, Any
from agents import function_tool

@function_tool
def search_knowledge_base(query: str, category: str = None) -> str:
    """
    Search the company knowledge base for relevant information
    
    Args:
        query: Search query
        category: Optional category filter (ai_development, automation, fullstack, cybersecurity)
    
    Returns:
        Relevant information from knowledge base
    """
    knowledge_files = {
        "ai_development": "data/knowledge_base/ai_development.json",
        "automation": "data/knowledge_base/automation.json", 
        "fullstack": "data/knowledge_base/fullstack.json",
        "cybersecurity": "data/knowledge_base/cybersecurity.json",
        "company": "data/knowledge_base/company_info.json"
    }
    
    results = []
    query_lower = query.lower()
    
    # Determine which files to search
    files_to_search = [knowledge_files[category]] if category and category in knowledge_files else knowledge_files.values()
    
    for file_path in files_to_search:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    
                # Search through FAQs
                if 'faqs' in data:
                    for faq in data['faqs']:
                        if (query_lower in faq.get('question', '').lower() or 
                            query_lower in faq.get('answer', '').lower()):
                            results.append(f"Q: {faq['question']}\nA: {faq['answer']}")
                
                # Search through services
                if 'services' in data:
                    for service in data['services']:
                        if query_lower in service.get('description', '').lower():
                            results.append(f"Service: {service['name']}\n{service['description']}")
                            
            except (json.JSONDecodeError, FileNotFoundError):
                continue
    
    if results:
        return "\n\n".join(results[:3])  # Return top 3 results
    else:
        return "No specific information found in knowledge base."

def get_company_info() -> str:
    """Get general company information"""
    return search_knowledge_base("company overview", "company")