01 - LLMs and Messages

This lesson introduces the basic building blocks of a LangChain application.

We will learn how to:

- Connect a Python application to an LLM using LangChain.
- Initialize a Gemini Flash chat model.
- Use invoke() to send a request to the model.
- Understand the AIMessage response.
- Understand SystemMessage and HumanMessage.
- Build a basic conversation using messages.

⸻

Prerequisites

Before starting this lesson, you should have:

- Python 3.10+
- Basic Python knowledge
- A Gemini API key

Create a .env file in the project root:

GOOGLE_API_KEY=your_api_key_here

Never commit your .env file or API key to GitHub.

⸻

1. Basic LLM Interaction

File

01_basic_llm.py

This is the simplest example in the repository.

We initialize a Gemini chat model and use LangChain’s invoke() method to send a request.

Flow

Python Application
|
| invoke()
v
+------------------+
| Gemini Flash |
| Chat Model |
+--------+---------+
|
v
AIMessage
|
v
response.content

Key Concepts

Chat Model

A chat model is an LLM designed to work with conversational inputs and messages.

In this repository, we use Gemini Flash through LangChain.

invoke()

invoke() sends input to the model and returns its response.

Conceptually:

Application
|
| invoke(input)
v
Chat Model
|
v
AIMessage

AIMessage

The model response is returned as an AIMessage.

The generated text can be accessed using:

response.content

⸻

2. Messages

File

02_messages.py

LLM applications commonly represent conversations using different message types.

The three important message types are:

Message Purpose
SystemMessage Defines the behavior or role of the AI
HumanMessage Represents the user’s input
AIMessage Represents the model’s response

Flow

+-------------------------+
| SystemMessage |
| "You are a teacher." |
+------------+------------+
|
v
+-------------------------+
| HumanMessage |
| "Explain React hooks." |
+------------+------------+
|
v
+-------------------------+
| Gemini |
| Chat Model |
+------------+------------+
|
v
+-------------------------+
| AIMessage |
| Generated answer |
+-------------------------+

⸻

3. Message-Based Conversation

A conversation can be represented as a sequence of messages:

SystemMessage
|
v
HumanMessage
|
v
AIMessage

For a multi-turn conversation, the application can provide previous messages as part of the input:

SystemMessage
|
v
HumanMessage
|
v
AIMessage
|
v
HumanMessage
|
v
AIMessage

This is an important concept because the model does not automatically maintain application-level conversation history. The application provides the relevant message history when making a request.

⸻

4. Files in This Lesson

01-llm-and-messages/
│
├── README.md
├── 01_basic_llm.py
└── 02_messages.py

01_basic_llm.py

Learn the basic interaction between a Python application and a Gemini chat model.

02_messages.py

Learn how SystemMessage and HumanMessage are sent to the model and how the model returns an AIMessage.

⸻

5. Key Takeaways

After completing this lesson, you should understand:

Chat Model
|
+-- invoke()
|
+-- SystemMessage
|
+-- HumanMessage
|
+-- AIMessage

The most important mental model is:

Application
|
v
Messages / Input
|
v
LangChain Chat Model
|
v
AIMessage

⸻

6. Exercise

Modify 02_messages.py.

Change the system message so that Gemini behaves like a:

Senior React developer who teaches beginners.

Then ask:

Explain React Hooks to a beginner.

Run the program and observe how the system message affects the response.

⸻

Next Lesson

In Lesson 2 - Prompt Templates, we will learn how to create reusable prompts instead of hard-coding the entire prompt every time.

The workflow will become:

Input Variables
|
v
Prompt Template
|
v
Chat Model
|
v
AI Response
