"""
Lesson 06: Tool Calling

This example demonstrates how an LLM can be given access to
a LangChain tool.

The LLM does not execute the Python function itself.

Instead:

    1. The user sends a request.
    2. The LLM determines whether a tool is needed.
    3. The LLM creates a structured tool call.
    4. The application executes the tool.
    5. The application can provide the result back to the LLM.

Flow:

                    User
                     |
                     v
              +-------------+
              |    Gemini   |
              +------+------+
                     |
                     | Tool Call
                     v
              +-------------+
              |    Tool     |
              +------+------+
                     |
                     v
                Tool Result
"""

import os

from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
load_dotenv()


# -------------------------------------------------------------------
# 2. Create a custom tool
# -------------------------------------------------------------------
@tool
def calculate_square(number: int) -> int:
    """
    Calculate the square of an integer.

    Args:
        number: The integer whose square should be calculated.

    Returns:
        The square of the provided number.
    """
    return number * number


# -------------------------------------------------------------------
# 3. Initialize Gemini Flash
# -------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# 4. Bind the tool to the LLM
# -------------------------------------------------------------------
# bind_tools() tells the model that this tool is available.
#
# Important:
# The LLM still does NOT execute the Python function.
#
# It can only generate a request asking the application to
# execute the tool.
llm_with_tools = llm.bind_tools([
    calculate_square
])


# -------------------------------------------------------------------
# 5. Send a request that requires the tool
# -------------------------------------------------------------------
response = llm_with_tools.invoke(
    "What is the square of 12?"
)


# -------------------------------------------------------------------
# 6. Display the model response
# -------------------------------------------------------------------
print("Model Response:")
print(response)


# -------------------------------------------------------------------
# 7. Inspect tool calls
# -------------------------------------------------------------------
# If Gemini decides that the calculator tool is appropriate,
# the AIMessage should contain tool call information.
print("\nTool Calls:")

for tool_call in response.tool_calls:
    print(tool_call)