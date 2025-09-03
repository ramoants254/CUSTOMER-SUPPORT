from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class TriageData(BaseModel):
    """Data structure for triage agent handoffs"""
    intent: str
    confidence: float
    customer_query: str
    extracted_entities: Optional[Dict[str, Any]] = None

class AIDevHandoffData(BaseModel):
    """Data for AI Development specialist handoff"""
    project_type: str  # ml_model, custom_agent, generative_ai, etc.
    technical_level: str  # beginner, intermediate, expert
    specific_need: str
    budget_range: Optional[str] = None

class AutomationHandoffData(BaseModel):
    """Data for Automation specialist handoff"""
    process_type: str  # workflow, rpa, optimization
    industry: Optional[str] = None
    current_tools: Optional[List[str]] = None
    pain_points: Optional[List[str]] = None

class FullStackHandoffData(BaseModel):
    """Data for Full-Stack development handoff"""
    project_type: str  # web_app, api, mobile_app
    tech_preferences: Optional[List[str]] = None
    timeline: Optional[str] = None
    complexity: str  # simple, medium, complex

class CybersecurityHandoffData(BaseModel):
    """Data for Cybersecurity specialist handoff"""
    service_type: str  # audit, penetration_test, compliance, secure_dev
    industry: Optional[str] = None
    compliance_needs: Optional[List[str]] = None
    current_security_level: Optional[str] = None

class EscalationData(BaseModel):
    """Data for human escalation"""
    reason: str
    urgency: str  # low, medium, high, critical
    customer_context: Dict[str, Any]
    conversation_summary: str