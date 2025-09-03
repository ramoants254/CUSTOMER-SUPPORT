from session_manager import session_manager
from typing import Dict, Any
from datetime import datetime

def generate_analytics_report() -> str:
    """Generate simple analytics report"""
    
    analytics = session_manager.get_customer_analytics()
    
    report = f"""
📊 RELEGO AI CUSTOMER SUPPORT ANALYTICS
📅 Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}

📈 OVERVIEW:
• Total Customers: {analytics['total_customers']}
• Qualified Leads: {analytics['qualified_leads']}
• Average Lead Score: {analytics['average_lead_score']}
• Conversion Rate: {analytics['conversion_rate']}%

💡 HIGH-VALUE CUSTOMERS:
"""
    
    # Add high-value customer details
    high_value_customers = [
        customer for customer in session_manager.customers.values()
        if customer.lead_score >= 70
    ]
    
    if high_value_customers:
        for customer in high_value_customers:
            report += f"• {customer.customer_id[:8]}: Score {customer.lead_score} ({customer.lead_status.value})\n"
    else:
        report += "• No high-value leads currently\n"
    
    report += f"""
🔥 RECOMMENDATIONS:
"""
    
    if analytics['qualified_leads'] > 0:
        report += f"• Follow up with {analytics['qualified_leads']} qualified leads immediately\n"
    
    if analytics['conversion_rate'] < 10:
        report += "• Improve lead qualification process (conversion rate below 10%)\n"
    
    if analytics['average_lead_score'] < 30:
        report += "• Focus on attracting higher-quality leads\n"
    
    return report
