# Relego AI Solutions - Customer Support Agent

An intelligent, multi-agent customer support system built with OpenAI Agents SDK, featuring advanced customer intelligence, session management, and comprehensive security guardrails.

## 🚀 Features

### 🤖 Multi-Agent Architecture
- **Triage Agent**: Intelligent customer routing and lead qualification
- **AI Development Specialist**: Custom AI solutions and machine learning consulting
- **Automation Specialist**: Process automation and RPA services
- **Full-Stack Specialist**: Web development and API solutions
- **Cybersecurity Specialist**: Security audits and compliance services

### 🧠 Customer Intelligence (Phase 3)
- **Lead Scoring**: Automatic qualification and scoring (0-100)
- **Customer Profiling**: Individual, Business, Enterprise classification
- **Interaction Tracking**: Complete conversation history and analytics
- **Real-time Analytics**: Customer insights and conversion metrics
- **Smart Escalation**: Automatic high-value lead detection

### 🛡️ Security Guardrails (Phase 4)
- **Input Protection**: Blocks malicious content, injection attempts, inappropriate requests
- **Output Quality Control**: Ensures professional tone and response quality
- **Business Relevance**: Filters off-topic queries (homework, unrelated content)
- **PII Detection**: Prevents sensitive information leakage
- **Threat Assessment**: AI-powered security analysis

### 📊 Session Management (Phase 2)
- **Persistent Memory**: SQLite-based conversation storage
- **Customer Profiles**: Detailed customer data and interaction history
- **Multi-session Support**: Handle multiple customers simultaneously
- **Session Analytics**: Performance metrics and usage statistics

## 🏗️ Architecture

```
Customer Input → Security Guardrails → Triage Agent → Specialist Agents → Response
                      ↓                      ↓              ↓              ↓
               Threat Detection      Intent Analysis   Expert Knowledge   Quality Control
               Business Validation   Lead Scoring     Service Delivery   Professional Tone
```

## 📦 Installation

### Prerequisites
- Python 3.12+
- OpenAI API Key
- Virtual environment (recommended)

### Setup

1. **Clone and Navigate**
   ```bash
   cd Customer-Support
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   - Set your OpenAI API key in `config/settings.py`
   - Or export as environment variable: `export OPENAI_API_KEY="your-key-here"`

## 🚀 Usage

### Basic Usage

```bash
# Activate virtual environment
source env/bin/activate

# Run the customer support system
python3 main.py
```

### Interactive Commands

- `hello` - Start a conversation
- `analytics` - View customer analytics
- `reset` - Start new conversation
- `exit` or `quit` - End session

### Example Interactions

```
You: Hi, I'm interested in your AI development services for my company
🤖 Assistant: Hello! Thank you for reaching out to Relego AI Solutions...

You: We need custom AI agents for our enterprise with a $500k budget
📊 Intelligence Update:
   • Lead Score: 75
   • Lead Status: qualified
   🚨 ESCALATION RECOMMENDED - High-value lead detected!
```

## 🧪 Testing

### Run Guardrails Test Suite
```bash
python3 test_guardrails.py
```

Choose from:
1. **Automated Test Suite** - Tests security, quality, and business relevance
2. **Interactive Testing** - Manual testing with real-time feedback

### Test Basic Functionality
```bash
python3 test_basic.py
```

## 📁 Project Structure

```
Customer-Support/
├── main.py                    # Main application entry point
├── session_manager.py         # Enhanced session management with intelligence
├── analytics.py              # Customer analytics and reporting
├── config/                   # Configuration settings
│   ├── settings.py           # Application settings
│   └── __init__.py
├── support_agents/           # AI agent implementations
│   ├── orchestrator.py       # Main triage agent with guardrails
│   ├── guardrails.py         # Security and quality guardrails
│   ├── ai_development.py     # AI specialist agent
│   ├── automation.py         # Automation specialist agent
│   ├── fullstack.py          # Full-stack specialist agent
│   └── cybersecurity.py      # Security specialist agent
├── models/                   # Data models
│   ├── customer_data.py      # Customer profiles and interaction data
│   └── handoff_data.py       # Agent handoff data structures
├── tools/                    # Agent tools and utilities
│   ├── knowledge_search.py   # Knowledge base search
│   └── company_info.py       # Company information tools
├── data/                     # Data storage
│   └── knowledge_base/       # Service-specific knowledge files
├── tests/                    # Test suites
│   ├── test_basic.py         # Basic functionality tests
│   └── test_guardrails.py    # Guardrails security tests
└── requirements.txt          # Python dependencies
```

## 🔧 Configuration

### Customer Intelligence Settings
```python
# Adjust lead scoring thresholds
LEAD_SCORE_QUALIFIED = 70    # Qualified lead threshold
LEAD_SCORE_CONTACTED = 40    # Contacted lead threshold
ESCALATION_INTERACTIONS = 5   # Auto-escalate after X interactions
```

### Guardrails Configuration
```python
# Enable/disable specific guardrails
SECURITY_GUARDRAILS = True
BUSINESS_GUARDRAILS = True
QUALITY_GUARDRAILS = True
PROFESSIONAL_TONE = True
```

## 📊 Analytics Dashboard

The system provides real-time analytics including:

- **Total Customers**: Number of unique customer interactions
- **Qualified Leads**: High-value prospects (lead score ≥ 70)
- **Average Lead Score**: Overall lead quality metric
- **Conversion Rate**: Percentage of qualified leads
- **Interaction Patterns**: Customer behavior analysis

## 🛡️ Security Features

### Input Guardrails
- Malicious pattern detection
- SQL injection prevention
- Social engineering blocking
- PII detection and protection

### Output Guardrails
- Professional tone enforcement
- Sensitive information filtering
- Quality assurance checks
- Brand consistency validation

## 🤝 Contributing

### Development Guidelines
1. Follow OpenAI Agents SDK best practices
2. Maintain clean, documented code
3. Add tests for new features
4. Update documentation accordingly

### Testing New Features
```bash
# Test individual components
python3 -m pytest tests/

# Test guardrails specifically
python3 test_guardrails.py

# Integration testing
python3 test_basic.py
```

## 📄 License

This project is proprietary software developed for Relego AI Solutions.

## 👨‍💻 Developer

**Tony Ndezwa**  
Senior AI Engineer  
Relego AI Solutions

---

## 🏆 Project Phases

### ✅ Phase 1: Basic Agent Implementation
- Core agent functionality
- Basic conversation handling
- Agent tool integration

### ✅ Phase 2: Session Management
- SQLite session persistence
- Customer data storage
- Multi-session support

### ✅ Phase 3: Customer Intelligence
- Lead scoring algorithms
- Customer profiling
- Real-time analytics
- Smart escalation

### ✅ Phase 4: Security Guardrails
- Comprehensive input validation
- Output quality control
- Business relevance filtering
- Enterprise-grade security

---

## 📞 Support

For technical support or questions about this customer support system, please contact the development team at Relego AI Solutions.

**System Status**: Production Ready ✅  
**Version**: 4.0 (All Phases Complete)  
**Last Updated**: September 2025
