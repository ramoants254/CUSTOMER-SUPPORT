# session_manager.py - Enhanced with Phase 3 Intelligence
from agents import SQLiteSession
from typing import Dict, Optional, List, Any
from models.customer_data import CustomerProfile, InteractionRecord, InteractionType, LeadStatus
import uuid
from datetime import datetime

class CustomerIntelligence:
    """Customer analysis and lead qualification"""
    
    def analyze_intent(self, message: str, customer: CustomerProfile) -> Dict[str, Any]:
        """Analyze customer message for lead indicators"""
        message_lower = message.lower()
        lead_indicators = []
        intent_strength = "low"
        
        # Budget/pricing indicators
        if any(word in message_lower for word in ["budget", "cost", "price", "investment"]):
            lead_indicators.append("budget_inquiry")
            intent_strength = "medium"
        
        # Timeline indicators
        if any(word in message_lower for word in ["when", "timeline", "urgent", "asap"]):
            lead_indicators.append("timeline_mentioned")
            intent_strength = "medium"
        
        # High-intent phrases
        if any(phrase in message_lower for phrase in ["need help", "looking for", "want to"]):
            intent_strength = "high"
        
        # Company indicators
        if any(word in message_lower for word in ["company", "business", "enterprise", "team"]):
            lead_indicators.append("business_inquiry")
        
        return {
            "lead_indicators": lead_indicators,
            "intent_strength": intent_strength,
            "lead_score_boost": len(lead_indicators) * 10
        }
    
    def calculate_lead_score(self, customer: CustomerProfile, interactions: List[InteractionRecord]) -> int:
        """Calculate lead score based on customer data and interactions"""
        score = customer.lead_score
        
        # Customer type scoring
        if customer.customer_type.value == "enterprise":
            score += 30
        elif customer.customer_type.value == "business":
            score += 15
        
        # Interaction-based scoring
        for interaction in interactions:
            score += len(interaction.lead_indicators) * 5
        
        # Frequency bonus
        if len(interactions) > 1:
            score += 10
        
        return min(score, 100)  # Cap at 100

class CustomerSessionManager:
    """Enhanced session manager with customer intelligence"""
    
    def __init__(self, db_path: str = "customer_sessions.db"):
        self.db_path = db_path
        self.active_sessions: Dict[str, SQLiteSession] = {}
        
        # Customer data storage (in production, use real database)
        self.customers: Dict[str, CustomerProfile] = {}
        self.interactions: Dict[str, List[InteractionRecord]] = {}
        self.intelligence = CustomerIntelligence()
    
    def get_or_create_session(self, customer_id: str = None) -> tuple[str, SQLiteSession, CustomerProfile]:
        """Get or create session with customer profile"""
        if customer_id is None:
            customer_id = str(uuid.uuid4())
        
        # Create session if needed
        if customer_id not in self.active_sessions:
            session = SQLiteSession(customer_id, self.db_path)
            self.active_sessions[customer_id] = session
        
        # Get or create customer profile
        if customer_id not in self.customers:
            self.customers[customer_id] = CustomerProfile(customer_id=customer_id)
            self.interactions[customer_id] = []
        
        return customer_id, self.active_sessions[customer_id], self.customers[customer_id]
    
    def record_interaction(self, customer_id: str, user_message: str, agent_response: str, agent_name: str) -> Dict[str, Any]:
        """Record interaction with intelligence analysis"""
        
        customer = self.customers.get(customer_id)
        if not customer:
            return {}
        
        # Analyze customer intent
        analysis = self.intelligence.analyze_intent(user_message, customer)
        
        # Create interaction record
        interaction = InteractionRecord(
            interaction_id=str(uuid.uuid4()),
            customer_id=customer_id,
            session_id=customer_id,
            interaction_type=InteractionType.INQUIRY,
            agent_used=agent_name,
            customer_query=user_message,
            agent_response=agent_response,
            lead_indicators=analysis["lead_indicators"]
        )
        
        # Store interaction
        if customer_id not in self.interactions:
            self.interactions[customer_id] = []
        self.interactions[customer_id].append(interaction)
        
        # Update customer profile
        customer.total_interactions += 1
        customer.last_interaction = datetime.now()
        customer.previous_inquiries.append(user_message[:100])
        customer.previous_inquiries = customer.previous_inquiries[-5:]  # Keep last 5
        customer.lead_indicators.extend(analysis["lead_indicators"])
        
        # Update lead score
        customer.lead_score = self.intelligence.calculate_lead_score(customer, self.interactions[customer_id])
        
        # Update lead status based on score
        if customer.lead_score >= 70:
            customer.lead_status = LeadStatus.QUALIFIED
        elif customer.lead_score >= 40:
            customer.lead_status = LeadStatus.CONTACTED
        
        return {
            "lead_score": customer.lead_score,
            "lead_status": customer.lead_status.value,
            "analysis": analysis,
            "should_escalate": customer.lead_score >= 70 or customer.total_interactions >= 5
        }
    
    def get_customer_analytics(self) -> Dict[str, Any]:
        """Get analytics for all customers"""
        total_customers = len(self.customers)
        qualified_leads = sum(1 for c in self.customers.values() if c.lead_status == LeadStatus.QUALIFIED)
        avg_lead_score = sum(c.lead_score for c in self.customers.values()) / total_customers if total_customers > 0 else 0
        
        return {
            "total_customers": total_customers,
            "qualified_leads": qualified_leads,
            "average_lead_score": round(avg_lead_score, 1),
            "conversion_rate": round((qualified_leads / total_customers * 100), 1) if total_customers > 0 else 0
        }

# Global session manager
session_manager = CustomerSessionManager()