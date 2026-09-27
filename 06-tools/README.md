06 - Tools

In the previous lessons, we learned how to build LangChain pipelines using prompts, models, parsers, and Runnables.

However, an LLM has an important limitation:

An LLM can generate information, but it cannot automatically perform actions in our application.

For example, an LLM cannot directly:

- Query our database.
- Call our internal API.
- Read a file.
- Calculate a value using application logic.
- Search a custom data source.

For these situations, we can give the LLM access to tools.

⸻

What We Will Learn

By the end of this lesson, you will understand:

- What a LangChain tool is.
- How to create a custom tool.
- How to use the @tool decorator.
- What tool calling means.
- How an LLM decides that a tool is needed.
- How tool results are returned to the application.
- The difference between a tool and an LLM.

⸻

1. What Is a Tool?

A tool is a function that an LLM can request the application to execute.

For example:

get_weather(city)

or:

calculate_tax(amount)

or:

search_customer(customer_id)

The important point is:

LLM does NOT directly execute the function.

Instead, the LLM requests a tool call and the application executes the function.

⸻

2. Basic Tool Flow

The basic concept is:

User
|
v
LLM
|
| "I need this tool"
v
Tool
|
| executes Python function
v
Tool Result
|
v
Application / LLM

For example:

User:
"What is 25 × 4?"
|
v
LLM
|
| call calculator
v
calculator(25, 4)
|
v
100

⸻

3. Creating a Tool

File

01_basic_tool.py

LangChain provides the @tool decorator to turn a normal Python function into a LangChain tool.

Conceptually:

Python Function
|
v
@tool
|
v
LangChain Tool

The function’s:

- Name
- Description
- Parameters

become important information that can be provided to the LLM.

⸻

4. Tool Calling

File

02_tool_calling.py

Tool calling means that the LLM can determine that a tool should be used and generate a structured tool request.

The flow becomes:

                    User
                     |
                     v
              +-------------+
              |     LLM     |
              +------+------+
                     |
             Tool needed?
                /       \
              No         Yes
              |           |
              v           v
          Response      Tool Call
                            |
                            v
                          Tool
                            |
                            v
                       Tool Result
                            |
                            v
                           LLM
                            |
                            v
                       Final Answer

⸻

5. Tool vs LLM

These two concepts should not be confused.

LLM

The LLM is responsible for:

- Understanding the request.
- Generating language.
- Deciding what information or action may be needed.

Tool

A tool performs an actual operation.

For example:

LLM
|
| "I need customer information."
v
Tool
|
v
Database
|
v
Customer Data

The tool performs the operation.

⸻

6. Example Tools

In real applications, tools might represent:

Database
↓
get_customer()
REST API
↓
get_order_status()
Calculator
↓
calculate_total()
File System
↓
read_document()
Search
↓
search_documents()

This is one of the foundations of AI agents.

⸻

7. Important Security Concept

Tools can perform real operations.

Therefore, tools should be designed carefully.

For example:

Safe Tool
get_customer()

is different from:

Dangerous Tool
delete_customer()

When building real agents, tool permissions and validation are important.

For this learning repository, we will use simple read-only examples.

⸻

8. Tool Calling vs Normal Function Calling

A normal Python function is called directly by our code:

Python
|
v
function()

With LLM tool calling:

User
|
v
LLM
|
| requests tool
v
Application
|
v
Tool

The LLM determines whether a tool should be requested based on the user’s input.

⸻

9. Files in This Lesson

06-tools/
│
├── README.md
├── 01_basic_tool.py
└── 02_tool_calling.py

01_basic_tool.py

Demonstrates how to create a custom LangChain tool using the @tool decorator.

02_tool_calling.py

Demonstrates how an LLM can be given access to a tool and generate a tool call.

⸻

10. Key Takeaways

Remember:

Tool
=
A function that an application exposes
for an LLM to request.

The overall flow is:

User
↓
LLM
↓
Tool Call
↓
Tool
↓
Tool Result
↓
LLM
↓
Final Response

This pattern is one of the foundations of modern AI agents.

⸻

11. Exercise

Create a tool called:

calculate_square(number)

It should return the square of a number.

For example:

Input:
5
Output:
25

Then modify the tool-calling example so that the model can use this tool.

Try asking:

What is the square of 12?

Observe whether the model requests the calculator tool.

⸻

Next Lesson

In Lesson 7 - Agents, we will combine:

LLM

- Tools
- Tool Calling
- Reasoning Loop

into an actual agent.

The architecture will become:

             User
               |
               v
             Agent
               |
        +------+------+
        |             |
        v             v
      Tool          Answer
        |
        v
    Tool Result
        |
        +-------> Agent

This will be the final major LangChain concept before our mini project.
