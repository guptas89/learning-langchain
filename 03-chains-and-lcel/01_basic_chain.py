"""
Lesson 03: Basic LCEL Chain

This example demonstrates how to connect three LangChain
components into a single pipeline:

    Prompt Template
          |
          v
       Gemini
          |
          v
    Output Parser
          |
          v
      Final String

This is the basic pattern behind many LangChain applications.

LCEL allows us to express the pipeline using:

    prompt | llm | parser
"""

import os

from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
# The Gemini API key is stored in .env.
#
# Keeping credentials outside the source code is important when
# publishing the project to GitHub.
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
# 3. Create the prompt template
# -------------------------------------------------------------------
# The {topic} variable will be replaced with the actual value
# when the chain is invoked.
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an experienced programming teacher."
    ),
    (
        "human",
        "Explain {topic} to a beginner in simple terms."
    ),
])


# -------------------------------------------------------------------
# 4. Create the output parser
# -------------------------------------------------------------------
# Gemini returns an AIMessage.
#
# StrOutputParser extracts the text from that AIMessage so that
# the final result of our chain is a normal Python string.
parser = StrOutputParser()


# -------------------------------------------------------------------
# 5. Build the LCEL chain
# -------------------------------------------------------------------
# The pipe operator (|) connects the components.
#
# Flow:
#
#     Input
#       |
#       v
#     Prompt
#       |
#       v
#     Gemini
#       |
#       v
#     Parser
#       |
#       v
#     String
#
chain = prompt | llm | parser


# -------------------------------------------------------------------
# 6. Execute the chain
# -------------------------------------------------------------------
# The dictionary provides the value for the {topic} variable
# defined in our prompt template.
result = chain.invoke({
    "topic": "React useMemo"
})


# -------------------------------------------------------------------
# 7. Display the final result
# -------------------------------------------------------------------
print("Generated Explanation:")
print(result)