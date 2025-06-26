"""
Quick test to verify CrewAI is working on your system
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("🧪 Testing CrewAI Installation")
print("="*60)
print(f"Python version: {sys.version}")
print("="*60)

# Step 1: Check imports
print("\n1️⃣ Checking imports...")
try:
    import crewai
    print("✅ crewai imported successfully")
except ImportError:
    print("❌ crewai not installed")
    print("   Run: pip install crewai")
    exit(1)

try:
    import langchain_openai
    print("✅ langchain_openai imported successfully")
except ImportError:
    print("❌ langchain_openai not installed")
    print("   Run: pip install langchain-openai")
    exit(1)

# Step 2: Check API key
print("\n2️⃣ Checking API key...")
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")
else:
    print("❌ OPENAI_API_KEY not found in .env")
    exit(1)

# Step 3: Test basic CrewAI functionality
print("\n3️⃣ Testing basic CrewAI...")
try:
    from crewai import Agent, Task, Crew
    from langchain_openai import ChatOpenAI
    
    # Create LLM
    llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")
    
    # Create simple agent
    agent = Agent(
        role="Test Agent",
        goal="Test the system",
        backstory="I am a test agent",
        llm=llm
    )
    
    # Create simple task
    task = Task(
        description="Say 'CrewAI is working!'",
        expected_output="A confirmation message",
        agent=agent
    )
    
    # Create crew
    crew = Crew(agents=[agent], tasks=[task])
    
    print("✅ CrewAI components created successfully")
    
    # Test execution
    print("\n4️⃣ Testing execution...")
    result = crew.kickoff()
    print(f"✅ Result: {result}")
    
    print("\n" + "="*60)
    print("✅ All tests passed! CrewAI is working correctly.")
    print("\nYou can now run:")
    print("  - python crew_no_tools.py")
    print("  - python direct_openai_analysis.py")
    print("  - python example_usage.py")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"   Type: {type(e).__name__}")
    print("\n💡 Try running: chmod +x install_missing.sh && ./install_missing.sh")
