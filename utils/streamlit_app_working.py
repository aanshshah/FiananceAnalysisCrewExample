"""
Streamlit Financial Analysis App - Simplified and Working
"""
import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Financial Analysis Assistant",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Financial Analysis Assistant")
st.markdown("Multi-agent AI analysis powered by CrewAI")

# Check setup
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("⚠️ OPENAI_API_KEY not found in .env file!")
    st.stop()

# Try to import CrewAI
try:
    from crewai import Agent, Crew, Task
    from langchain_openai import ChatOpenAI
    crew_available = True
except ImportError as e:
    crew_available = False
    st.error(f"CrewAI not properly installed: {e}")
    st.info("Run: pip install crewai langchain-openai")

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Analysis Request")
    
    company = st.text_input(
        "Enter company name:",
        placeholder="e.g., Apple, Tesla, Microsoft"
    )
    
    analyze_button = st.button("🔍 Analyze", type="primary", disabled=not crew_available)
    
    if analyze_button and company:
        with st.spinner(f"Analyzing {company}..."):
            try:
                # Initialize LLM
                llm = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    api_key=api_key,
                    temperature=0.7
                )
                
                # Create agents
                agents = []
                
                # Research Agent
                researcher = Agent(
                    role='Research Analyst',
                    goal='Gather company information',
                    backstory='Expert at analyzing companies',
                    llm=llm
                )
                agents.append(researcher)
                
                # Financial Analyst
                analyst = Agent(
                    role='Financial Analyst',
                    goal='Evaluate investment potential',
                    backstory='Skilled at financial analysis',
                    llm=llm
                )
                agents.append(analyst)
                
                # Create tasks
                tasks = []
                
                research_task = Task(
                    description=f"Provide a brief overview of {company}: what they do, market position, and recent trends.",
                    agent=researcher
                )
                tasks.append(research_task)
                
                analysis_task = Task(
                    description=f"Analyze {company} as an investment: pros, cons, and recommendation.",
                    agent=analyst
                )
                tasks.append(analysis_task)
                
                # Create and run crew
                crew = Crew(
                    agents=agents,
                    tasks=tasks,
                    verbose=False
                )
                
                result = crew.kickoff()
                
                # Display results
                st.success("✅ Analysis Complete!")
                
                st.markdown("### 📊 Analysis Results")
                st.markdown(f"**Company:** {company}")
                st.markdown(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
                
                st.markdown("### 📝 Detailed Analysis")
                st.write(str(result))
                
                st.info("💡 This is AI-generated analysis for educational purposes only, not financial advice.")
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")
                st.info("Try running: python simple_working_analysis.py for debugging")

with col2:
    st.header("📚 How It Works")
    st.markdown("""
    This app uses **CrewAI** to coordinate multiple AI agents:
    
    1. **Research Analyst** 🔍
       - Gathers company information
       - Identifies key business areas
    
    2. **Financial Analyst** 📊
       - Evaluates investment potential
       - Provides recommendations
    
    Each agent contributes their expertise to create comprehensive analysis.
    """)
    
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Enter well-known company names
    - Analysis takes 15-30 seconds
    - Results are based on AI's training data
    """)

# Footer
st.markdown("---")
st.markdown("🤖 Powered by CrewAI and OpenAI")

# Sidebar status
with st.sidebar:
    st.header("System Status")
    
    if api_key:
        st.success("✅ API Key Loaded")
    else:
        st.error("❌ API Key Missing")
    
    if crew_available:
        st.success("✅ CrewAI Ready")
    else:
        st.error("❌ CrewAI Not Ready")
    
    st.markdown("### 🛠️ Quick Fixes")
    st.code("""
# If CrewAI not working:
pip install crewai
pip install langchain-openai

# Test with:
python simple_working_analysis.py
    """)
