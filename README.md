# 🤖 Financial Analysis Crew AI - Multi-Agent Investment Assistant

An advanced financial analysis chatbot powered by CrewAI that orchestrates multiple specialized AI agents to provide comprehensive investment insights. Features beautiful UI options with full visibility into AI agent thinking and collaboration.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-0.28+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange.svg)

## ✨ Key Features

### 🤝 Multi-Agent AI System
Three specialized AI agents collaborate to provide comprehensive analysis:
- **🔍 Research Analyst**: Gathers company information and market insights
- **📊 Financial Analyst**: Evaluates financial metrics and growth potential
- **💡 Investment Advisor**: Provides actionable recommendations and risk assessment

### 🎨 Multiple UI Versions
Choose from 5 different interfaces, each with unique features:

1. **Agent Insights UI** ⭐ - See exactly how AI agents think and collaborate
2. **Ultra Transparent UI** 🔬 - Maximum visibility with detailed communications
3. **Enhanced Modern UI** 💜 - Clean design with preset queries
4. **Premium Feature-Rich UI** 💎 - Charts, exports, and advanced features
5. **Original Streamlit UI** 📋 - Simple and functional

### 🚀 Unique Capabilities
- **Agent Communication Visibility**: Watch AI agents' thinking process in real-time
- **Rich Markdown Support**: Beautiful tables, code blocks, and formatted analysis
- **Preset Query Templates**: One-click analysis for common questions (6-12 templates)
- **Interactive Timeline**: See how agents build on each other's work
- **Export Options**: Save analysis as JSON or Markdown
- **Progress Tracking**: Visual indicators showing analysis stages
- **Error Handling**: User-friendly error messages and troubleshooting

## 🖼️ UI Preview

### Agent Insights View
```
┌─────────────────────────────┐
│ 🔍 Research Analyst         │
│ Step 1 of 3                 │
├─────────────────────────────┤
│ I'm researching Apple...    │
│ • Market cap: $3T           │
│ • Main products: iPhone...  │
└─────────────────────────────┘
           ↓
┌─────────────────────────────┐
│ 📊 Financial Analyst        │
│ Step 2 of 3                 │
├─────────────────────────────┤
│ Based on the research...    │
│ • P/E Ratio: 29.5           │
│ • Revenue growth: 5.5%      │
└─────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher (3.11 recommended for best compatibility)
- OpenAI API key
- 1GB free disk space

### Installation

1. **Clone or navigate to the project**:
   ```bash
   cd /Users/aansh/Documents/introspective-diary/FiananceAnalysisCrew
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. **Launch the UI selector** (Easiest):
   ```bash
   python launch_ui.py
   ```

   Or run a specific version directly:
   ```bash
   streamlit run app_agent_insights.py  # ⭐ Recommended
   ```

## 💬 How to Use

### Interactive UI Launcher
```bash
python launch_ui.py
```
Select from 5 different UI versions based on your needs.

### Direct Commands

#### See Agent Thinking (Recommended)
```bash
streamlit run app_agent_insights.py
```
- Watch AI agents collaborate in real-time
- Color-coded agent cards
- 9 preset analysis templates

#### Maximum Transparency
```bash
streamlit run app_ultra_transparent.py
```
- Detailed agent communications
- Raw output toggle
- Export capabilities
- 12 preset templates

#### Command Line Analysis
```bash
python example_usage.py
```
- Full terminal-based analysis
- Detailed output logs
- Great for automation

## 📁 Project Structure

```
FiananceAnalysisCrew/
├── 🎯 Core Files
│   ├── crew.py                     # Main CrewAI agents configuration
│   ├── crew_with_logging.py        # Enhanced crew with communication capture
│   └── requirements.txt            # Python dependencies
│
├── 🎨 UI Versions
│   ├── app.py                      # Original Streamlit interface
│   ├── app_agent_insights.py       # ⭐ Agent thinking visibility
│   ├── app_ultra_transparent.py    # 🔬 Maximum detail view
│   ├── app_enhanced.py             # 💜 Modern clean UI
│   ├── app_premium.py              # 💎 Feature-rich version
│   └── streamlit_app_working.py    # Simple working demo
│
├── 🛠️ Utilities
│   ├── launch_ui.py                # Interactive UI selector
│   ├── example_usage.py            # Command-line example
│   ├── debug_api.py                # API connection tester
│   └── test_crewai.py              # CrewAI functionality test
│
├── 📚 Documentation
│   ├── README.md                   # This file
│   ├── AGENT_COMMUNICATION_GUIDE.md # Agent visibility guide
│   └── UI_COMPLETE_SUMMARY.md      # UI versions comparison
│
└── 🔐 Configuration
    ├── .env.example                # Environment template
    ├── .env                        # Your API keys (git ignored)
    └── config.yaml                 # Application settings
```

## 🎯 UI Version Comparison

| Feature | Original | Enhanced | Premium | Agent Insights ⭐ | Ultra Transparent 🔬 |
|---------|----------|----------|---------|-------------------|---------------------|
| **Preset Queries** | ❌ | 6 | 9 | 9 | 12 |
| **Agent Thinking Visible** | ❌ | ❌ | ❌ | ✅ | ✅ Maximum |
| **Timeline View** | ❌ | ❌ | ❌ | ✅ | ✅ Animated |
| **Rich Markdown** | Basic | ✅ | ✅ | ✅ | ✅ Enhanced |
| **Export Options** | ❌ | ❌ | ✅ | ✅ | ✅ Multi-format |
| **Charts/Graphs** | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Color Themes** | Default | Purple | Rainbow | Professional | Modern |

## 🧠 How It Works

### Agent Collaboration Flow
```
User Query → Research Analyst → Financial Analyst → Investment Advisor → Final Report
                    ↓                    ↓                    ↓
              Gathers Data      Evaluates Metrics    Makes Recommendations
```

### Agent Specializations

**🔍 Research Analyst**
- Company overview and business model
- Market position and competition
- Industry trends and developments

**📊 Financial Analyst**
- Financial health evaluation
- Growth prospects assessment
- Risk and opportunity identification

**💡 Investment Advisor**
- Investment recommendations (Buy/Hold/Sell)
- Risk considerations
- Time horizon guidance

## 🔧 Configuration

### Environment Variables (.env)
```bash
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL_NAME=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.1
```

### Supported Companies
The system recognizes major companies including:
- Tech: Apple, Microsoft, Google, Amazon, Tesla, Meta, NVIDIA
- Finance: JPMorgan, Bank of America, Visa
- Healthcare: Pfizer, Johnson & Johnson
- And many more...

## 🚨 Troubleshooting

### Common Issues

**ModuleNotFoundError**
```bash
# Ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**API Key Issues**
- Verify your OpenAI API key is valid
- Check you have sufficient credits
- Ensure no extra spaces in .env file

**Python Version Issues**
- Use Python 3.11 for best compatibility
- Python 3.13 may have package compatibility issues

### Debug Tools
```bash
python debug_api.py          # Test API connections
python test_crewai.py        # Test CrewAI setup
python diagnose_crewai.py    # Comprehensive diagnostics
```

## 📊 Example Queries

### Preset Templates Include:
- 📈 "Analyze Apple's growth potential"
- ⚖️ "What are Tesla's main investment risks?"
- 🔍 "Compare Microsoft vs Google"
- 💰 "Is Amazon a good value investment?"
- 🤖 "Analyze NVIDIA in the AI boom"
- 📊 "Evaluate Meta's fundamentals"

### Custom Queries:
- "Should I invest in renewable energy stocks?"
- "What's the outlook for banking sector?"
- "Analyze Disney's streaming strategy"

## 🛡️ Important Disclaimers

- **Educational Purpose Only**: This tool is for learning and demonstration
- **Not Financial Advice**: Always consult qualified financial advisors
- **AI Limitations**: Analysis based on training data, not real-time information
- **No Trading Features**: This tool does not execute trades

## 🔐 Security

- API keys stored locally in `.env` (never committed to git)
- No user data collection or storage
- All analysis happens locally
- Consider regenerating API keys after testing

## 🤝 Contributing

Contributions are welcome! Ideas for enhancement:
- Add more specialized agents (Technical Analyst, ESG Analyst)
- Integrate real-time data sources
- Add portfolio analysis features
- Create mobile-responsive versions
- Add more visualization options

## 📝 Version History

- **v4.0** - Added agent communication visibility
- **v3.0** - Multiple UI versions with enhanced features
- **v2.0** - Fixed callbacks and memory issues
- **v1.0** - Initial CrewAI implementation


## 📄 License

This project is for educational purposes. Use at your own discretion.
