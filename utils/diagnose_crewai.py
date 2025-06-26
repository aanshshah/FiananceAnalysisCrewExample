"""
Diagnose CrewAI Issues
"""
import os
import sys
from dotenv import load_dotenv

load_dotenv()

print("🔍 CrewAI Diagnostic Tool")
print("="*60)
print(f"Python: {sys.version}")
print(f"Working Directory: {os.getcwd()}")
print("="*60)

# Check packages
print("\n📦 Package Versions:")
packages_to_check = ['crewai', 'langchain', 'langchain_openai', 'openai', 'pydantic']

for package in packages_to_check:
    try:
        module = __import__(package.replace('-', '_'))
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {package}: {version}")
    except ImportError:
        print(f"❌ {package}: not installed")

# Check API key
print("\n🔑 API Key Check:")
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"✅ OPENAI_API_KEY: {api_key[:10]}...{api_key[-4:]}")
else:
    print("❌ OPENAI_API_KEY: not found")

# Test basic CrewAI functionality
print("\n🧪 Testing CrewAI Components:")

try:
    from crewai import Agent, Task, Crew
    print("✅ Basic imports successful")
    
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(api_key=api_key)
    print("✅ LLM created")
    
    # Test with minimal agent
    agent = Agent(
        role="Test",
        goal="Test",
        backstory="Test",
        llm=llm
    )
    print("✅ Agent created")
    
    # Test with minimal task
    task = Task(
        description="Say hello",
        agent=agent
    )
    print("✅ Task created")
    
    # Test crew creation
    crew = Crew(agents=[agent], tasks=[task])
    print("✅ Crew created")
    
    # Test if we can get version info
    try:
        import crewai
        if hasattr(crewai, '__version__'):
            print(f"\n📌 CrewAI Version: {crewai.__version__}")
        
        # Check for known issues
        print("\n⚠️  Known Issues:")
        print("1. Task callbacks might fail with certain CrewAI versions")
        print("2. Memory/cache features can cause errors")
        print("3. Some tool integrations are version-sensitive")
        
    except:
        pass
    
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"   Type: {type(e).__name__}")

print("\n💡 Recommendations:")
print("1. Use simple configurations without memory/cache")
print("2. Avoid task callbacks if they cause errors")
print("3. Use the latest stable versions of all packages")
print("4. Run: python simple_working_analysis.py for a minimal working example")
