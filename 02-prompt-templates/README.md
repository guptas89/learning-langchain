02 - Prompt Templates

In the previous lesson, we learned how to communicate with an LLM using messages.

In this lesson, we will learn how to create reusable and dynamic prompts using LangChain prompt templates.

Instead of hard-coding the complete prompt every time, we can define a template with variables and provide values when the application runs.

⸻

What We Will Learn

By the end of this lesson, you will understand:

- What a prompt template is.
- Why prompt templates are useful.
- How to create a basic prompt template.
- How to pass variables into a prompt.
- How to create chat prompts using system and human messages.
- How prompt templates fit into an LLM application.

⸻

1. Why Prompt Templates?

A hard-coded prompt looks like this:

Explain React Hooks to a beginner.

This works, but it is not reusable.

If we want to ask about Angular, Python, or LangGraph, we would need to create another prompt.

A prompt template solves this problem.

Explain {topic} to a {level} developer.

Now the same template can be reused:

topic = React Hooks
level = beginner

or:

topic = LangGraph
level = intermediate

⸻

2. Basic Prompt Template

File

01_basic_prompt.py

The basic flow is:

Input Variables
|
v
+----------------------+
| Prompt Template |
| |
| Explain {topic} to |
| a {level} developer |
+----------+-----------+
|
v
Formatted Prompt

The template contains placeholders such as:

{topic}
{level}

Values are supplied when the template is invoked.

⸻

3. Chat Prompt Template

File

02_chat_prompt.py

For chat-based applications, we can define separate system and human messages.

The flow becomes:

                Input Variables
                       |
                       v
              +----------------+
              | Chat Prompt    |
              |   Template     |
              +-------+--------+
                      |
          +-----------+-----------+
          |                       |
          v                       v

System Message Human Message
| |
+-----------+-----------+
|
v
Chat Model
|
v
AIMessage

For example:

System:
You are an experienced React teacher.
Human:
Explain {topic} to a {level} developer.

The variables are supplied when the application runs.

⸻

4. Why Use Prompt Templates?

Prompt templates provide several benefits:

Reusability

The same prompt structure can be used with different inputs.

Separation of Logic

The prompt structure is separated from application data.

Maintainability

Changing the prompt does not require changing the application logic.

Composition

Prompt templates can later be combined with:

Prompt
|
v
LLM
|
v
Output Parser

This becomes the foundation of LangChain chains and LCEL.

⸻

5. Files in This Lesson

02-prompt-templates/
│
├── README.md
├── 01_basic_prompt.py
└── 02_chat_prompt.py

01_basic_prompt.py

Demonstrates a basic reusable prompt template with variables.

02_chat_prompt.py

Demonstrates a chat prompt containing SystemMessage and HumanMessage templates.

⸻

6. Key Takeaways

The important concept from this lesson is:

Hard-coded Prompt
↓
Prompt Template
↓
Reusable Prompt

And for chat applications:

System Template +
Human Template
|
v
Chat Prompt Template
|
v
Chat Model

⸻

7. Exercise

Modify 02_chat_prompt.py.

Create a prompt template that accepts:

technology
topic
level

For example:

technology = React
topic = useMemo
level = beginner

The prompt should ask the model to explain the topic clearly to the specified level of developer.

Then try changing the values to:

technology = Python
topic = decorators
level = intermediate

You should be able to reuse the same prompt template without changing its structure.

⸻

Next Lesson

In Lesson 3 - Chains and LCEL, we will connect multiple LangChain components together.

The workflow will become:

Input
|
v
Prompt Template
|
v
Chat Model
|
v
Output Parser
|
v
Final Output

This is where we start building actual LangChain pipelines.
