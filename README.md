# 🧠 Research Assistant Agent

A smart, tool-using research assistant powered by LangChain and OpenAI/Anthropic LLMs. It can search the web, extract information from Wikipedia, and save structured research summaries to a text file.

## 🚀 Features

- 🧾 Accepts a user query and returns a structured response with:
  - Topic
  - Summary
  - Sources
  - Tools used
- 🌐 Uses DuckDuckGo for web search
- 📚 Queries Wikipedia for relevant info
- 💾 Saves output to `research_output.txt`

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4o](https://platform.openai.com/docs/models/gpt-4o)
- [Anthropic Claude (optional)](https://www.anthropic.com/index/introducing-claude)
- Python 3.8+
- Pydantic
- Dotenv

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/research-assistant-agent.git
   cd research-assistant-agent

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   
3. **Install dependencies**
   ```bash
    pip install -r requirements.txt
   
4. **Set up .env file**
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key (optional)

🧪 Run the App
    ```bash
    python main.py

📁 File Structure
    ```bash
    main.py              # Entry script
    tools.py             # Web, Wikipedia, and file-saving tools
    requirements.txt     # Dependencies
    research_output.txt  # Saved outputs
    .env                 # API keys


