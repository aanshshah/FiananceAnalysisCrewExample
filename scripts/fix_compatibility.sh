#!/bin/bash

echo "🔧 Fixing CrewAI Compatibility Issues..."
echo "========================================"

# Check if we're in virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Not in virtual environment. Activating..."
    source venv/bin/activate
fi

echo ""
echo "📦 Step 1: Uninstalling conflicting packages..."
pip uninstall -y openai langchain langchain-openai langchain-community crewai crewai-tools chromadb embedchain

echo ""
echo "📦 Step 2: Installing compatible versions..."
pip install --no-cache-dir \
    openai==1.30.1 \
    langchain==0.2.1 \
    langchain-openai==0.1.7 \
    langchain-community==0.2.1 \
    crewai==0.30.11 \
    crewai-tools==0.2.6 \
    pydantic==2.7.1 \
    chromadb==0.4.24

echo ""
echo "🧪 Step 3: Testing the setup..."
python test_setup.py

echo ""
echo "✅ Fix complete! Try running:"
echo "   python simple_crew.py"
echo ""
echo "If you still get errors, try:"
echo "   1. Create a new virtual environment"
echo "   2. Use requirements_updated.txt"
