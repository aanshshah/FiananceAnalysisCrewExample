#!/usr/bin/env python3
"""
Financial Analysis UI Launcher
Choose which UI version to run
"""

import os
import sys
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("""
╔═══════════════════════════════════════════════════════════════╗
║         🤖 Financial Analysis AI - UI Version Selector        ║
╚═══════════════════════════════════════════════════════════════╝
    """)

def print_menu():
    print("""
Choose your UI version:

1️⃣  Original Version (app.py)
    - Basic chat interface
    - Fixed and stable
    - Simple and functional

2️⃣  Enhanced Version (app_enhanced.py) 
    - Modern purple gradient design
    - 6 preset query templates
    - Rich markdown support
    - Progress tracking & timestamps

3️⃣  Premium Version (app_premium.py)
    - Advanced animated gradients
    - 9 preset templates
    - Charts and data visualization
    - Multi-tab interface

4️⃣  Agent Insights Version (app_agent_insights.py) ⭐ NEW
    - See agent thinking process
    - Color-coded agent cards
    - Timeline view of collaboration
    - 9 preset templates

5️⃣  Ultra Transparent Version (app_ultra_transparent.py) 🔬 NEW
    - Maximum visibility into AI process
    - Detailed agent communications
    - Raw output toggle
    - 12 preset templates
    - Export capabilities

6️⃣  Exit

    """)

def launch_app(app_file):
    """Launch the selected Streamlit app"""
    print(f"\n🚀 Launching {app_file}...")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_file])
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
    except Exception as e:
        print(f"\n❌ Error launching app: {e}")
        print("\nMake sure Streamlit is installed: pip install streamlit")

def main():
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            launch_app('app.py')
        elif choice == '2':
            launch_app('app_enhanced.py')
        elif choice == '3':
            launch_app('app_premium.py')
        elif choice == '4':
            launch_app('app_agent_insights.py')
        elif choice == '5':
            launch_app('app_ultra_transparent.py')
        elif choice == '6':
            print("\n👋 Goodbye!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Check if we're in the right directory
    required_files = ['app.py', 'app_enhanced.py', 'app_premium.py', 
                     'app_agent_insights.py', 'app_ultra_transparent.py']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print("❌ Error: Missing required files:")
        for f in missing_files:
            print(f"   - {f}")
        print("\nMake sure you're in the FiananceAnalysisCrew directory.")
        sys.exit(1)
    
    # Check if Streamlit is installed
    try:
        import streamlit
    except ImportError:
        print("❌ Streamlit is not installed.")
        print("Install it with: pip install streamlit")
        sys.exit(1)
    
    main()
