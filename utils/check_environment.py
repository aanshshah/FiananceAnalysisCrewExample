"""
Check system and environment details
"""
import sys
import platform
import subprocess
import os

print("🔍 System Information")
print("="*60)

# Python version
print(f"Python Version: {sys.version}")
print(f"Python Version Info: {sys.version_info}")
print(f"Platform: {platform.platform()}")
print(f"Machine: {platform.machine()}")

# Virtual environment
print(f"\nVirtual Environment: {'Yes' if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) else 'No'}")
print(f"Python Executable: {sys.executable}")

# Check installed packages
print("\n📦 Key Package Versions:")
print("-"*60)

packages = ['crewai', 'langchain', 'openai', 'pydantic', 'langchain-openai']
for package in packages:
    try:
        module = __import__(package.replace('-', '_'))
        version = getattr(module, '__version__', 'unknown')
        print(f"{package}: {version}")
    except ImportError:
        print(f"{package}: not installed")

print("\n💡 Recommendations:")
if sys.version_info >= (3, 13):
    print("⚠️  You're using Python 3.13 which is very new.")
    print("   Some packages might not be fully compatible yet.")
    print("   Consider using Python 3.10 or 3.11 for better compatibility.")

print("\nTo create a new environment with Python 3.11:")
print("1. Install Python 3.11 if not already installed")
print("2. python3.11 -m venv venv311")
print("3. source venv311/bin/activate")
print("4. pip install -r requirements_updated.txt")
