# models/customer_data.py
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class CustomerType(str, Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"
    ENTERPRISE = "enterprise"

class LeadStatus(str, Enum):
    NEW = "new"
    QUALIFIED = "qualified"
    CONTACTED = "contacted"
    CONVERTED = "converted"
    LOST = "lost"

class InteractionType(str, Enum):
    INQUIRY = "inquiry"
    SUPPORT = "support"
    SALES = "sales"
    COMPLAINT = "complaint"
    FEEDBACK = "feedback"

class CustomerProfile(BaseModel):
    """Enhanced customer profile with history tracking"""
    customer_id: str
    email: Optional[str] = None
    company_name: Optional[str] = None
    customer_type: CustomerType = CustomerType.INDIVIDUAL
    industry: Optional[str] = None
    company_size: Optional[str] = None
    
    # Preferences
    preferred_services: List[str] = []
    technical_level: str = "beginner"  # beginner, intermediate, expert
    communication_style: str = "professional"  # casual, professional, technical
    
    # History
    total_interactions: int = 0
    last_interaction: Optional[datetime] = None
    previous_inquiries: List[str] = []
    
    # Lead qualification
    lead_status: LeadStatus = LeadStatus.NEW
    lead_score: int = 0
    lead_indicators: List[str] = []
    budget_range: Optional[str] = None
    decision_timeline: Optional[str] = None
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class InteractionRecord(BaseModel):
    """Individual interaction tracking"""
    interaction_id: str
    customer_id: str
    session_id: str
    interaction_type: InteractionType
    service_area: Optional[str] = None
    agent_used: str
    customer_query: str
    agent_response: str
    satisfaction_score: Optional[int] = None
    lead_indicators: List[str] = []
    follow_up_needed: bool = False
    escalated: bool = False
    timestamp: datetime = Field(default_factory=datetime.now)

class SupportTicket(BaseModel):
    """Support ticket for complex issues"""
    ticket_id: str
    customer_id: str
    title: str
    description: str
    priority: str = "medium"  # low, medium, high, critical
    status: str = "open"  # open, in_progress, resolved, closed
    assigned_to: Optional[str] = None
    service_area: str
    created_from_session: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)