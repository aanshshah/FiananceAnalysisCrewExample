#!/bin/bash

echo "🔧 Python Version Solution"
echo "=========================="
echo ""
echo "You're using Python 3.13, which is too new for many packages."
echo "Here are your options:"
echo ""

# Check if Python 3.11 is available
if command -v python3.11 &> /dev/null; then
    echo "✅ Python 3.11 is available! Let's use it:"
    echo ""
    echo "Run these commands:"
    echo "  cd /Users/aansh/Documents/introspective-diary/FiananceAnalysisCrew"
    echo "  python3.11 -m venv venv311"
    echo "  source venv311/bin/activate"
    echo "  pip install -r requirements.txt"
    echo "  python example_usage.py"
else
    echo "❌ Python 3.11 not found."
    echo ""
    echo "Option 1: Install Python 3.11"
    echo "  brew install python@3.11"
    echo ""
    echo "Option 2: Use current Python 3.13 with latest packages"
    echo "  chmod +x install_python313.sh"
    echo "  ./install_python313.sh"
    echo "  python minimal_working_example.py"
fi

echo ""
echo "Current Python version:"
python3 --version

echo ""
echo "Available Python versions on your system:"
ls -la /usr/local/bin/python* 2>/dev/null | grep -E "python[0-9]" || echo "Check /opt/homebrew/bin/ for M1/M2 Macs"
ls -la /opt/homebrew/bin/python* 2>/dev/null | grep -E "python[0-9]"
