"""
Lesson 02: Basic Prompt Templates

This example demonstrates how to create a reusable prompt
using LangChain's PromptTemplate.

Instead of hard-coding a complete prompt, we define variables
that can be replaced with different values at runtime.

Flow:

    Input Variables
          |
          v
    +----------------------+
    |    PromptTemplate    |
    |                      |
    | Explain {topic} to   |
    | a {level} developer  |
    +----------+-----------+
               |
               v
        Formatted Prompt
               |
               v
             Gemini
               |
               v
          AI Response
"""

import os

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
# The Gemini API key is stored in the .env file.
#
# Keeping API keys outside the source code prevents accidentally
# committing sensitive credentials to GitHub.
load_dotenv()


# -------------------------------------------------------------------
# 2. Initialize the Gemini Flash chat model
# -------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# 3. Create a reusable prompt template
# -------------------------------------------------------------------
# The values inside {topic} and {level} are variables.
#
# We will provide their actual values later when invoking
# the prompt template.
prompt = PromptTemplate.from_template(
    "Explain {topic} to a {level} developer."
)


# -------------------------------------------------------------------
# 4. Provide values for the template variables
# -------------------------------------------------------------------
# LangChain replaces:
#
#     {topic} -> React Hooks
#     {level} -> beginner
#
# The resulting prompt becomes:
#
#     Explain React Hooks to a beginner developer.
formatted_prompt = prompt.format(
    topic="React Hooks",
    level="beginner",
)


# -------------------------------------------------------------------
# 5. Display the generated prompt
# -------------------------------------------------------------------
# Printing the prompt helps us understand what is actually
# being sent to the model.
print("Formatted Prompt:")
print(formatted_prompt)


# -------------------------------------------------------------------
# 6. Send the formatted prompt to Gemini
# -------------------------------------------------------------------
response = llm.invoke(formatted_prompt)


# -------------------------------------------------------------------
# 7. Display the model response
# -------------------------------------------------------------------
print("\nModel Response:")
print(response.content)