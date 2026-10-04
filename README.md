# Learning LangChain

A practical, from-scratch guide to learning LangChain
through small, runnable Python examples.

## What you'll learn

- LLMs and chat models
- Messages
- Prompt templates
- LCEL and chains
- Structured output
- Runnables
- Tools
- Agents
- A practical mini project

## Requirements

- Python 3.10+
- Gemini API key
- Basic Python knowledge

## Installation

From the project root, create and activate a virtual environment, install the dependencies, and copy the environment-variable template:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp -n .env.example .env
```

If `.env` does not already exist, the command above creates it from the template. Open `.env` and replace `your_gemini_api_key_here` with your Gemini API key. You can create a key in [Google AI Studio](https://aistudio.google.com/app/apikey). Keep `.env` private; it is excluded from Git.

Run a example from the project root with the virtual environment activated:

```bash
python 01-llm-and-messages/basic_llm.py
```

## Learning path

1.  LLMs & Messages
2.  Prompt Templates
3.  Chains & LCEL
4.  Structured Output
5.  Runnables
6.  Tools
7.  Agents
8.  Mini Project
