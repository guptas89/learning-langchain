"""
Lesson 06: Basic Tools

This example demonstrates how to turn a normal Python function
into a LangChain Tool using the @tool decorator.

A tool is a function that can be exposed to an LLM.

Flow:

    Python Function
          |
          v
       @tool
          |
          v
    LangChain Tool

The LLM does not directly execute the function.
The application is responsible for executing the tool.
"""

from langchain_core.tools import tool


# -------------------------------------------------------------------
# 1. Create a normal Python function and decorate it with @tool
# -------------------------------------------------------------------
# The @tool decorator converts the function into a LangChain Tool.
#
# The function name becomes the tool name.
#
# The docstring is important because it describes to the LLM
# what the tool does.
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
# 2. Inspect the tool
# -------------------------------------------------------------------
# A LangChain Tool contains metadata that can be provided to
# an LLM during tool calling.
print("Tool name:")
print(calculate_square.name)

print("\nTool description:")
print(calculate_square.description)


# -------------------------------------------------------------------
# 3. Execute the tool directly
# -------------------------------------------------------------------
# A tool can still be executed by our application.
#
# This example calls the tool directly so that we can first
# understand what a LangChain Tool actually is.
result = calculate_square.invoke({
    "number": 5
})


# -------------------------------------------------------------------
# 4. Display the result
# -------------------------------------------------------------------
print("\nTool Result:")
print(result)