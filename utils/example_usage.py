"""
Example script showing how to use the Financial Analysis Crew directly
This demonstrates what happens under the hood in the chatbot
"""
import os
from dotenv import load_dotenv
from crew import FinancialAnalysisCrew
import json
from datetime import datetime

# Load environment variables
load_dotenv()

def analyze_company(company_name: str, query: str = None):
    """
    Analyze a company using the Financial Analysis Crew
    """
    print(f"\n{'='*60}")
    print(f"Starting Financial Analysis for: {company_name}")
    print(f"{'='*60}\n")
    
    # Initialize the crew
    crew = FinancialAnalysisCrew()
    
    # Run the analysis
    print("🚀 Launching AI Agents...\n")
    result = crew.analyze(company_name, query)
    
    # Display results
    print(f"\n{'='*60}")
    print("📊 FINAL ANALYSIS RESULTS")
    print(f"{'='*60}\n")
    
    print(f"Company: {result['company']}")
    print(f"Analysis completed at: {result['timestamp']}")
    
    if result['query']:
        print(f"User Query: {result['query']}\n")
    
    print("\n📈 Full Analysis:")
    print("-" * 40)
    print(result['analysis'])
    
    # Note about intermediate steps being disabled
    print(f"\n\n{'='*60}")
    print("ℹ️  Note: Intermediate step tracking has been disabled")
    print("    to improve stability. The analysis above shows")
    print("    the final collaborative result from all agents.")
    print(f"{'='*60}")
    
    # Save to file
    output_file = f"analysis_{company_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n✅ Full results saved to: {output_file}")

def main():
    """
    Main function to demonstrate the crew in action
    """
    print("\n🤖 Financial Analysis Crew - Direct Usage Example")
    print("This script shows what happens under the hood of the chatbot\n")
    
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key")
        return
    
    if not os.getenv("SERPER_API_KEY"):
        print("⚠️  Warning: SERPER_API_KEY not found")
        print("Web search capabilities will be limited")
        print("Get a free API key at https://serper.dev/\n")
    
    # Example analyses
    examples = [
        {
            "company": "Apple",
            "query": "Should I buy Apple stock for long-term investment?"
        },
        {
            "company": "Tesla",
            "query": "What are the main risks of investing in Tesla?"
        },
        {
            "company": "Microsoft",
            "query": None  # General analysis without specific question
        }
    ]
    
    print("Choose an analysis to run:")
    for i, example in enumerate(examples, 1):
        query_text = example['query'] if example['query'] else "General analysis"
        print(f"{i}. {example['company']} - {query_text}")
    
    choice = input("\nEnter your choice (1-3) or type a company name: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(examples):
        example = examples[int(choice) - 1]
        analyze_company(example['company'], example['query'])
    else:
        # Custom company
        company = choice
        query = input(f"Any specific question about {company}? (Press Enter for general analysis): ").strip()
        analyze_company(company, query if query else None)

if __name__ == "__main__":
    main()
