"""
Minimal test to verify CrewAI setup
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("🧪 Testing CrewAI Setup...")
print("="*60)

# Check environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY not found in environment!")
    exit(1)

print(f"✅ OpenAI API Key loaded: {api_key[:10]}...{api_key[-4:]}")

# Test OpenAI directly
print("\n1️⃣ Testing OpenAI Connection...")
try:
    from langchain_openai import ChatOpenAI
    
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.1,
        api_key=api_key
    )
    
    # Test with a simple prompt
    result = llm.invoke("Say 'Hello, CrewAI is working!'")
    print(f"✅ OpenAI Response: {result.content}")
except Exception as e:
    print(f"❌ OpenAI Error: {e}")
    print("\nTroubleshooting:")
    print("1. Check if your API key is valid")
    print("2. Ensure you have API credits")
    print("3. Try regenerating your API key")
    exit(1)

# Test CrewAI imports
print("\n2️⃣ Testing CrewAI Imports...")
try:
    from crewai import Agent, Crew, Task
    print("✅ CrewAI imports successful")
except Exception as e:
    print(f"❌ CrewAI import error: {e}")
    exit(1)

# Test creating a simple agent
print("\n3️⃣ Testing Simple Agent Creation...")
try:
    test_agent = Agent(
        role='Test Agent',
        goal='Test the setup',
        backstory='I am a test agent',
        llm=llm,
        verbose=True
    )
    print("✅ Agent created successfully")
except Exception as e:
    print(f"❌ Agent creation error: {e}")
    exit(1)

# Test creating a simple task
print("\n4️⃣ Testing Simple Task Creation...")
try:
    test_task = Task(
        description="Say hello",
        expected_output="A greeting",
        agent=test_agent
    )
    print("✅ Task created successfully")
except Exception as e:
    print(f"❌ Task creation error: {e}")
    exit(1)

# Test running a minimal crew
print("\n5️⃣ Testing Minimal Crew Execution...")
try:
    test_crew = Crew(
        agents=[test_agent],
        tasks=[test_task],
        verbose=True
    )
    
    result = test_crew.kickoff()
    print(f"✅ Crew execution successful!")
    print(f"Result: {result}")
except Exception as e:
    print(f"❌ Crew execution error: {e}")
    print(f"\nError type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n" + "="*60)
print("✅ All tests passed! Your CrewAI setup is working correctly.")
print("\nYou can now run:")
print("  python example_usage.py")
