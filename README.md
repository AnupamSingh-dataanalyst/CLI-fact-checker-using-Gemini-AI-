# CLI-fact-checker-using-Gemini-AI
# 🔍 Free Fact Checker CLI- OSNIT

> **A weekend project that rivals expensive paid fact-checking APIs!**

A simple, fast, and **completely free** command-line fact-checker that combines Google's Gemini AI with Wikipedia for accurate fact verification. Built as an alternative to costly services like Perplexity Sonar.

![Demo](https://img.shields.io/badge/Status-Working-brightgreen) ![Python](https://img.shields.io/badge/Python-3.12+-blue) ![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange) ![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🚀 **Lightning Fast** - Get fact-checks in seconds
- 🧠 **AI-Powered** - Leverages Google's latest Gemini 1.5 Flash model
- 📚 **Wikipedia Integration** - Adds context from reliable sources
- 🎨 **Beautiful CLI** - Colorful output with confidence levels
- 🛡️ **Privacy-First** - No data collection, runs locally

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/free-fact-checker.git
cd free-fact-checker

# Install dependencies
pip3 install google-generativeai requests

# Get your free Gemini API key from https://aistudio.google.com/app/apikey
# Edit fact_checker.py and add your key

# Make executable
chmod +x fact-check.sh

# Start fact-checking!
./fact-check.sh "The Moon landing happened in 1969"
```

## 📸 Sample Output

```
🚀 Starting fact check...

🔍 Checking: The Great Wall of China is visible from space with naked eye
==================================================
📚 Found Wikipedia context: Great Wall of China
🤖 Analyzing with Gemini...

==================================================
FACT CHECK RESULT:
==================================================
STATUS: FALSE
CONFIDENCE: High
EXPLANATION: This is a persistent myth but factually incorrect. The Great Wall of China is NOT visible from space with the naked eye. NASA has confirmed this multiple times. While the wall is long, it's only about 4-6 meters wide, making it impossible to see from space without telescopic aid.

📖 Reference: https://en.wikipedia.org/wiki/Great_Wall_of_China

Fact check complete!
```

## 💡 Why This Beats Paid Alternatives

| Feature | Free Fact Checker | Perplexity Sonar Pro | Other Paid APIs |
|---------|-------------------|----------------------|-----------------|
| **Cost** | ✅ FREE | ❌ $20/month | ❌ $50-200/month |
| **Speed** | ✅ 2-3 seconds | ✅ 2-4 seconds | ⚠️ 5-10 seconds |
| **Accuracy** | ✅ High (Gemini AI) | ✅ High | ⚠️ Varies |
| **Privacy** | ✅ Local execution | ❌ Cloud-based | ❌ Cloud-based |
| **Customization** | ✅ Full control | ❌ Limited | ❌ Limited |
| **Offline Capability** | ⚠️ API required | ❌ No | ❌ No |

## 🛠️ Installation

### Prerequisites
- Python 3.8+ (tested on 3.12)
- Linux/macOS (Windows with WSL)
- Internet connection
- Free Google AI Studio account

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/free-fact-checker.git
   cd free-fact-checker
   ```

2. **Install Python dependencies**
   ```bash
   pip3 install google-generativeai requests
   ```

3. **Get your free Gemini API key**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Click "Create API Key"
   - Copy the key

4. **Configure the API key**
   ```bash
   # Edit the Python script
   nano fact_checker.py
   
   # Find this line and add your key:
   GEMINI_API_KEY = "your-api-key-here"
   ```

5. **Make executable and test**
   ```bash
   chmod +x fact-check.sh
   ./fact-check.sh "Python was created by Guido van Rossum"
   ```

## 🎯 Usage Examples

```bash
# Technology facts
./fact-check.sh "ChatGPT was released in 2022"

# Historical events
./fact-check.sh "World War II ended in 1945"

# Science claims
./fact-check.sh "Water boils at 100 degrees Celsius"

# Myths and misconceptions
./fact-check.sh "You only use 10% of your brain"

# Recent events (Gemini has recent knowledge)
./fact-check.sh "COVID-19 pandemic started in 2019"
```

## 🏗️ Architecture

```
Bash Script (CLI Interface)
    ↓
Python Script (Core Logic)
    ↓
┌─────────────────┬─────────────────┐
│   Gemini API    │  Wikipedia API  │
│  (Fact Check)   │   (Context)     │
└─────────────────┴─────────────────┘
```

## 🔧 Customization

### Adding New Data Sources
```python
# In fact_checker.py, add your own sources:
def search_custom_source(self, query):
    # Your custom API integration here
    pass
```

### Changing AI Models
```python
# Switch to different Gemini models:
self.model = genai.GenerativeModel('gemini-1.5-pro')  # More powerful
self.model = genai.GenerativeModel('gemini-1.5-flash') # Faster (default)
```

### Output Formats
- Modify the bash script for different output styles
- Add JSON output option
- Integrate with other tools via pipes

**Perfect for:**
- Personal fact-checking
- Small team usage
- Educational projects
- Research work

## 🤝 Contributing

This was a weekend project, but contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

**Ideas for contributions:**
- Add more data sources (PubMed, arXiv, etc.)
- Implement caching for repeated queries
- Add batch processing
- Create a web interface
- Add more output formats

## 📝 License

MIT License - Feel free to use, modify, and distribute!

## 🎉 Acknowledgments

- **Google** for the generous Gemini API free tier
- **Wikipedia** for reliable, free knowledge
- **Open Source Community** for inspiration

## 📈 Roadmap

- [ ] Add support for batch fact-checking
- [ ] Implement result caching
- [ ] Add more confidence metrics
- [ ] Create web dashboard
- [ ] Add source credibility scoring
- [ ] Implement fact-check history

---

## 💬 Connect

Built this over a weekend as a proof-of-concept that you don't need expensive APIs for quality fact-checking!

⭐ **Star this repo** if you found it useful!  
🐛 **Report issues** if you find any bugs  
🔄 **Share** with others who need free fact-checking

-------------------------------------------------------------------------

