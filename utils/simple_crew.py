"""
Simple Financial Analysis Crew - No memory/embeddings to avoid compatibility issues
"""
from crewai import Agent, Crew, Task, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
import os
from datetime import datetime
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize tools
search_tool = SerperDevTool()

# Initialize LLM
try:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    print("✅ LLM initialized successfully")
except Exception as e:
    print(f"❌ Error initializing LLM: {e}")
    raise

class SimpleFinancialCrew:
    def __init__(self):
        self.create_agents()
    
    def create_agents(self):
        """Create simplified agents without memory"""
        
        # Research Agent
        self.researcher = Agent(
            role='Research Analyst',
            goal='Research company information and market data',
            backstory='Expert at finding and summarizing financial information',
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm
        )
        
        # Analysis Agent  
        self.analyst = Agent(
            role='Financial Analyst',
            goal='Analyze financial data and provide insights',
            backstory='Skilled at interpreting financial metrics and trends',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
        
    def analyze(self, company_name: str):
        """Run simplified analysis"""
        
        # Task 1: Research
        research_task = Task(
            description=f"""Research {company_name} and find:
            1. Current stock price
            2. Recent news (last month)
            3. Basic financial metrics
            Provide a concise summary.""",
            expected_output="Brief research summary with key findings",
            agent=self.researcher
        )
        
        # Task 2: Analysis
        analysis_task = Task(
            description=f"""Based on the research about {company_name}, provide:
            1. Investment outlook (positive/neutral/negative)
            2. Key strengths and risks
            3. Simple recommendation
            Keep it brief and actionable.""",
            expected_output="Short investment analysis with recommendation",
            agent=self.analyst
        )
        
        # Create crew without memory/embeddings
        crew = Crew(
            agents=[self.researcher, self.analyst],
            tasks=[research_task, analysis_task],
            process=Process.sequential,
            verbose=True,
            memory=False,  # Disable memory to avoid RAG errors
            embedder={
                "provider": "openai",
                "config": {
                    "api_key": os.getenv("OPENAI_API_KEY"),
                    "model": "text-embedding-ada-002"
                }
            } if False else None  # Disable embeddings
        )
        
        print(f"\n🚀 Starting analysis of {company_name}...\n")
        
        try:
            result = crew.kickoff()
            return {
                'company': company_name,
                'timestamp': datetime.now().isoformat(),
                'analysis': str(result)
            }
        except Exception as e:
            print(f"❌ Error during analysis: {e}")
            return {
                'company': company_name,
                'timestamp': datetime.now().isoformat(),
                'analysis': f"Error: {str(e)}"
            }

# Test script
if __name__ == "__main__":
    print("🧪 Testing Simple Financial Crew...")
    print("="*60)
    
    crew = SimpleFinancialCrew()
    
    # Test with Apple
    result = crew.analyze("Apple Inc")
    
    print("\n" + "="*60)
    print("📊 Analysis Results:")
    print("="*60)
    print(json.dumps(result, indent=2))
