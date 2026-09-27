"""
Lesson 04: Structured Output with LCEL

This example combines concepts from previous lessons:

    Lesson 2
        Prompt Templates

    Lesson 3
        LCEL Chains

    Lesson 4
        Structured Output

Complete flow:

    User Input
         |
         v
    Prompt Template
         |
         v
    Gemini Flash
         |
         v
    Pydantic Schema
         |
         v
    Structured Python Object
"""

import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
load_dotenv()


# -------------------------------------------------------------------
# 2. Define the expected output structure
# -------------------------------------------------------------------
class TechnologyInfo(BaseModel):
    """
    Represents structured information about a technology.
    """

    name: str = Field(
        description="Name of the technology."
    )

    type: str = Field(
        description="Type or category of the technology."
    )

    primary_use: str = Field(
        description="The primary use of the technology."
    )

    popularity: str = Field(
        description="General popularity level such as low, medium, or high."
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
# The model will now return data that follows TechnologyInfo.
structured_llm = llm.with_structured_output(
    TechnologyInfo
)


# -------------------------------------------------------------------
# 5. Create the prompt template
# -------------------------------------------------------------------
# The {technology} variable allows us to reuse the same
# chain for different technologies.
prompt = ChatPromptTemplate.from_template(
    """
    Provide structured information about the following technology:

    Technology:
    {technology}
    """
)


# -------------------------------------------------------------------
# 6. Build the LCEL chain
# -------------------------------------------------------------------
# Flow:
#
#     Input
#       |
#       v
#     Prompt
#       |
#       v
#     Structured LLM
#       |
#       v
#     TechnologyInfo
#
chain = prompt | structured_llm


# -------------------------------------------------------------------
# 7. Execute the chain
# -------------------------------------------------------------------
result = chain.invoke({
    "technology": "React"
})


# -------------------------------------------------------------------
# 8. Display the complete structured object
# -------------------------------------------------------------------
print("Structured Technology Information:")
print(result)


# -------------------------------------------------------------------
# 9. Access individual fields
# -------------------------------------------------------------------
print("\nName:")
print(result.name)

print("\nType:")
print(result.type)

print("\nPrimary Use:")
print(result.primary_use)

print("\nPopularity:")
print(result.popularity)