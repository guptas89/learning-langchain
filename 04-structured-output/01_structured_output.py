"""
Lesson 04: Basic Structured Output

This example demonstrates how to ask an LLM to return
information in a predefined structure.

Instead of receiving arbitrary text, we define a Pydantic
model that describes the data we want.

Flow:

    User Request
          |
          v
    +-------------+
    | Gemini      |
    | Chat Model  |
    +------+------+
           |
           v
    +-------------+
    |  Pydantic   |
    |   Schema    |
    +------+------+
           |
           v
    Python Object

Learning objectives:

    1. Define a Pydantic model.
    2. Connect the model to Gemini.
    3. Use with_structured_output().
    4. Receive structured Python data.
"""

import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
# The Gemini API key is stored in the .env file.
#
# Never put API keys directly into source code.
load_dotenv()


# -------------------------------------------------------------------
# 2. Define the expected output structure
# -------------------------------------------------------------------
# Pydantic allows us to define the fields we expect from the LLM.
#
# The model should return information matching this structure.
class CourseTopic(BaseModel):
    """Represents structured information about a programming topic."""

    name: str = Field(
        description="Name of the programming topic."
    )

    category: str = Field(
        description="Category of the topic."
    )

    description: str = Field(
        description="A short explanation of the topic."
    )

    difficulty: str = Field(
        description="Difficulty level such as beginner, intermediate, or advanced."
    )


# -------------------------------------------------------------------
# 3. Initialize Gemini Flash
# -------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# 4. Configure structured output
# -------------------------------------------------------------------
# with_structured_output() tells LangChain that we want the
# response to follow the CourseTopic schema.
structured_llm = llm.with_structured_output(CourseTopic)


# -------------------------------------------------------------------
# 5. Ask the model for structured information
# -------------------------------------------------------------------
result = structured_llm.invoke(
    "Give me information about React Hooks."
)


# -------------------------------------------------------------------
# 6. Display the structured result
# -------------------------------------------------------------------
print("Structured Result:")
print(result)


# -------------------------------------------------------------------
# 7. Access individual fields
# -------------------------------------------------------------------
# Because the response follows our Pydantic schema, we can
# access individual fields directly.
print("\nTopic Name:")
print(result.name)

print("\nCategory:")
print(result.category)

print("\nDifficulty:")
print(result.difficulty)

print("\nDescription:")
print(result.description)