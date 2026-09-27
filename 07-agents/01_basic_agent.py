"""
Lesson 07: Basic Agent

This example demonstrates a simple LangChain agent that has
access to a calculator tool.

The important difference between a chain and an agent is that
the agent can decide whether it needs to use a tool.

Flow:

                         User
                           |
                           v
                        Agent
                           |
                           v
                     Gemini Flash
                           |
                    Need calculator?
                       /        \
                     No          Yes
                     |            |
                     v            v
                  Answer      Calculator
                                  |
                                  v
                             Tool Result
                                  |
                                  v
                                Agent
                                  |
                                  v
                             Final Answer

This example uses LangChain's current agent abstraction.
"""

import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
# The Google Gemini API key is stored in .env:
#
# GOOGLE_API_KEY=your_api_key
#
# Never commit your .env file to GitHub.
load_dotenv()


# -------------------------------------------------------------------
# 2. Create the calculator tool
# -------------------------------------------------------------------
# The @tool decorator exposes this Python function as a
# LangChain tool.
#
# The docstring is important because it tells the LLM what
# this tool does.
@tool
def calculate_square(number: int) -> int:
    """
    Calculate the square of an integer.

    Args:
        number: The integer whose square should be calculated.

    Returns:
        The square of the number.
    """
    return number * number


# -------------------------------------------------------------------
# 3. Initialize Gemini Flash
# -------------------------------------------------------------------
# os.getenv() reads GOOGLE_API_KEY from the .env file.
#
# temperature=0 makes the model's responses more deterministic.
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# 4. Create the agent
# -------------------------------------------------------------------
# The agent receives:
#
#     - The Gemini model
#     - A list of tools
#
# The agent uses the model to decide whether a tool should
# be called.
agent = create_agent(
    model=llm,
    tools=[calculate_square],
    system_prompt=(
        "You are a helpful assistant. "
        "Use the calculator tool when a calculation is required."
    ),
)


# -------------------------------------------------------------------
# 5. Send a request to the agent
# -------------------------------------------------------------------
# The input uses the standard message format:
#
# [
#     {
#         "role": "user",
#         "content": "..."
#     }
# ]
#
# The agent decides what to do with this request.
result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is the square of 12?",
        }
    ]
})


# -------------------------------------------------------------------
# 6. Display the agent messages
# -------------------------------------------------------------------
# An agent may produce several messages while it works.
#
# For learning purposes, we print the complete message history
# so that you can see the agent/tool interaction.
print("Agent Messages:\n")

for message in result["messages"]:
    print(message)
    print("-" * 80)