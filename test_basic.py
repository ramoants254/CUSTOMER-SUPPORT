from agents import Agent, Runner
from config.settings import settings
import os
import asyncio

# Create a basic agent without tools first
basic_agent = Agent(
    name="Basic Support Agent",
    instructions=f"""You are a customer support agent for {settings.company_name}.

We're a cutting-edge technology company specializing in AI-driven solutions for businesses.

Our services include:
🤖 AI Development - Custom AI agents, ML models, generative AI solutions
⚙️ Automation Solutions - Process automation and workflow optimization
💻 Full-Stack Development - Web applications and API development
🔒 Cybersecurity Services - Security audits and secure development

Starting prices:
- AI Development: From $5,000
- Automation Solutions: From $3,000
- Full-Stack Development: From $4,000
- Cybersecurity Services: From $2,000

Contact: {settings.company_email}
Website: {settings.company_website}

Be helpful and professional. If customers need detailed technical consultation, 
offer to connect them with our specialists."""
)

async def main():
    """Test basic agent functionality"""
    
    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = settings.openai_api_key
    
    print(f"🤖 Welcome to {settings.company_name} Customer Support!")
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("Thank you for contacting Relego AI Solutions! Have a great day! 👋")
                break
                
            if not user_input:
                continue
            
            # Run the conversation with basic agent
            print("🤖 Assistant: ", end="")
            result = await Runner.run(basic_agent, user_input)
            print(result.final_output)
            print()
            
        except KeyboardInterrupt:
            print("\n\nThank you for contacting Relego AI Solutions! Have a great day! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again or contact support@ndezwa.dev for assistance.\n")

if __name__ == "__main__":
    asyncio.run(main())
