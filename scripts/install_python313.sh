#!/bin/bash

echo "🔧 Installing CrewAI for Python 3.13..."
echo "========================================"

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "🐍 Python version: $python_version"

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Not in virtual environment. Please activate it first:"
    echo "   source venv/bin/activate"
    exit 1
fi

echo ""
echo "📦 Installing latest compatible versions..."

# Install packages one by one to handle failures gracefully
pip install --upgrade pip

echo "Installing OpenAI..."
pip install openai

echo "Installing LangChain..."
pip install langchain

echo "Installing LangChain OpenAI..."
pip install langchain-openai

echo "Installing LangChain Community..."
pip install langchain-community

echo "Installing CrewAI (latest version)..."
pip install crewai

echo "Installing additional tools..."
pip install python-dotenv requests beautifulsoup4 streamlit

echo ""
echo "📋 Installed versions:"
pip list | grep -E "(crewai|langchain|openai)"

echo ""
echo "✅ Installation complete!"
echo ""
echo "Try running:"
echo "   python minimal_working_example.py"
