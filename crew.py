"""
Fixed Financial Analysis Crew - Works with current AI knowledge
"""
from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI
import os
from datetime import datetime
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
    llm = None

class FinancialAnalysisCrew:
    def __init__(self):
        self.agents = self._create_agents()
        self.tasks = []
        self.crew = None
        self.intermediate_results = []
    
    def _create_agents(self):
        """Create the financial analysis agents without external tools"""
        
        # Financial Analyst Agent
        financial_analyst = Agent(
            role='Senior Financial Analyst',
            goal='Analyze financial data and market trends to provide investment insights',
            backstory="""You are an experienced financial analyst with expertise in evaluating 
            companies based on available information. You provide balanced, thoughtful analysis 
            based on your training knowledge up to your cutoff date.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
            max_iter=2
        )
        
        # Research Analyst Agent
        research_analyst = Agent(
            role='Investment Research Analyst',
            goal='Provide comprehensive information about companies based on general knowledge',
            backstory="""You are a knowledgeable research analyst who understands company 
            fundamentals, market dynamics, and industry trends based on your training data.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
            max_iter=2
        )
        
        # Investment Advisor Agent
        investment_advisor = Agent(
            role='Senior Investment Advisor',
            goal='Provide actionable investment recommendations based on analysis',
            backstory="""You are a seasoned investment advisor who provides clear, 
            balanced recommendations. You always remind clients that this is educational 
            content and not personalized financial advice.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
            max_iter=2
        )
        
        return {
            'financial_analyst': financial_analyst,
            'research_analyst': research_analyst,
            'investment_advisor': investment_advisor
        }
    
    def create_tasks(self, company_name: str, user_query: str = None):
        """Create tasks for analyzing a specific company"""
        
        # Task 1: Company Research
        research_task = Task(
            description=f"""Based on your training knowledge, provide information about {company_name}:
            1. Company overview and main business segments
            2. Key products, services, and revenue sources
            3. Market position and main competitors
            4. General trends in their industry
            5. Notable strengths and challenges
            
            Note: Use your general knowledge about the company. Be clear about what information 
            you're confident about versus what might have changed since your training cutoff.""",
            expected_output="A comprehensive overview of the company based on general knowledge",
            agent=self.agents['research_analyst']
        )
        
        # Task 2: Financial Analysis
        analysis_task = Task(
            description=f"""Analyze the investment potential of {company_name} based on general principles:
            1. Evaluate the company's business model and competitive advantages
            2. Discuss growth prospects and market opportunities
            3. Identify key risks and challenges
            4. Consider industry trends and market position
            5. Provide a balanced view of the investment case
            
            Base your analysis on fundamental investment principles and the company information provided.""",
            expected_output="A balanced financial analysis highlighting opportunities and risks",
            agent=self.agents['financial_analyst']
        )
        
        # Task 3: Investment Recommendation
        recommendation_task = Task(
            description=f"""Based on the research and analysis of {company_name}, provide:
            1. A general investment perspective (bullish/neutral/bearish)
            2. Key factors supporting this view
            3. Main risks investors should consider
            4. Type of investor this might suit (growth, value, income, etc.)
            5. Important considerations and caveats
            
            {"Additional consideration: " + user_query if user_query else ""}
            
            Remember to note that this is educational content and not personalized investment advice.""",
            expected_output="A thoughtful investment perspective with appropriate disclaimers",
            agent=self.agents['investment_advisor']
        )
        
        self.tasks = [research_task, analysis_task, recommendation_task]
        return self.tasks
    
    def analyze(self, company_name: str, user_query: str = None):
        """Run the financial analysis crew"""
        try:
            # Clear previous results
            self.intermediate_results = []
            
            # Create tasks
            self.create_tasks(company_name, user_query)
            
            # Create and run crew
            self.crew = Crew(
                agents=list(self.agents.values()),
                tasks=self.tasks,
                process=Process.sequential,
                verbose=True,
                memory=False,  # Disable memory to avoid errors
                cache=False,    # Disable cache to avoid errors
                max_rpm=10
            )
            
            print(f"\n🚀 Starting analysis of {company_name}...")
            result = self.crew.kickoff()
            
            # Return final result
            final_result = {
                'company': company_name,
                'query': user_query,
                'timestamp': datetime.now().isoformat(),
                'analysis': str(result),
                'status': 'success'
            }
            
            return final_result
            
        except Exception as e:
            print(f"❌ Error during analysis: {e}")
            return {
                'company': company_name,
                'query': user_query,
                'timestamp': datetime.now().isoformat(),
                'analysis': f"Error occurred: {str(e)}",
                'status': 'error'
            }

# Test the crew if run directly
if __name__ == "__main__":
    print("🧪 Testing Financial Analysis Crew...")
    crew = FinancialAnalysisCrew()
    
    company = input("\nEnter company name (or press Enter for 'Apple'): ").strip() or "Apple"
    
    result = crew.analyze(company)
    
    print("\n" + "="*60)
    print("📊 Analysis Results:")
    print("="*60)
    print(json.dumps(result, indent=2))
