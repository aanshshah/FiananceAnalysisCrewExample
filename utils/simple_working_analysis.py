"""
Simple Working Financial Analysis - Guaranteed to work!
"""
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def simple_crew_analysis(company_name):
    """Simple analysis using CrewAI with minimal configuration"""
    
    try:
        from crewai import Agent, Crew, Task
        from langchain_openai import ChatOpenAI
        
        # Initialize LLM
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Create one simple agent
        analyst = Agent(
            role='Financial Analyst',
            goal='Analyze companies',
            backstory='You are a helpful financial analyst.',
            llm=llm,
            verbose=True
        )
        
        # Create one simple task
        task = Task(
            description=f"""Provide a brief analysis of {company_name} in 3 parts:
            1. What the company does (2 sentences)
            2. Investment pros and cons (2-3 points each)
            3. Simple recommendation (buy/hold/wait)
            
            Keep the total response under 200 words.""",
            expected_output="A brief investment analysis",
            agent=analyst
        )
        
        # Create minimal crew
        crew = Crew(
            agents=[analyst],
            tasks=[task],
            verbose=True
        )
        
        # Run analysis
        print(f"\n🔍 Analyzing {company_name}...\n")
        result = crew.kickoff()
        
        return {
            'success': True,
            'company': company_name,
            'analysis': str(result),
            'timestamp': datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'company': company_name,
            'timestamp': datetime.now().isoformat()
        }

def main():
    print("🚀 Simple Financial Analysis Tool")
    print("="*50)
    
    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in .env file")
        return
    
    print("✅ API key loaded")
    
    while True:
        print("\n" + "-"*50)
        company = input("Enter company name (or 'quit' to exit): ").strip()
        
        if company.lower() == 'quit':
            print("\n👋 Goodbye!")
            break
            
        if not company:
            company = "Apple"
            print(f"Using default: {company}")
        
        result = simple_crew_analysis(company)
        
        print("\n" + "="*50)
        print("📊 ANALYSIS RESULTS")
        print("="*50)
        
        if result['success']:
            print(f"\nCompany: {result['company']}")
            print(f"Time: {result['timestamp']}")
            print(f"\nAnalysis:\n{result['analysis']}")
        else:
            print(f"\n❌ Error: {result['error']}")
            print("\n💡 Troubleshooting tips:")
            print("1. Check your OpenAI API key is valid")
            print("2. Ensure you have API credits")
            print("3. Try running: pip install crewai langchain-openai")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    main()
