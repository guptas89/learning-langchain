"""
Lesson 03: Chain Composition

This example demonstrates how multiple LCEL chains can be
combined to create a larger workflow.

We will build:

    Topic
      |
      v
    Explanation Chain
      |
      v
    Summary Chain
      |
      v
    Final Summary

The important idea is that a chain can be treated as a
component and connected to another chain.

Flow:

    Topic
      |
      v
+---------------------+
| Explanation Chain   |
+----------+----------+
           |
           v
+---------------------+
| Summary Chain       |
+----------+----------+
           |
           v
      Final Summary
"""

import os

from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
load_dotenv()


# -------------------------------------------------------------------
# 2. Initialize Gemini Flash
# -------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# 3. Create the explanation prompt
# -------------------------------------------------------------------
explanation_prompt = ChatPromptTemplate.from_template(
    """
    Explain the following programming topic to a beginner.

    Topic:
    {topic}

    Include:
    - A simple definition
    - How it works
    - One practical example
    """
)


# -------------------------------------------------------------------
# 4. Create the explanation chain
# -------------------------------------------------------------------
explanation_chain = (
    explanation_prompt
    | llm
    | StrOutputParser()
)


# -------------------------------------------------------------------
# 5. Create the summary prompt
# -------------------------------------------------------------------
summary_prompt = ChatPromptTemplate.from_template(
    """
    Summarize the following explanation in exactly 3 bullet points.

    Explanation:
    {explanation}
    """
)


# -------------------------------------------------------------------
# 6. Create the summary chain
# -------------------------------------------------------------------
summary_chain = (
    summary_prompt
    | llm
    | StrOutputParser()
)


# -------------------------------------------------------------------
# 7. Transform the output between the two chains
# -------------------------------------------------------------------
# The explanation chain returns a string:
#
#     "React useMemo is..."
#
# But the summary prompt expects a dictionary:
#
#     {
#         "explanation": "..."
#     }
#
# RunnableLambda performs this small transformation.
to_summary_input = RunnableLambda(
    lambda explanation: {
        "explanation": explanation
    }
)


# -------------------------------------------------------------------
# 8. Compose the complete workflow
# -------------------------------------------------------------------
# Flow:
#
#     topic
#       |
#       v
#     Explanation Chain
#       |
#       v
#     RunnableLambda
#       |
#       v
#     Summary Chain
#       |
#       v
#     Final Summary
#
full_chain = (
    explanation_chain
    | to_summary_input
    | summary_chain
)


# -------------------------------------------------------------------
# 9. Execute the complete workflow
# -------------------------------------------------------------------
result = full_chain.invoke({
    "topic": "React useMemo"
})


# -------------------------------------------------------------------
# 10. Display the result
# -------------------------------------------------------------------
print("Final Summary:")
print(result)