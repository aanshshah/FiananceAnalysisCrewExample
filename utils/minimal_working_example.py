"""
Minimal working example for Python 3.13 - Version agnostic
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("🚀 Minimal CrewAI Example for Python 3.13")
print("="*60)
print(f"Python version: {sys.version}")
print("="*60)

# Check API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ Please set OPENAI_API_KEY in .env file")
    exit(1)

print("✅ OpenAI API key loaded")

# Try to import and use CrewAI
try:
    print("\n📦 Importing required modules...")
    
    # Import with error handling for different versions
    try:
        from langchain_openai import ChatOpenAI
        print("✅ langchain_openai imported")
    except ImportError:
        print("❌ langchain_openai not found, trying alternative...")
        from langchain.chat_models import ChatOpenAI
    
    from crewai import Agent, Crew, Task
    print("✅ crewai imported")
    
    # Initialize LLM with minimal config
    print("\n🤖 Initializing LLM...")
    llm = ChatOpenAI(
        temperature=0.7,
        api_key=api_key
    )
    print("✅ LLM initialized")
    
    # Create a simple agent without tools
    print("\n👤 Creating agent...")
    agent = Agent(
        role='Analyst',
        goal='Provide simple analysis',
        backstory='You are a helpful analyst.',
        verbose=True,
        llm=llm
    )
    print("✅ Agent created")
    
    # Create a simple task
    print("\n📋 Creating task...")
    task = Task(
        description="Say hello and introduce yourself in one sentence.",
        expected_output="A greeting and introduction",
        agent=agent
    )
    print("✅ Task created")
    
    # Create crew with minimal config
    print("\n🚢 Creating crew...")
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )
    print("✅ Crew created")
    
    # Run the crew
    print("\n🎯 Running crew...")
    print("-"*60)
    result = crew.kickoff()
    print("-"*60)
    
    print(f"\n📊 Result: {result}")
    print("\n✅ Success! CrewAI is working on Python 3.13")
    
    # Now try a more complex example
    print("\n" + "="*60)
    print("🎯 Let's try a stock analysis...")
    print("="*60)
    
    company = input("\nEnter a company name (or press Enter for 'Apple'): ").strip() or "Apple"
    
    analysis_task = Task(
        description=f"Provide a brief 2-3 sentence analysis of {company} as an investment.",
        expected_output="A brief investment analysis",
        agent=agent
    )
    
    analysis_crew = Crew(
        agents=[agent],
        tasks=[analysis_task],
        verbose=True
    )
    
    print(f"\n🔍 Analyzing {company}...")
    print("-"*60)
    analysis_result = analysis_crew.kickoff()
    print("-"*60)
    
    print(f"\n📊 Analysis: {analysis_result}")
    
except ImportError as e:
    print(f"\n❌ Import error: {e}")
    print("\n💡 Please run: chmod +x install_python313.sh && ./install_python313.sh")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print(f"Error type: {type(e).__name__}")
    
    if "api" in str(e).lower() or "key" in str(e).lower():
        print("\n💡 This looks like an API key issue:")
        print("1. Check your OpenAI API key is valid")
        print("2. Ensure you have API credits at https://platform.openai.com/usage")
        print("3. Try regenerating your API key")
    else:
        print("\n💡 Debug info:")
        print(f"Full error: {str(e)}")
