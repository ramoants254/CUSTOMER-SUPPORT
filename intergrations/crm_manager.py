# integrations/crm_manager.py
from models.customer_data import CustomerProfile, InteractionRecord, SupportTicket
from typing import Dict, Any, Optional, List
import uuid
from datetime import datetime

class CRMManager:
    """Manages customer data and integrations"""
    
    def __init__(self):
        # In-memory storage for demo (replace with actual database)
        self.customers: Dict[str, CustomerProfile] = {}
        self.interactions: Dict[str, List[InteractionRecord]] = {}
        self.tickets: Dict[str, SupportTicket] = {}
    
    def get_or_create_customer(self, session_id: str, initial_data: Dict[str, Any] = None) -> CustomerProfile:
        """Get existing customer or create new profile"""
        
        # Try to find existing customer by session or email
        customer_id = session_id  # Using session_id as customer_id for demo
        
        if customer_id in self.customers:
            return self.customers[customer_id]
        
        # Create new customer
        customer_data = {
            "customer_id": customer_id,
            **(initial_data or {})
        }
        
        customer = CustomerProfile(**customer_data)
        self.customers[customer_id] = customer
        self.interactions[customer_id] = []
        
        return customer
    
    def update_customer(self, customer_id: str, updates: Dict[str, Any]) -> CustomerProfile:
        """Update customer profile"""
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            for key, value in updates.items():
                if hasattr(customer, key):
                    setattr(customer, key, value)
            customer.updated_at = datetime.now()
            return customer
        raise ValueError(f"Customer {customer_id} not found")
    
    def record_interaction(self, interaction: InteractionRecord):
        """Record customer interaction"""
        customer_id = interaction.customer_id
        if customer_id not in self.interactions:
            self.interactions[customer_id] = []
        
        self.interactions[customer_id].append(interaction)
        
        # Update customer stats
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            customer.total_interactions += 1
            customer.last_interaction = interaction.timestamp
            customer.previous_inquiries.append(interaction.customer_query[:100])
            # Keep only last 10 inquiries
            customer.previous_inquiries = customer.previous_inquiries[-10:]
    
    def get_customer_history(self, customer_id: str) -> List[InteractionRecord]:
        """Get customer interaction history"""
        return self.interactions.get(customer_id, [])
    
    def create_support_ticket(self, customer_id: str, title: str, description: str, 
                            priority: str = "medium", service_area: str = "general") -> SupportTicket:
        """Create support ticket for escalation"""
        ticket_id = str(uuid.uuid4())
        
        ticket = SupportTicket(
            ticket_id=ticket_id,
            customer_id=customer_id,
            title=title,
            description=description,
            priority=priority,
            service_area=service_area,
            created_from_session=customer_id  # Using customer_id as session for demo
        )
        
        self.tickets[ticket_id] = ticket
        return ticket
    
    def get_customer_tickets(self, customer_id: str) -> List[SupportTicket]:
        """Get all tickets for customer"""
        return [ticket for ticket in self.tickets.values() 
                if ticket.customer_id == customer_id]
    
    def generate_analytics(self) -> Dict[str, Any]:
        """Generate analytics report"""
        total_customers = len(self.customers)
        total_interactions = sum(len(interactions) for interactions in self.interactions.values())
        total_tickets = len(self.tickets)
        
        # Lead statistics
        qualified_leads = sum(1 for customer in self.customers.values() 
                            if customer.lead_status.value in ["qualified", "contacted"])
        
        return {
            "total_customers": total_customers,
            "total_interactions": total_interactions,
            "total_tickets": total_tickets,
            "qualified_leads": qualified_leads,
            "conversion_rate": (qualified_leads / total_customers * 100) if total_customers > 0 else 0,
            "avg_interactions_per_customer": total_interactions / total_customers if total_customers > 0 else 0
        }

# Global CRM manager
crm_manager = CRMManager()