#!/bin/bash

echo "🔧 Installing Missing Packages for Python 3.13"
echo "============================================="

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Please activate your virtual environment first:"
    echo "   source venv/bin/activate"
    exit 1
fi

echo ""
echo "📦 Installing crewai-tools and dependencies..."

# Upgrade pip first
pip install --upgrade pip

# Install packages one by one
echo ""
echo "1️⃣ Installing openai..."
pip install openai

echo ""
echo "2️⃣ Installing langchain packages..."
pip install langchain langchain-openai langchain-community

echo ""
echo "3️⃣ Installing crewai..."
pip install crewai

echo ""
echo "4️⃣ Installing crewai-tools..."
pip install crewai-tools

echo ""
echo "5️⃣ Installing other dependencies..."
pip install python-dotenv requests beautifulsoup4

echo ""
echo "📋 Installed versions:"
echo "====================="
pip list | grep -E "(crewai|langchain|openai)" || echo "Check with: pip list"

echo ""
echo "✅ Installation complete!"
echo ""
echo "🎯 Now try these in order:"
echo "   1. python crew_no_tools.py     (works without web tools)"
echo "   2. python direct_openai_analysis.py  (no CrewAI needed)"
echo "   3. python minimal_working_example.py  (basic CrewAI test)"
