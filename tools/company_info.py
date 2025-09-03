from config.settings import settings
from agents import function_tool


@function_tool
def get_company_overview() -> str:
    """Get company overview information"""
    return f"""**About {settings.company_name}**

We're a cutting-edge technology company specializing in AI-driven solutions for businesses.

🎯 **Our Mission**: Transforming businesses through intelligent automation and AI innovation

📧 **Contact**: {settings.company_email}
🌐 **Website**: {settings.company_website}
🕒 **Business Hours**: {settings.business_hours_start} - {settings.business_hours_end} {settings.business_timezone}

**Our Services**:
🤖 AI Development - Custom AI agents, ML models, generative AI solutions
⚙️ Automation Solutions - Process automation and workflow optimization
💻 Full-Stack Development - Web applications and API development
🔒 Cybersecurity Services - Security audits and secure development"""


@function_tool
def get_service_overview(service: str) -> str:
    """Get specific service overview"""
    services = {
        "ai_development": """**AI Development Services**
        
🤖 Custom AI Agents - Intelligent assistants for your business needs
🧠 Machine Learning Models - Predictive analytics and data insights  
💬 Generative AI Solutions - Content creation and automation
🔗 AI Integration - Seamlessly integrate AI into existing systems

Starting from $5,000 for basic implementations.""",

        "automation": """**Automation Solutions**
        
⚙️ Process Automation - Streamline repetitive business processes
🔄 Workflow Optimization - Improve efficiency and reduce manual work
🤖 RPA Implementation - Robotic Process Automation solutions
📊 Analytics Integration - Data-driven automation insights

Starting from $3,000 for process automation.""",

        "fullstack": """**Full-Stack Development**
        
💻 Web Applications - Modern, responsive web solutions
🔌 API Development - Robust backend services and integrations
📱 Mobile-First Design - Optimized for all devices
☁️ Cloud Deployment - Scalable cloud infrastructure

Starting from $4,000 for web applications.""",

        "cybersecurity": """**Cybersecurity Services**
        
🔒 Security Audits - Comprehensive security assessments
🛡️ Penetration Testing - Identify vulnerabilities before attackers do
📋 Compliance Services - GDPR, HIPAA, and industry standards
🔐 Secure Development - Security-first development practices

Starting from $2,000 for security audits."""
    }
    
    return services.get(service, "Service information not available.")


@function_tool
def get_pricing_info() -> str:
    """Get pricing information"""
    return """**Pricing Information**

Our pricing is customized based on your specific needs and project scope.

💼 **Free Consultation** - Initial consultation to understand your requirements
📊 **Custom Quotes** - Tailored pricing based on project complexity
🎯 **Flexible Packages** - One-time projects or ongoing partnerships

**Starting Prices**:
- AI Development: From $5,000
- Automation Solutions: From $3,000  
- Full-Stack Development: From $4,000
- Cybersecurity Services: From $2,000

For accurate quotes, I can connect you with our sales team."""