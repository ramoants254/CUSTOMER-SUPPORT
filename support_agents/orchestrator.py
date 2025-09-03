# support_agents/orchestrator.py
from agents import Agent
from models.customer_data import CustomerType, LeadStatus
from support_agents.ai_development import ai_development_agent
from support_agents.automation import automation_agent
from support_agents.fullstack import fullstack_agent
from support_agents.cybersecurity import cybersecurity_agent
from support_agents.guardrails import TRIAGE_GUARDRAILS
from tools.knowledge_search import search_knowledge_base
from tools.company_info import get_company_overview, get_pricing_info

def classify_intent(message: str) -> tuple[str, float]:
    """Enhanced intent classification"""
    message_lower = message.lower()
    
    # AI Development keywords
    ai_keywords = ["ai", "artificial intelligence", "machine learning", "ml", "model", 
                   "neural network", "deep learning", "nlp", "computer vision", 
                   "generative ai", "chatbot", "llm", "custom agent"]
    if any(keyword in message_lower for keyword in ai_keywords):
        return "ai_development", 0.85
    
    # Automation keywords  
    automation_keywords = ["automation", "automate", "workflow", "process", "rpa", 
                          "optimize", "efficiency", "streamline", "robotic process"]
    if any(keyword in message_lower for keyword in automation_keywords):
        return "automation", 0.85
        
    # Full-stack keywords
    fullstack_keywords = ["website", "web app", "frontend", "backend", "fullstack", 
                         "api", "database", "react", "node", "development"]
    if any(keyword in message_lower for keyword in fullstack_keywords):
        return "fullstack", 0.85
        
    # Cybersecurity keywords
    security_keywords = ["security", "cybersecurity", "vulnerability", "audit", 
                        "penetration", "pentest", "secure", "compliance", "breach"]
    if any(keyword in message_lower for keyword in security_keywords):
        return "cybersecurity", 0.85
    
    # Pricing keywords
    pricing_keywords = ["price", "cost", "pricing", "quote", "budget", "how much", "fee"]
    if any(keyword in message_lower for keyword in pricing_keywords):
        return "pricing", 0.9
        
    # Company info keywords
    company_keywords = ["about", "company", "services", "what do you do", "who are you"]
    if any(keyword in message_lower for keyword in company_keywords):
        return "company_info", 0.8
    
    return "general", 0.5

# Enhanced triage agent with intelligence capabilities and guardrails
enhanced_triage_agent = Agent(
    name="Enhanced Triage Agent",
    instructions="""You are an intelligent customer support agent for Relego AI Solutions with advanced customer analysis capabilities.

Your enhanced role includes:
1. Greet customers warmly and professionally
2. Analyze customer intent and identify lead opportunities  
3. Provide personalized responses based on customer history and type
4. Route specialized questions to appropriate specialist agents
5. Qualify leads and suggest appropriate follow-up actions

Customer Intelligence Features:
- Adjust responses based on customer type (individual/business/enterprise)
- Personalize technical level based on customer expertise
- Identify high-value leads and prioritize accordingly
- Track customer interaction patterns for better service

When you detect high-value customers or qualified leads:
- Prioritize their requests and offer immediate assistance
- Suggest connecting with senior specialists for complex needs
- Provide detailed information and offer consultations

For specialized technical needs, use the appropriate specialist tools.
Always maintain a professional, helpful tone while leveraging customer intelligence.""",
    
    tools=[
        get_company_overview,
        get_pricing_info,
        search_knowledge_base,
        ai_development_agent.as_tool(
            tool_name="consult_ai_specialist",
            tool_description="Get specialized help with AI development, ML models, or custom AI agents"
        ),
        automation_agent.as_tool(
            tool_name="consult_automation_specialist", 
            tool_description="Get specialized help with process automation, RPA, or workflow optimization"
        ),
        fullstack_agent.as_tool(
            tool_name="consult_fullstack_specialist",
            tool_description="Get specialized help with web development, APIs, or full-stack projects"
        ),
        cybersecurity_agent.as_tool(
            tool_name="consult_security_specialist",
            tool_description="Get specialized help with security audits, penetration testing, or cybersecurity"
        )
    ],
    
    # Add guardrails for security and quality control
    input_guardrails=TRIAGE_GUARDRAILS["input_guardrails"],
    output_guardrails=TRIAGE_GUARDRAILS["output_guardrails"]
)


def analyze_customer_context(customer_email: str, message: str) -> dict:
    """
    Analyze customer context for intelligent routing
    """
    # Determine customer type based on email domain
    customer_type = CustomerType.INDIVIDUAL
    if "@" in customer_email:
        domain = customer_email.split("@")[1]
        if any(enterprise in domain.lower() for enterprise in 
               ["microsoft", "google", "amazon", "apple", "ibm", "oracle"]):
            customer_type = CustomerType.ENTERPRISE
        elif not domain.endswith((".gmail.com", ".yahoo.com", ".hotmail.com")):
            customer_type = CustomerType.BUSINESS
    
    # Classify intent
    intent, confidence = classify_intent(message)
    
    # Determine lead potential
    lead_indicators = [
        "budget", "timeline", "implementation", "enterprise", "team",
        "scale", "integration", "custom", "consultation", "proposal"
    ]
    
    lead_score = sum(1 for indicator in lead_indicators 
                    if indicator in message.lower())
    
    if lead_score >= 3:
        lead_status = LeadStatus.HOT
    elif lead_score >= 1:
        lead_status = LeadStatus.WARM
    else:
        lead_status = LeadStatus.COLD
    
    return {
        "customer_type": customer_type,
        "intent": intent,
        "confidence": confidence,
        "lead_status": lead_status,
        "lead_score": lead_score
    }