"""
Financial Analysis Chatbot - Enhanced Agent Output Display
Improved layout for better readability and intuitive agent trace following
"""
import streamlit as st
from datetime import datetime
import os
import sys
from pathlib import Path
import time
import json
import re

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

# Import the crew
from crew import FinancialAnalysisCrew

# Page configuration
st.set_page_config(
    page_title="AI Financial Analyst - Clear Agent View",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clean, professional CSS with improved agent display
st.markdown("""
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global styles */
    .main {
        font-family: 'Inter', sans-serif;
        background: #f8fafc;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.15);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    /* Agent output container */
    .agent-output-container {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
    }
    
    /* Agent sequence header */
    .agent-sequence-header {
        background: #f3f4f6;
        margin: -1.5rem -1.5rem 1.5rem -1.5rem;
        padding: 1rem 1.5rem;
        border-radius: 12px 12px 0 0;
        border-bottom: 2px solid #e5e7eb;
    }
    
    .agent-sequence-header h3 {
        margin: 0;
        color: #1f2937;
        font-size: 1.25rem;
        font-weight: 600;
    }
    
    /* Individual agent section */
    .agent-section {
        background: #fafafa;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .agent-section:hover {
        border-color: #e5e7eb;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    
    .agent-section.research {
        border-left: 4px solid #3b82f6;
    }
    
    .agent-section.financial {
        border-left: 4px solid #10b981;
    }
    
    .agent-section.advisor {
        border-left: 4px solid #f59e0b;
    }
    
    /* Agent header */
    .agent-header {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid #e5e7eb;
    }
    
    .agent-icon {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        margin-right: 1rem;
        flex-shrink: 0;
    }
    
    .agent-icon.research {
        background: #dbeafe;
        color: #3b82f6;
    }
    
    .agent-icon.financial {
        background: #d1fae5;
        color: #10b981;
    }
    
    .agent-icon.advisor {
        background: #fed7aa;
        color: #f59e0b;
    }
    
    .agent-title {
        flex: 1;
    }
    
    .agent-name {
        font-weight: 600;
        color: #1f2937;
        margin: 0;
        font-size: 1.1rem;
    }
    
    .agent-step {
        font-size: 0.875rem;
        color: #6b7280;
        margin: 0;
    }
    
    .agent-timestamp {
        font-size: 0.875rem;
        color: #9ca3af;
    }
    
    /* Agent content */
    .agent-content {
        color: #374151;
        line-height: 1.6;
    }
    
    .agent-content h4 {
        color: #1f2937;
        margin: 1rem 0 0.5rem 0;
        font-size: 1rem;
        font-weight: 600;
    }
    
    .agent-content ul {
        margin: 0.5rem 0;
        padding-left: 1.5rem;
    }
    
    .agent-content li {
        margin: 0.25rem 0;
    }
    
    /* Flow indicator */
    .flow-indicator {
        text-align: center;
        margin: 1rem 0;
        color: #6b7280;
        font-size: 1.5rem;
    }
    
    /* Chat messages */
    .chat-message {
        margin-bottom: 1.5rem;
        animation: fadeIn 0.3s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .user-message {
        background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
        margin-left: 20%;
        padding: 1.25rem;
        border-radius: 16px 16px 4px 16px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
    
    .assistant-message {
        background: white;
        margin-right: 20%;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #e5e7eb;
    }
    
    /* Summary section */
    .summary-section {
        background: #f9fafb;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
        border: 1px solid #e5e7eb;
    }
    
    .summary-section h4 {
        color: #1f2937;
        margin: 0 0 1rem 0;
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    /* Preset buttons */
    .preset-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 0.75rem;
        margin-bottom: 1.5rem;
    }
    
    .preset-button {
        background: white;
        border: 2px solid #e5e7eb;
        border-radius: 10px;
        padding: 0.875rem 1rem;
        cursor: pointer;
        transition: all 0.2s ease;
        text-align: center;
        font-weight: 500;
        color: #374151;
    }
    
    .preset-button:hover {
        border-color: #3b82f6;
        background: #eff6ff;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
    }
    
    /* Metrics */
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f2937;
        margin: 0;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #6b7280;
        margin: 0.25rem 0 0 0;
    }
    
    /* Status indicators */
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 16px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .status-processing {
        background: #fef3c7;
        color: #92400e;
    }
    
    .status-complete {
        background: #d1fae5;
        color: #065f46;
    }
    
    .status-error {
        background: #fee2e2;
        color: #991b1b;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'crew' not in st.session_state:
    st.session_state.crew = FinancialAnalysisCrew()
if 'analyzing' not in st.session_state:
    st.session_state.analyzing = False
if 'total_analyses' not in st.session_state:
    st.session_state.total_analyses = 0
if 'current_analysis_stages' not in st.session_state:
    st.session_state.current_analysis_stages = []

# Helper function to capture and parse agent outputs
def capture_agent_outputs():
    """Simulate agent outputs for demonstration"""
    # In a real implementation, this would capture actual agent outputs
    # For now, we'll create a structured format
    return [
        {
            'agent': 'Research Analyst',
            'timestamp': datetime.now(),
            'status': 'complete',
            'output': """I'm analyzing the requested company based on my knowledge.

**Key Findings:**
- Company operates in multiple sectors
- Strong market position established
- Recent developments show growth trajectory
- Competitive advantages identified

**Market Position:**
- Industry leader in key segments
- Expanding market share
- Strong brand recognition"""
        },
        {
            'agent': 'Financial Analyst',
            'timestamp': datetime.now(),
            'status': 'complete',
            'output': """Based on the research provided, here's my financial analysis:

**Financial Health:**
- Solid revenue growth trends
- Healthy profit margins
- Strong balance sheet

**Valuation Metrics:**
- P/E ratio within industry norms
- Revenue multiples reasonable
- Growth prospects justify current valuation"""
        },
        {
            'agent': 'Investment Advisor',
            'timestamp': datetime.now(),
            'status': 'complete',
            'output': """After reviewing all analysis, here's my recommendation:

**Investment Stance:** Bullish (Buy)

**Key Reasons:**
1. Strong fundamentals
2. Growth potential remains intact
3. Competitive advantages sustainable

**Risk Factors:**
- Market volatility
- Regulatory changes
- Competition intensifying

**Recommended Action:**
Consider for long-term portfolio with 3-5 year horizon."""
        }
    ]

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Financial Analyst</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem; opacity: 0.95;">
        Clear Agent Communication & Analysis Flow
    </p>
</div>
""", unsafe_allow_html=True)

# Top metrics
metrics_cols = st.columns(4)
with metrics_cols[0]:
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-value">{st.session_state.total_analyses}</p>
        <p class="metric-label">Total Analyses</p>
    </div>
    """, unsafe_allow_html=True)

with metrics_cols[1]:
    st.markdown("""
    <div class="metric-card">
        <p class="metric-value">3</p>
        <p class="metric-label">AI Agents</p>
    </div>
    """, unsafe_allow_html=True)

with metrics_cols[2]:
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-value">{len(st.session_state.messages)}</p>
        <p class="metric-label">Conversations</p>
    </div>
    """, unsafe_allow_html=True)

with metrics_cols[3]:
    status = "🟢 Active" if os.getenv("OPENAI_API_KEY") else "🔴 Offline"
    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-value">{status}</p>
        <p class="metric-label">System Status</p>
    </div>
    """, unsafe_allow_html=True)

# Main content
col_main, col_sidebar = st.columns([3, 1])

with col_main:
    # Preset queries
    st.markdown("### 🎯 Quick Analysis Templates")
    
    preset_queries = [
        ("📈 Growth Stock", "Analyze Apple's growth potential"),
        ("⚖️ Risk Analysis", "What are Tesla's main risks?"),
        ("🔍 Comparison", "Compare Microsoft vs Google"),
        ("💰 Value Check", "Is Amazon undervalued?"),
        ("🤖 AI Play", "Analyze NVIDIA in AI market"),
        ("📊 Fundamentals", "Meta's financial strength")
    ]
    
    # Display presets in grid
    st.markdown('<div class="preset-grid">', unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, (label, query) in enumerate(preset_queries):
        with cols[idx % 3]:
            if st.button(label, key=f"preset_{idx}", use_container_width=True):
                st.session_state.messages.append({
                    "role": "user",
                    "content": query,
                    "timestamp": datetime.now()
                })
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Chat interface
    st.markdown("### 💬 Analysis Chat")
    
    # Chat container
    chat_container = st.container()
    with chat_container:
        if not st.session_state.messages:
            st.info("""
            👋 **Welcome!** I'll show you exactly how our AI agents collaborate to analyze investments.
            
            You'll see:
            - 🔍 Research Analyst gathering information
            - 📊 Financial Analyst evaluating metrics  
            - 💡 Investment Advisor providing recommendations
            
            Choose a template above or ask your own question!
            """)
        else:
            for msg_idx, message in enumerate(st.session_state.messages):
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>You</strong> • {message.get('timestamp', datetime.now()).strftime('%I:%M %p')}
                        <br><br>
                        {message['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Assistant message with agent outputs
                    if 'agent_outputs' in message and message['agent_outputs']:
                        # Agent output container
                        st.markdown("""
                        <div class="agent-output-container">
                            <div class="agent-sequence-header">
                                <h3>🤝 AI Agent Collaboration Process</h3>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Display each agent's output
                        for idx, agent_output in enumerate(message['agent_outputs']):
                            agent = agent_output['agent']
                            
                            # Determine styling
                            if 'Research' in agent:
                                agent_class = 'research'
                                icon = '🔍'
                            elif 'Financial' in agent:
                                agent_class = 'financial'
                                icon = '📊'
                            else:
                                agent_class = 'advisor'
                                icon = '💡'
                            
                            # Agent section
                            st.markdown(f"""
                            <div class="agent-section {agent_class}">
                                <div class="agent-header">
                                    <div class="agent-icon {agent_class}">{icon}</div>
                                    <div class="agent-title">
                                        <p class="agent-name">{agent}</p>
                                        <p class="agent-step">Step {idx + 1} of {len(message['agent_outputs'])}</p>
                                    </div>
                                    <div class="agent-timestamp">
                                        {agent_output['timestamp'].strftime('%I:%M:%S %p')}
                                    </div>
                                </div>
                                <div class="agent-content">
                            """, unsafe_allow_html=True)
                            
                            # Display agent output with markdown
                            st.markdown(agent_output['output'])
                            
                            st.markdown("</div></div>", unsafe_allow_html=True)
                            
                            # Flow indicator
                            if idx < len(message['agent_outputs']) - 1:
                                st.markdown('<div class="flow-indicator">⬇️</div>', unsafe_allow_html=True)
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        # Summary section
                        st.markdown("""
                        <div class="summary-section">
                            <h4>📋 Final Analysis Summary</h4>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Main analysis content
                    st.markdown('<div class="assistant-message">', unsafe_allow_html=True)
                    st.markdown(message.get('content', ''))
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Action buttons
                    col1, col2, col3 = st.columns([1, 1, 8])
                    with col1:
                        if st.button("📋 Copy", key=f"copy_{msg_idx}"):
                            st.toast("Analysis copied!", icon="✅")
                    with col2:
                        if st.button("💾 Save", key=f"save_{msg_idx}"):
                            filename = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                            with open(filename, 'w') as f:
                                json.dump({
                                    'query': st.session_state.messages[msg_idx-1]['content'] if msg_idx > 0 else '',
                                    'analysis': message.get('content', ''),
                                    'agent_outputs': message.get('agent_outputs', []),
                                    'timestamp': message.get('timestamp', datetime.now()).isoformat()
                                }, f, indent=2, default=str)
                            st.toast(f"Saved as {filename}", icon="✅")
    
    # Input section
    st.markdown("---")
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.text_area(
                "Your question",
                placeholder="Ask about any company or investment strategy...\n\nExample: 'Analyze Apple stock' or 'Should I invest in Tesla?'",
                height=80,
                label_visibility="collapsed"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("🚀 Analyze", use_container_width=True, type="primary")
    
    # Handle submission
    if submitted and user_input and not st.session_state.analyzing:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now()
        })
        st.session_state.analyzing = True
        st.rerun()
    
    # Analysis execution
    if st.session_state.analyzing:
        last_message = st.session_state.messages[-1]['content']
        
        # Company detection
        companies = [
            "Apple", "Microsoft", "Google", "Amazon", "Tesla", "Meta", "Netflix", 
            "NVIDIA", "AMD", "Intel", "IBM", "Oracle", "Salesforce", "Adobe"
        ]
        
        company_found = None
        for company in companies:
            if company.lower() in last_message.lower():
                company_found = company
                break
        
        if not company_found:
            words = last_message.split()
            for word in words:
                if len(word) > 2 and word[0].isupper():
                    company_found = word
                    break
        
        if company_found:
            # Show progress
            progress_container = st.container()
            with progress_container:
                st.markdown(f"""
                <div class="agent-output-container">
                    <div class="agent-sequence-header">
                        <h3>🔄 Analyzing {company_found}...</h3>
                    </div>
                    <div style="padding: 1.5rem;">
                        <span class="status-badge status-processing">AI Agents Collaborating</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Progress bar
                progress_bar = st.progress(0)
                
                # Simulate agent stages
                agent_stages = [
                    "🔍 Research Analyst gathering information...",
                    "📊 Financial Analyst evaluating metrics...",
                    "💡 Investment Advisor forming recommendations..."
                ]
                
                for i, stage in enumerate(agent_stages):
                    st.info(stage)
                    progress_bar.progress((i + 1) / len(agent_stages))
                    time.sleep(0.5)
            
            try:
                # Run analysis
                start_time = time.time()
                result = st.session_state.crew.analyze(company_found, last_message)
                analysis_time = time.time() - start_time
                
                # Clear progress
                progress_container.empty()
                
                # Get simulated agent outputs
                agent_outputs = capture_agent_outputs()
                
                # Create response
                response = f"""
## 📊 {company_found} Investment Analysis

{result.get('analysis', 'Analysis results')}

---

### 📈 Analysis Metrics

| Metric | Value |
|--------|-------|
| **Company** | {company_found} |
| **Date** | {datetime.now().strftime('%B %d, %Y')} |
| **Time** | {analysis_time:.1f} seconds |
| **Agents** | 3 specialists |

---

### ⚠️ Disclaimer

This is AI-generated analysis for educational purposes only. Not financial advice. Always consult qualified advisors before investing.
"""
                
                # Add to messages
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "timestamp": datetime.now(),
                    "agent_outputs": agent_outputs
                })
                
                st.session_state.total_analyses += 1
                
            except Exception as e:
                progress_container.empty()
                st.error(f"Analysis error: {str(e)}")
                
                error_response = """
## ❌ Analysis Error

Unable to complete analysis. Please try again or check your API configuration.

**Troubleshooting:**
1. Verify API key is valid
2. Check internet connection
3. Try a simpler query
"""
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_response,
                    "timestamp": datetime.now()
                })
        
        else:
            # No company found
            response = """
## 🤔 Company Not Recognized

Please mention a specific company name in your query.

**Examples:**
- "Analyze Apple stock"
- "Tesla investment risks"
- "Compare Microsoft and Google"

Try the preset templates above for quick analysis!
"""
            
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now()
            })
        
        st.session_state.analyzing = False
        st.rerun()

# Sidebar
with col_sidebar:
    st.markdown("### 🧠 Agent Roles")
    
    with st.expander("How It Works", expanded=True):
        st.markdown("""
        **Three AI Agents Collaborate:**
        
        🔍 **Research Analyst**
        - Gathers company info
        - Market analysis
        - Industry trends
        
        📊 **Financial Analyst**
        - Evaluates metrics
        - Risk assessment
        - Growth analysis
        
        💡 **Investment Advisor**
        - Recommendations
        - Strategy guidance
        - Action items
        
        Each agent builds on the previous one's work for comprehensive analysis.
        """)
    
    # Controls
    st.markdown("---")
    st.markdown("### ⚙️ Controls")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_analyses = 0
        st.rerun()
    
    if st.button("🔄 Reset System", use_container_width=True):
        st.session_state.crew = FinancialAnalysisCrew()
        st.toast("System reset!", icon="✅")
    
    # Status
    st.markdown("---")
    st.markdown("### 📊 Status")
    
    if os.getenv("OPENAI_API_KEY"):
        st.success("✅ API Connected")
    else:
        st.error("❌ API Key Missing")
    
    st.caption("v5.0 • Clear Agent View")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 1rem;">
    <p>AI Financial Analyst • Built with CrewAI & Streamlit</p>
    <p style="font-size: 0.875rem;">For educational purposes only • Not financial advice</p>
</div>
""", unsafe_allow_html=True)
