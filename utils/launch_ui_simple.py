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

1️⃣  Main App (app.py)
    - Fixed callbacks and memory issues
    - Basic chat interface
    - Stable and functional

2️⃣  Streamlit Working App (streamlit_app_working.py)
    - Simple working version
    - No complex features
    - Good for testing

3️⃣  Exit

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
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            if os.path.exists('app.py'):
                launch_app('app.py')
            else:
                print("\n❌ app.py not found!")
                input("\nPress Enter to continue...")
        elif choice == '2':
            if os.path.exists('streamlit_app_working.py'):
                launch_app('streamlit_app_working.py')
            else:
                print("\n❌ streamlit_app_working.py not found!")
                input("\nPress Enter to continue...")
        elif choice == '3':
            print("\n👋 Goodbye!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Check if we're in the right directory
    if not os.path.exists('crew.py'):
        print("❌ Error: crew.py not found.")
        print("Make sure you're in the FiananceAnalysisCrew directory.")
        sys.exit(1)
    
    # Check if Streamlit is installed
    try:
        import streamlit
    except ImportError:
        print("❌ Streamlit is not installed.")
        print("Install it with: pip install streamlit")
        sys.exit(1)
    
    main()
