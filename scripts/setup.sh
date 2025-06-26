#!/bin/bash

# Setup script for Financial Analysis Crew AI Chatbot

echo "🚀 Setting up Financial Analysis Crew AI Chatbot..."
echo "=============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Check for .env file
echo ""
if [ ! -f .env ]; then
    echo "📋 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your API keys:"
    echo "   - OPENAI_API_KEY"
    echo "   - SERPER_API_KEY (optional but recommended)"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "=============================================="
echo "✅ Setup complete!"
echo ""
echo "To run the chatbot:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Make sure you've added your API keys to .env"
echo "3. Run: streamlit run app.py"
echo ""
echo "To run the example script:"
echo "python example_usage.py"
echo ""
echo "Happy analyzing! 📈"
