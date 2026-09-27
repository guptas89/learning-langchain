04 - Structured Output

In the previous lessons, we learned how to:

- Communicate with an LLM.
- Work with messages.
- Create reusable prompt templates.
- Build chains using LCEL.

In this lesson, we will learn how to ask an LLM to return data in a defined structure instead of returning arbitrary text.

This is called structured output.

⸻

What We Will Learn

By the end of this lesson, you will understand:

- Why free-form LLM responses can be difficult for applications to use.
- What structured output means.
- How to define a Pydantic model.
- How to use with_structured_output().
- How an LLM response can become a Python object.
- How structured output can be used inside an LCEL chain.

⸻

1. The Problem with Free-Form Text

Suppose we ask an LLM:

Tell me about React.

The model might return:

React is a JavaScript library used for building user interfaces...

This is useful for a human.

But an application may need specific fields:

name
category
description
difficulty

A free-form response makes it difficult to reliably extract those values.

⸻

2. Structured Output

Instead of asking for arbitrary text, we define the structure we want.

For example:

CourseTopic
│
├── name
├── category
├── description
└── difficulty

The model should return data matching this structure.

⸻

3. Pydantic Model

We can describe the expected structure using a Pydantic model:

CourseTopic
|
+-- name: str
+-- category: str
+-- description: str
+-- difficulty: str

Pydantic provides validation and gives us a predictable Python object.

⸻

4. Structured Output Flow

The basic flow is:

User Request
|
v
+-------------------+
| Chat Model |
+---------+---------+
|
v
+-------------------+
| Structured Schema |
| Pydantic |
+---------+---------+
|
v
+-------------------+
| Python Object |
+-------------------+

Instead of:

LLM → String

we get:

LLM → Structured Python Object

⸻

5. with_structured_output()

LangChain provides:

with_structured_output()

to connect a chat model with a schema.

Conceptually:

Chat Model +
Pydantic Schema
|
v
Structured Chat Model

We can then invoke the model and receive data that follows our schema.

⸻

6. Basic Example

File

01_structured_output.py

We will define a simple CourseTopic model.

CourseTopic
|
+-- name
+-- category
+-- description
+-- difficulty

The model will return an instance of this structure.

⸻

7. Structured Output in a Chain

File

02_structured_chain.py

We will combine structured output with the concepts from previous lessons.

The flow becomes:

Input
|
v
Prompt Template
|
v
Gemini
|
v
Pydantic Schema
|
v
Structured Python Object

This demonstrates how structured output can become part of a LangChain pipeline.

⸻

8. Why Structured Output Matters

Structured output is useful when an LLM needs to provide information to another part of an application.

Common examples include:

- Data extraction
- Classification
- API responses
- Form processing
- RAG applications
- Agent workflows
- Database operations

For example:

User
|
v
LLM
|
v
Structured Data
|
+------> Database
|
+------> API
|
+------> Application Logic

⸻

9. Important Mental Model

Remember the progression:

Lesson 1
LLM
↓
Text
Lesson 2
Prompt Template
↓
LLM
↓
Text
Lesson 3
Prompt
↓
LLM
↓
Parser
↓
Text
Lesson 4
Prompt
↓
LLM
↓
Schema
↓
Structured Data

This is an important transition from generative AI to application-oriented AI.

⸻

10. Files in This Lesson

04-structured-output/
│
├── README.md
├── 01_structured_output.py
└── 02_structured_chain.py

01_structured_output.py

Demonstrates how to define a Pydantic schema and use it with a Gemini chat model.

02_structured_chain.py

Demonstrates how structured output can be combined with a prompt template to create an LCEL chain.

⸻

11. Key Takeaways

After completing this lesson, you should understand:

Free-form LLM response
↓
String

versus:

Structured LLM response
↓
Defined Schema
↓
Python Object

The main concepts are:

Pydantic

- with_structured_output()
- LCEL

⸻

12. Exercise

Modify the Pydantic model so that it represents a technology rather than a course topic.

For example:

Technology
│
├── name
├── type
├── primary_use
└── popularity

Then ask the model to return structured information about:

React

Try the same code with:

LangGraph

The application code should remain mostly unchanged. Only the input and/or schema should need to change.

⸻

Next Lesson

In Lesson 5 - Runnables, we will learn the building blocks behind LCEL.

We will explore:

Runnable
RunnableLambda
RunnablePassthrough
RunnableParallel

and understand how LangChain moves data between components.

The mental model will become:

Input
|
v
Runnable
|
v
Runnable
|
v
Runnable
|
v
Output
