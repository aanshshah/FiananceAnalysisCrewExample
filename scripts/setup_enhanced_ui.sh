#!/bin/bash

echo "🎨 Setting up Enhanced UI Dependencies"
echo "====================================="

# Check if in virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Please activate your virtual environment first:"
    echo "   source venv/bin/activate"
    exit 1
fi

echo ""
echo "📦 Installing additional UI dependencies..."

# Install visualization libraries for premium version
pip install plotly pandas --quiet

echo "✅ Plotly installed (for charts)"
echo "✅ Pandas installed (for data tables)"

echo ""
echo "🎯 Quick Start Guide:"
echo "===================="
echo ""
echo "1. Launch UI selector:"
echo "   python launch_ui.py"
echo ""
echo "2. Or run directly:"
echo "   streamlit run app_enhanced.py  # Recommended"
echo "   streamlit run app_premium.py   # All features"
echo ""
echo "3. View on mobile:"
echo "   Open browser to http://YOUR_IP:8501"
echo ""
echo "✅ Setup complete! Enjoy your enhanced UI!"
