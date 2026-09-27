"""
Lesson 01: LLMs and Messages

This example demonstrates the most basic interaction between
a Python application and a Gemini chat model through LangChain.

Learning objectives:
    1. Initialize a chat model.
    2. Send a request using invoke().
    3. Understand the AIMessage response.
    4. Extract the text using response.content.

Architecture:

    Python Application
            |
            v
    ┌─────────────────┐
    │  Gemini Flash   │
    │   Chat Model    │
    └────────┬────────┘
             |
             v
         AIMessage
             |
             v
        response.content
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# Load environment variables
# -------------------------------------------------------------------
# The GOOGLE_API_KEY is stored in .env.
#
# Keeping API keys outside the source code is important when
# publishing projects to GitHub.
load_dotenv()


# -------------------------------------------------------------------
# Create the Gemini chat model
# -------------------------------------------------------------------
# temperature=0 makes the model more deterministic.
#
# We will use Gemini Flash throughout this learning repository.
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# Send a request to the model
# -------------------------------------------------------------------
# invoke() is one of the fundamental LangChain methods.
#
# It sends the input to the model and returns an AIMessage object.
response = llm.invoke(
    "Explain LangChain in one sentence."
)


# -------------------------------------------------------------------
# Display the complete response
# -------------------------------------------------------------------
print(response)


# -------------------------------------------------------------------
# Display only the generated text
# -------------------------------------------------------------------
# AIMessage contains more than just text.
# response.content gives us the actual generated response.
print("\nGenerated text:")
print(response.content)