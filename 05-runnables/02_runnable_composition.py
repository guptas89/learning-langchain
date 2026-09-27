"""
Lesson 05: Runnable Composition

This example demonstrates how multiple Runnables can be
connected together.

We will also introduce RunnableParallel.

The example creates two independent pieces of information
about a technology:

    1. A simple definition
    2. A learning recommendation

Both operations receive the same input.

Flow:

                     Input
                       |
             +---------+---------+
             |                   |
             v                   v
       Definition           Recommendation
       Runnable              Runnable
             |                   |
             +---------+---------+
                       |
                       v
                 Combined Result
"""

from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
)


# -------------------------------------------------------------------
# 1. Define the first Python function
# -------------------------------------------------------------------
def create_definition(technology: str) -> str:
    """
    Create a simple definition for the supplied technology.
    """
    return f"{technology} is a technology used to build software."


# -------------------------------------------------------------------
# 2. Define the second Python function
# -------------------------------------------------------------------
def create_recommendation(technology: str) -> str:
    """
    Create a simple learning recommendation.
    """
    return f"Start learning the core concepts of {technology} first."


# -------------------------------------------------------------------
# 3. Convert both functions into Runnables
# -------------------------------------------------------------------
definition_runnable = RunnableLambda(
    create_definition
)

recommendation_runnable = RunnableLambda(
    create_recommendation
)


# -------------------------------------------------------------------
# 4. Run both Runnables in parallel
# -------------------------------------------------------------------
# RunnableParallel sends the same input to both Runnables.
#
# The result is combined into a dictionary:
#
# {
#     "definition": ...,
#     "recommendation": ...
# }
parallel = RunnableParallel(
    definition=definition_runnable,
    recommendation=recommendation_runnable,
)


# -------------------------------------------------------------------
# 5. Execute the parallel Runnable
# -------------------------------------------------------------------
result = parallel.invoke("LangGraph")


# -------------------------------------------------------------------
# 6. Display the combined result
# -------------------------------------------------------------------
print("Combined Result:")
print(result)


# -------------------------------------------------------------------
# 7. Access individual results
# -------------------------------------------------------------------
print("\nDefinition:")
print(result["definition"])

print("\nRecommendation:")
print(result["recommendation"])