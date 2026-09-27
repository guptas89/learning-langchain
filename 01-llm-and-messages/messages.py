"""
Lesson 01: Chat Messages

Chat-based LLM applications commonly work with three types
of messages:

    SystemMessage
        Defines the behavior or role of the assistant.

    HumanMessage
        Represents the user's request.

    AIMessage
        Represents the model's response.

Conversation flow:

    SystemMessage
          |
          v
    HumanMessage
          |
          v
       Gemini
          |
          v
      AIMessage
"""
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)


# -------------------------------------------------------------------
# Load environment variables
# -------------------------------------------------------------------
load_dotenv()


# -------------------------------------------------------------------
# Initialize Gemini
# -------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


# -------------------------------------------------------------------
# Build the conversation
# -------------------------------------------------------------------
# The system message establishes the assistant's role.
#
# The human message contains the actual user request.
messages = [
    SystemMessage(
        content="You are an experienced Python teacher."
    ),
    HumanMessage(
        content="Explain Python decorators to a beginner."
    ),
]


# -------------------------------------------------------------------
# Send the conversation to Gemini
# -------------------------------------------------------------------
response = llm.invoke(messages)


# -------------------------------------------------------------------
# Display the model response
# -------------------------------------------------------------------
print(response.content)