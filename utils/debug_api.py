"""
Debug script to test API connections
"""
import os
from dotenv import load_dotenv
import openai
import requests

# Load environment variables
load_dotenv()

print("🔍 Debugging API Connections...")
print("="*60)

# Check OpenAI API Key
openai_key = os.getenv("OPENAI_API_KEY")
if openai_key:
    print(f"✅ OpenAI API Key found: {openai_key[:10]}...{openai_key[-4:]}")
    
    # Test OpenAI connection
    print("\n📡 Testing OpenAI API connection...")
    try:
        from openai import OpenAI
        client = OpenAI(api_key=openai_key)
        
        # Try a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=10
        )
        print("✅ OpenAI API connection successful!")
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"❌ OpenAI API error: {str(e)}")
        print("\nPossible issues:")
        print("- Invalid API key")
        print("- API key doesn't have access to the model")
        print("- Network connectivity issues")
else:
    print("❌ OpenAI API Key not found in environment!")

print("\n" + "="*60)

# Check Serper API Key
serper_key = os.getenv("SERPER_API_KEY")
if serper_key:
    print(f"✅ Serper API Key found: {serper_key[:10]}...{serper_key[-4:]}")
    
    # Test Serper connection
    print("\n📡 Testing Serper API connection...")
    try:
        headers = {
            'X-API-KEY': serper_key,
            'Content-Type': 'application/json'
        }
        data = {
            'q': 'test query'
        }
        response = requests.post(
            'https://google.serper.dev/search',
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            print("✅ Serper API connection successful!")
        else:
            print(f"❌ Serper API error: Status code {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Serper API error: {str(e)}")
else:
    print("⚠️  Serper API Key not found (optional but recommended)")

print("\n" + "="*60)
print("\n📋 Environment Summary:")
print(f"- Python version: {os.sys.version.split()[0]}")
print(f"- Working directory: {os.getcwd()}")
print(f"- .env file exists: {os.path.exists('.env')}")

# Check if we can import required packages
print("\n📦 Package Import Test:")
try:
    import crewai
    print(f"✅ crewai version: {crewai.__version__ if hasattr(crewai, '__version__') else 'unknown'}")
except ImportError as e:
    print(f"❌ crewai import failed: {e}")

try:
    import langchain
    print(f"✅ langchain version: {langchain.__version__ if hasattr(langchain, '__version__') else 'unknown'}")
except ImportError as e:
    print(f"❌ langchain import failed: {e}")

print("\n💡 Next Steps:")
print("1. If OpenAI API failed, check your API key is valid")
print("2. Make sure you're using the correct model name")
print("3. Try regenerating your API key if needed")
print("4. Ensure you have sufficient API credits")
