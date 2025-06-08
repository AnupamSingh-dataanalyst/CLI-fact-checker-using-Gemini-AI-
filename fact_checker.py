#!/usr/bin/env python3
"""
Simple Fact Checker using Gemini API + Wikipedia
For older machines - minimal dependencies
"""

import sys
import json
import requests
import google.generativeai as genai
from datetime import datetime

# Configuration
GEMINI_API_KEY = "YOUR GEMINI API KEY"
WIKI_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

class FactChecker:
    def __init__(self, api_key=None):
        
        genai.configure(api_key= GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def search_wikipedia(self, query):
        """Simple Wikipedia search for basic facts"""
        try:
            # Simple search - just try direct page lookup
            search_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
            response = requests.get(search_url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'title': data.get('title', ''),
                    'extract': data.get('extract', ''),
                    'url': data.get('content_urls', {}).get('desktop', {}).get('page', '')
                }
        except Exception as e:
            print(f"Wikipedia search failed: {e}")
        
        return None
    
    def fact_check_with_gemini(self, claim, wiki_context=None):
        """Use Gemini to fact-check the claim"""
        
        prompt = f"""
Please fact-check this claim: "{claim}"

Instructions:
1. Analyze the claim for factual accuracy
2. Provide a confidence level (High/Medium/Low)
3. Give a brief explanation
4. If the claim involves specific dates, names, or events, be precise

"""
        
        if wiki_context:
            prompt += f"\nAdditional context from Wikipedia:\n{wiki_context['extract']}\n"
        
        prompt += """
Format your response as:
STATUS: [TRUE/FALSE/PARTIALLY TRUE/UNCLEAR]
CONFIDENCE: [High/Medium/Low]
EXPLANATION: [Brief explanation]
"""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error with Gemini API: {e}"
    
    def check_claim(self, claim):
        """Main fact-checking function"""
        print(f"🔍 Checking: {claim}")
        print("=" * 50)
        
        # Try Wikipedia for basic context (optional)
        wiki_result = None
        key_terms = claim.split()[:3]  # First few words as search terms
        if len(key_terms) > 0:
            wiki_query = " ".join(key_terms)
            wiki_result = self.search_wikipedia(wiki_query)
            
            if wiki_result:
                print(f"📚 Found Wikipedia context: {wiki_result['title']}")
        
        # Get Gemini's analysis
        print("🤖 Analyzing with Gemini...")
        analysis = self.fact_check_with_gemini(claim, wiki_result)
        
        print("\n" + "=" * 50)
        print("FACT CHECK RESULT:")
        print("=" * 50)
        print(analysis)
        
        if wiki_result and wiki_result['url']:
            print(f"\n📖 Reference: {wiki_result['url']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fact_checker.py 'Your claim here'")
        print("Example: python3 fact_checker.py 'The Moon landing happened in 1969'")
        sys.exit(1)
    
    claim = " ".join(sys.argv[1:])
    
    # Initialize fact checker
    checker = FactChecker()
    
    # Check the claim
    checker.check_claim(claim)

if __name__ == "__main__":
    main()
