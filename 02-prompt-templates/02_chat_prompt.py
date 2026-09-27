"""
Lesson 02: Chat Prompt Templates

This example demonstrates how to create a reusable chat prompt
using ChatPromptTemplate.

A chat prompt can contain multiple message templates.

We will use:

    System Message
        |
        | Defines the AI's role
        v
    Human Message
        |
        | Contains the user's dynamic request
        v
    Gemini
        |
        v
    AIMessage

Flow:

    Input Variables
          |
          v
    +-----------------------+
    |  ChatPromptTemplate   |
    +-----------+-----------+
                |
        +-------+-------+
        |               |
        v               v
    System          Human
    Message         Message
        |               |
        +-------+-------+
                |
                v
             Gemini
                |
                v
            AIMessage
"""

import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------------
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
# 3. Create a chat prompt template
# -------------------------------------------------------------------
# The prompt contains two different message types:
#
#   system -> Defines the behavior and role of the AI.
#   human  -> Represents the user's request.
#
# Both messages can contain variables.
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an experienced {technology} developer "
        "who teaches beginners clearly."
    ),
    (
        "human",
        "Explain {topic} to a {level} developer."
    ),
])


# -------------------------------------------------------------------
# 4. Provide values for the template variables
# -------------------------------------------------------------------
# LangChain replaces the variables with the values below.
messages = prompt.format_messages(
    technology="React",
    topic="useMemo",
    level="beginner",
)


# -------------------------------------------------------------------
# 5. Display the generated messages
# -------------------------------------------------------------------
# This is useful while learning because it allows us to see
# what messages will actually be sent to the model.
print("Generated Messages:")
for message in messages:
    print(f"\n{message.type}:")
    print(message.content)


# -------------------------------------------------------------------
# 6. Send the messages to Gemini
# -------------------------------------------------------------------
response = llm.invoke(messages)


# -------------------------------------------------------------------
# 7. Display the model response
# -------------------------------------------------------------------
print("\nModel Response:")
print(response.content)