# Multi AI Agent Research System

An agentic AI research system that autonomously searches for relevant sources, extracts information from web resources, generates a structured research report, and evaluates the final report using a critic agent.

## Architecture

```text
User Topic
    |
    v
Search Agent
    |
    |-- web_search
    |
    v
Reader Agent
    |
    |-- scrape_url
    |
    v
Research Writer
    |
    v
Critic Agent
    |
    v
Final Research Report
```

## Features

- Autonomous research workflow
- Web search agent
- Web content extraction
- Research report generation
- AI based report evaluation
- Multi agent architecture
- Tool calling
- LLM powered reasoning
- Streamlit interface for demonstration

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

```text
Multi_Ai_Agent_System/
|
|-- app.py
|-- main.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|
`-- src/
    |
    |-- agents/
    |   `-- agent.py
    |
    |-- pipelines/
    |   `-- pipeline.py
    |
    `-- tools/
        `-- tools.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Multi-Ai-Agent-Research-System.git
```

### 2. Move into the project

```bash
cd Multi-Ai-Agent-Research-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Never commit your `.env` file to GitHub.

## Running the Application

### Streamlit Interface

```bash
streamlit run app.py
```

### Terminal Version

```bash
python main.py
```

## Workflow

### 1. Search Agent

The Search Agent receives the research topic and searches for recent and reliable sources using the web search tool.

### 2. Reader Agent

The Reader Agent selects a relevant source and extracts useful information from the webpage using the scraping tool.

### 3. Research Writer

The Writer combines the search results and extracted research to generate a structured research report.

### 4. Critic Agent

The Critic reviews the generated report and provides:

- Score
- Strengths
- Areas for improvement
- Final assessment

## Example

### Input

```text
Latest approaches for improving retrieval quality in RAG systems
```

### Pipeline

```text
Research Topic
      |
      v
Search Agent
      |
      v
Relevant Sources
      |
      v
Reader Agent
      |
      v
Extracted Research
      |
      v
Research Writer
      |
      v
Generated Report
      |
      v
Critic Agent
      |
      v
Final Review
```

## Future Improvements

- Parallel agent execution
- Source quality scoring
- Citation tracking
- Research history
- Better error handling
- Agent memory
- Improved source verification

## License

This project is for educational and portfolio purposes.
