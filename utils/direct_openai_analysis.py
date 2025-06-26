"""
Direct OpenAI Financial Analysis - No CrewAI needed
Works with any Python version!
"""
import os
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables
load_dotenv()

def analyze_company(company_name):
    """Analyze a company using OpenAI directly"""
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "❌ Please set OPENAI_API_KEY in .env file"
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        print(f"\n🔍 Analyzing {company_name}...")
        print("="*60)
        
        # Simulate multi-agent analysis with different prompts
        agents_prompts = [
            {
                "role": "Research Analyst",
                "prompt": f"As a research analyst, provide a brief overview of {company_name} including what they do, recent news, and market position. Keep it under 100 words."
            },
            {
                "role": "Financial Analyst", 
                "prompt": f"As a financial analyst, evaluate {company_name}'s financial health, growth prospects, and key risks. Keep it under 100 words."
            },
            {
                "role": "Investment Advisor",
                "prompt": f"As an investment advisor, provide a buy/hold/sell recommendation for {company_name} with brief reasoning. Keep it under 100 words."
            }
        ]
        
        results = []
        
        for agent in agents_prompts:
            print(f"\n🤖 {agent['role']} working...")
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a professional {agent['role']}."},
                    {"role": "user", "content": agent['prompt']}
                ],
                temperature=0.7,
                max_tokens=150
            )
            
            result = response.choices[0].message.content
            results.append({
                "agent": agent['role'],
                "analysis": result
            })
            
            print(f"✅ {agent['role']} complete")
            print(f"   {result[:80]}...")
        
        return results
        
    except Exception as e:
        return f"❌ Error: {str(e)}"

def main():
    print("🤖 Financial Analysis Assistant (Direct OpenAI)")
    print("="*60)
    print("This works without CrewAI - using OpenAI directly!")
    print("="*60)
    
    while True:
        company = input("\n💼 Enter company name (or 'quit' to exit): ").strip()
        
        if company.lower() == 'quit':
            print("\n👋 Goodbye!")
            break
        
        if not company:
            company = "Apple"
            print(f"📌 Using default: {company}")
        
        results = analyze_company(company)
        
        if isinstance(results, str):
            print(results)
        else:
            print(f"\n📊 Complete Analysis for {company}")
            print("="*60)
            
            for i, result in enumerate(results, 1):
                print(f"\n{i}. {result['agent']}")
                print("-"*40)
                print(result['analysis'])
            
            # Save results
            filename = f"analysis_{company.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump({
                    "company": company,
                    "timestamp": datetime.now().isoformat(),
                    "analysis": results
                }, f, indent=2)
            
            print(f"\n💾 Results saved to: {filename}")
            print("\n✨ This demonstrates multi-agent collaboration without CrewAI!")

if __name__ == "__main__":
    main()
