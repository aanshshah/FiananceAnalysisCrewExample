"""
Enhanced Financial Analysis Crew with Agent Communication Visibility
"""
from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI
import os
from datetime import datetime
import json
from dotenv import load_dotenv
import sys
from io import StringIO

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

class FinancialAnalysisCrewWithLogging:
    def __init__(self):
        self.agents = self._create_agents()
        self.agent_logs = []
        self.captured_output = []
        
    def _create_agents(self):
        """Create the financial analysis agents with enhanced visibility"""
        
        # Financial Analyst Agent
        financial_analyst = Agent(
            role='Senior Financial Analyst',
            goal='Analyze financial data and market trends to provide investment insights',
            backstory="""You are an experienced financial analyst with expertise in evaluating 
            companies based on available information. You provide balanced, thoughtful analysis 
            based on your training knowledge up to your cutoff date. Always explain your reasoning.""",
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
            fundamentals, market dynamics, and industry trends based on your training data.
            Always start by acknowledging what you're researching and your approach.""",
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
            balanced recommendations. You always explain your reasoning and remind clients 
            that this is educational content and not personalized financial advice.""",
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
            description=f"""As the Research Analyst, research {company_name} and provide:

1. **Company Overview**: What does {company_name} do? Main products and services?
2. **Market Position**: Where does {company_name} stand in their industry?
3. **Key Strengths**: What are {company_name}'s competitive advantages?
4. **Recent Developments**: Any notable trends or changes in their business?

Start your response with: "🔍 Research Analyst here. I'm researching {company_name}..."
Explain your findings clearly and note any limitations in your knowledge.""",
            expected_output="A comprehensive research report with clear explanations",
            agent=self.agents['research_analyst']
        )
        
        # Task 2: Financial Analysis
        analysis_task = Task(
            description=f"""As the Financial Analyst, analyze {company_name}'s investment potential:

1. **Financial Health**: Evaluate the company's financial stability
2. **Growth Prospects**: Assess future growth potential
3. **Risk Factors**: Identify key risks and challenges
4. **Valuation**: Comment on whether the company might be fairly valued

Start your response with: "📊 Financial Analyst here. Based on the research..."
Explain your analytical process and reasoning.""",
            expected_output="A detailed financial analysis with clear reasoning",
            agent=self.agents['financial_analyst']
        )
        
        # Task 3: Investment Recommendation
        recommendation_task = Task(
            description=f"""As the Investment Advisor, provide recommendations for {company_name}:

1. **Investment Stance**: Bullish, Neutral, or Bearish?
2. **Key Rationale**: Top 3 reasons for your recommendation
3. **Risk Considerations**: What should investors watch out for?
4. **Time Horizon**: Short-term vs long-term perspective
5. **Action Items**: Specific suggestions for investors

Start with: "💡 Investment Advisor here. After reviewing the analysis..."
{f'Also address: {user_query}' if user_query else ''}

Remember to note this is educational content only.""",
            expected_output="Clear investment recommendations with rationale",
            agent=self.agents['investment_advisor']
        )
        
        return [research_task, analysis_task, recommendation_task]
    
    def capture_agent_output(self, output_stream):
        """Capture and parse agent outputs"""
        output = output_stream.getvalue()
        lines = output.split('\n')
        
        agent_messages = []
        current_agent = None
        current_message = []
        
        for line in lines:
            # Detect agent headers
            if "Research Analyst here" in line:
                if current_agent and current_message:
                    agent_messages.append({
                        'agent': current_agent,
                        'message': '\n'.join(current_message)
                    })
                current_agent = "Research Analyst"
                current_message = [line]
            elif "Financial Analyst here" in line:
                if current_agent and current_message:
                    agent_messages.append({
                        'agent': current_agent,
                        'message': '\n'.join(current_message)
                    })
                current_agent = "Financial Analyst"
                current_message = [line]
            elif "Investment Advisor here" in line:
                if current_agent and current_message:
                    agent_messages.append({
                        'agent': current_agent,
                        'message': '\n'.join(current_message)
                    })
                current_agent = "Investment Advisor"
                current_message = [line]
            elif current_agent and line.strip():
                current_message.append(line)
        
        # Add final message
        if current_agent and current_message:
            agent_messages.append({
                'agent': current_agent,
                'message': '\n'.join(current_message)
            })
        
        return agent_messages
    
    def analyze(self, company_name: str, user_query: str = None):
        """Run the financial analysis crew with output capture"""
        try:
            # Clear previous logs
            self.agent_logs = []
            
            # Create tasks
            tasks = self.create_tasks(company_name, user_query)
            
            # Create crew
            crew = Crew(
                agents=list(self.agents.values()),
                tasks=tasks,
                process=Process.sequential,
                verbose=True,
                memory=False,
                cache=False,
                max_rpm=10
            )
            
            print(f"\n🚀 Starting analysis of {company_name}...")
            
            # Capture stdout to get agent outputs
            old_stdout = sys.stdout
            sys.stdout = captured_output = StringIO()
            
            try:
                result = crew.kickoff()
                
                # Restore stdout
                sys.stdout = old_stdout
                
                # Parse captured output
                agent_messages = self.capture_agent_output(captured_output)
                
                # Structure the result with agent communications
                final_result = {
                    'company': company_name,
                    'query': user_query,
                    'timestamp': datetime.now().isoformat(),
                    'analysis': str(result),
                    'agent_communications': agent_messages,
                    'status': 'success'
                }
                
                return final_result
                
            finally:
                # Always restore stdout
                sys.stdout = old_stdout
                
        except Exception as e:
            print(f"❌ Error during analysis: {e}")
            return {
                'company': company_name,
                'query': user_query,
                'timestamp': datetime.now().isoformat(),
                'analysis': f"Error occurred: {str(e)}",
                'agent_communications': [],
                'status': 'error'
            }
