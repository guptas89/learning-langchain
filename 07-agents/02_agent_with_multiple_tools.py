"""
Lesson 07: Agent with Multiple Tools

This example demonstrates an agent that has access to multiple
tools.

Available tools:

    calculate_square()
    calculate_cube()

The agent decides which tool is appropriate for the user's
request.

Flow:

                         User
                           |
                           v
                         Agent
                           |
                           v
                     Gemini Flash
                           |
                +----------+----------+
                |                     |
                v                     v
       calculate_square()     calculate_cube()
                |                     |
                +----------+----------+
                           |
                           v
                       Tool Result
                           |
                           v
                         Agent
                           |
                           v
                      Final Answer
"""

import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
# GOOGLE_API_KEY is read from the .env file.
load_dotenv()


# -------------------------------------------------------------------
# 2. Create the square calculation tool
# -------------------------------------------------------------------
@tool
def calculate_square(number: int) -> int:
    """
    Calculate the square of an integer.

    Args:
        number: The integer to square.

    Returns:
        The square of the number.
    """
    return number * number


# -------------------------------------------------------------------
# 3. Create the cube calculation tool
# -------------------------------------------------------------------
@tool
def calculate_cube(number: int) -> int:
    """
    Calculate the cube of an integer.

    Args:
        number: The integer to cube.

    Returns:
        The cube of the number.
    """
    return number * number * number


# -------------------------------------------------------------------
# 4. Initialize Gemini Flash
# -------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# 5. Create the agent
# -------------------------------------------------------------------
# The agent now has two tools available.
#
# The LLM can decide which tool is appropriate based on
# the user's request.
agent = create_agent(
    model=llm,
    tools=[
        calculate_square,
        calculate_cube,
    ],
    system_prompt=(
        "You are a helpful math assistant. "
        "Use the available calculation tools when appropriate."
    ),
)


# -------------------------------------------------------------------
# 6. Ask the agent to calculate a square
# -------------------------------------------------------------------
print("=" * 80)
print("QUESTION 1")
print("=" * 80)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is the square of 5?",
        }
    ]
})


# -------------------------------------------------------------------
# 7. Display the first conversation
# -------------------------------------------------------------------
for message in result["messages"]:
    print(message)
    print("-" * 80)


# -------------------------------------------------------------------
# 8. Ask the agent to calculate a cube
# -------------------------------------------------------------------
print("\n")
print("=" * 80)
print("QUESTION 2")
print("=" * 80)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is the cube of 5?",
        }
    ]
})


# -------------------------------------------------------------------
# 9. Display the second conversation
# -------------------------------------------------------------------
for message in result["messages"]:
    print(message)
    print("-" * 80)