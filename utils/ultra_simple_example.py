"""
Ultra-simple working example - No memory, no embeddings, minimal dependencies
"""
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("🚀 Ultra-Simple CrewAI Example")
print("="*60)

# Check API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ Please set OPENAI_API_KEY in .env file")
    exit(1)

try:
    from crewai import Agent, Crew, Task, Process
    from langchain_openai import ChatOpenAI
    
    # Initialize LLM
    llm = ChatOpenAI(
        temperature=0.7,
        model="gpt-3.5-turbo",
        api_key=api_key
    )
    
    # Create a simple agent
    analyst = Agent(
        role='Stock Analyst',
        goal='Provide simple stock analysis',
        backstory='You are a helpful stock analyst.',
        verbose=True,
        llm=llm,
        max_iter=1
    )
    
    # Create a simple task
    company = input("\nEnter a company name (or press Enter for 'Apple'): ").strip() or "Apple"
    
    task = Task(
        description=f"""
        Provide a brief analysis of {company} stock including:
        1. What the company does
        2. Recent performance (general)
        3. Simple buy/hold/sell recommendation
        
        Keep it under 100 words.
        """,
        expected_output="A brief stock analysis",
        agent=analyst
    )
    
    # Create crew with minimal configuration
    crew = Crew(
        agents=[analyst],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
        memory=False,  # No memory
        embedder=None,  # No embeddings
        cache=False,    # No cache
        max_rpm=10
    )
    
    print(f"\n🔍 Analyzing {company}...")
    print("-"*60)
    
    # Run the crew
    result = crew.kickoff()
    
    print("\n" + "="*60)
    print("📊 ANALYSIS RESULT:")
    print("="*60)
    print(result)
    print("\n✅ Analysis complete!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("\nPlease install required packages:")
    print("pip install crewai langchain-openai")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"Error type: {type(e).__name__}")
    
    # If it's an API error, provide helpful info
    if "api" in str(e).lower():
        print("\n💡 API Troubleshooting:")
        print("1. Check your OpenAI API key is valid")
        print("2. Ensure you have API credits")
        print("3. Try regenerating your API key")
