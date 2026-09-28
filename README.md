# Multi AI Agent Research System

An agentic AI research system that autonomously searches for relevant sources, extracts information from web resources, generates a structured research report, and evaluates the final report using a critic agent.

## Architecture

User Topic
    ↓
Search Agent
    ↓
Reader Agent
    ↓
Research Writer
    ↓
Critic Agent
    ↓
Final Research Report

## Features

- Autonomous research workflow
- Web search agent
- Web content extraction
- Research report generation
- AI based report evaluation
- Multi agent architecture
- Tool calling
- LLM powered reasoning
- Streamlit interface

## Tech Stack

- Python
- LangChain
- Groq
- OpenRouter
- LLMs
- Streamlit
- Web Search
- Web Scraping

## Project Structure


Multi_Ai_Agent_System/
│
├── app.py
├── main.py
├── requirements.txt
│
├── src/
│   ├── agents/
│   │   └── agent.py
│   │
│   ├── pipelines/
│   │   └── pipeline.py
│   │
│   └── tools/
│       └── tools.py
│
└── README.md

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Multi-Ai-Agent-Research-System.git

Move into the project:

cd Multi-Ai-Agent-Research-System

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key

Never commit your .env file.

Run

Run the Streamlit application:

streamlit run app.py

Or run the pipeline directly:

python main.py
Workflow
1. Search Agent

Searches for recent and reliable information related to the research topic.

2. Reader Agent

Selects relevant sources and extracts useful information from the web.

3. Writer

Combines the collected research and generates a structured research report.

4. Critic

Reviews the generated report and provides a score, strengths, areas for improvement, and a final assessment.

Example

Input:

Latest approaches for improving retrieval quality in RAG systems

The system searches for relevant sources, extracts research information, generates a report, and evaluates the report.

Future Improvements
Parallel agent execution
Source quality scoring
Citation tracking
Research history
Better error handling
Agent memory
Improved source verification