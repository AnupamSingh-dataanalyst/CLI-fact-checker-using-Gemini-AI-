#!/bin/bash

# Simple Fact Checker CLI
# Usage: fact-check "Your claim here"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/fact_checker.py"

# Check if Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo -e "${RED}Error: fact_checker.py not found in $SCRIPT_DIR${NC}"
    exit 1
fi

# Check arguments
if [ $# -eq 0 ]; then
    echo -e "${BLUE}Simple Fact Checker${NC}"
    echo ""
    echo -e "${YELLOW}Usage:${NC} fact-check 'Your claim here'"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo "  fact-check 'The Moon landing happened in 1969'"
    echo "  fact-check 'Python was created by Guido van Rossum'"
    echo "  fact-check 'The Great Wall of China is visible from space'"
    echo ""
    echo -e "${YELLOW}Setup:${NC}"
    echo "  1. Install dependencies: pip3 install google-generativeai requests"
    echo "  2. Set API key: export GEMINI_API_KEY='your-key-here'"
    echo "  3. Or edit fact_checker.py to add your API key"
    exit 1
fi

# Check if required Python packages are installed
python3 -c "import google.generativeai, requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Missing dependencies${NC}"
    echo "Please install: pip3 install google-generativeai requests"
    exit 1
fi

# Check for API key
if [ -z "$GEMINI_API_KEY" ]; then
    echo -e "${YELLOW}Warning: GEMINI_API_KEY not set${NC}"
    echo "Make sure to set your API key in the Python script or environment"
    echo ""
fi

# Get the claim (all arguments joined)
claim="$*"

# Run the fact checker
echo -e "${GREEN}🚀 Starting fact check...${NC}"
echo ""

python3 "$PYTHON_SCRIPT" "$claim"

echo -e "${GREEN}Created by Anupam Singh with AI.${NC}"
echo -e "${BLUE}Fact check complete!${NC}"
