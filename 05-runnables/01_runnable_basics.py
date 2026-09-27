"""
Lesson 05: Runnable Basics

This example introduces two important LangChain Runnables:

    1. RunnableLambda
    2. RunnablePassthrough

A Runnable is a component that receives input and produces output.

Flow:

    Input
      |
      v
    RunnableLambda
      |
      v
    Transformed Output


    Input
      |
      v
    RunnablePassthrough
      |
      v
    Same Input
"""

from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
)


# -------------------------------------------------------------------
# 1. Create a normal Python function
# -------------------------------------------------------------------
# This function accepts a technology name and adds a prefix.
#
# We will later convert this normal Python function into a
# LangChain Runnable.
def add_prefix(technology: str) -> str:
    """
    Add a descriptive prefix to a technology name.
    """
    return f"Learning: {technology}"


# -------------------------------------------------------------------
# 2. Convert the Python function into a Runnable
# -------------------------------------------------------------------
# RunnableLambda allows a normal Python function to participate
# in an LCEL pipeline.
add_prefix_runnable = RunnableLambda(add_prefix)


# -------------------------------------------------------------------
# 3. Execute the Runnable
# -------------------------------------------------------------------
result = add_prefix_runnable.invoke("Python")


# -------------------------------------------------------------------
# 4. Display the result
# -------------------------------------------------------------------
print("RunnableLambda result:")
print(result)


# -------------------------------------------------------------------
# 5. Create a RunnablePassthrough
# -------------------------------------------------------------------
# RunnablePassthrough returns the input without modifying it.
passthrough = RunnablePassthrough()


# -------------------------------------------------------------------
# 6. Execute RunnablePassthrough
# -------------------------------------------------------------------
original_value = passthrough.invoke("React")


# -------------------------------------------------------------------
# 7. Display the result
# -------------------------------------------------------------------
print("\nRunnablePassthrough result:")
print(original_value)