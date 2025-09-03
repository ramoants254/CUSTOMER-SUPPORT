from agents import Runner, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from support_agents.orchestrator import enhanced_triage_agent
from config.settings import settings
from session_manager import session_manager
import os
import asyncio


async def main():
    """Main entry point with session management and guardrails"""
    
    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = settings.openai_api_key
    
    print(f"🤖 Welcome to {settings.company_name} Customer Support!")
    print("🛡️ Protected by advanced security guardrails")
    print("Type 'exit' to quit, 'reset' for new conversation\n")
    
    # Create or get customer session with Phase 3 intelligence
    customer_id, session, customer_profile = session_manager.get_or_create_session()
    print(f"Session ID: {customer_id[:8]}...")
    print(f"👤 Customer Type: {customer_profile.customer_type.value}")
    print(f"📊 Lead Score: {customer_profile.lead_score}\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("Thank you for contacting Relego AI Solutions! Have a great day! 👋")
                break
                
            if user_input.lower() == 'reset':
                print("🔄 Starting new conversation...\n")
                customer_id, session, customer_profile = session_manager.get_or_create_session()
                print(f"New Session ID: {customer_id[:8]}...\n")
                continue
                
            if user_input.lower() == 'analytics':
                analytics = session_manager.get_customer_analytics()
                print(f"📊 Analytics: {analytics['total_customers']} customers, "
                      f"{analytics['qualified_leads']} qualified leads, "
                      f"avg score: {analytics['average_lead_score']}\n")
                continue
                
            if not user_input:
                continue
            
            # Run conversation with session memory and guardrails protection
            print("🤖 Assistant: ", end="")
            
            try:
                result = await Runner.run(enhanced_triage_agent, user_input, session=session)
                print(result.final_output)
                
                # Record interaction with intelligence
                intelligence_data = session_manager.record_interaction(
                    customer_id, user_input, result.final_output, "Enhanced Triage Agent"
                )
                
                # Show intelligence updates for high-value leads
                if intelligence_data.get("lead_score", 0) >= 50:
                    print(f"\n💡 Lead Score: {intelligence_data['lead_score']} | "
                          f"Status: {intelligence_data['lead_status']}")
                    
                    if intelligence_data.get("should_escalate", False):
                        print("🚨 High-value lead - Recommend escalation to sales team")
                        
            except InputGuardrailTripwireTriggered as e:
                # Handle input guardrail violations
                print("\n🛡️ I'm sorry, but I can't process that request.")
                print("Our security systems detected content that violates our usage policies.")
                print("Please ensure your message is:")
                print("• Related to Relego AI Solutions services")
                print("• Appropriate for customer support") 
                print("• Free from malicious content")
                print("\nPlease rephrase your question and try again.")
                
                # Log the incident for security monitoring
                print(f"\n[SECURITY] Input guardrail triggered: {e.guardrail_result.guardrail.get_name()}")
                
            except OutputGuardrailTripwireTriggered as e:
                # Handle output guardrail violations
                print("\n🔄 I apologize, but my response didn't meet our quality standards.")
                print("Let me try again with a better response...")
                
                # Log the incident for quality monitoring
                print(f"\n[QUALITY] Output guardrail triggered: {e.guardrail_result.guardrail.get_name()}")
                
                # Attempt a fallback response
                fallback_response = f"Thank you for your inquiry about {user_input[:50]}{'...' if len(user_input) > 50 else ''}. "
                fallback_response += "I'd be happy to help you with information about Relego AI Solutions' services. "
                fallback_response += "Would you like me to connect you with one of our specialists for personalized assistance?"
                
                print(fallback_response)
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nThank you for contacting Relego AI Solutions! Have a great day! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again or contact support@ndezwa.dev for assistance.\n")


if __name__ == "__main__":
    asyncio.run(main())