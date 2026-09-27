07 - Agents

In the previous lesson, we learned about tools and tool calling.

We saw that an LLM can decide that a tool is required and generate a tool call.

However, our previous example stopped at the tool-call stage.

In this lesson, we will complete the process and build an actual agent.

⸻

What We Will Learn

By the end of this lesson, you will understand:

- What an AI agent is.
- How an agent differs from a normal chain.
- How an agent uses tools.
- How an agent decides which tool to use.
- How tool execution works.
- How the agent receives the tool result.
- How the agent produces a final answer.
- How multiple tools can be given to an agent.

⸻

1. What Is an Agent?

A simple chain follows a predefined sequence.

For example:

Input
↓
Prompt
↓
LLM
↓
Parser
↓
Output

The sequence is predefined.

An agent is different.

An agent can decide what action it needs to take based on the user’s request.

Conceptually:

User
|
v
Agent
|
v
Decide what to do
|
+-------> Answer directly
|
+-------> Call Tool
|
v
Tool Result
|
v
Agent
|
v
Final Answer

⸻

2. Chain vs Agent

Chain

A chain follows a predefined path:

A
↓
B
↓
C
↓
D

The developer defines the sequence.

⸻

Agent

An agent can decide what to do next:

             Input
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
     Result
        |
        └────────→ Agent

The agent can continue until it has enough information to produce the final response.

⸻

3. Agent Loop

The most important concept in this lesson is the agent loop.

                 User
                   |
                   v
                Agent
                   |
                   v
             Decide Action
                   |
            +------+------+
            |             |
            v             v
         Answer          Tool
            |             |
            |             v
            |         Tool Result
            |             |
            |             v
            |           Agent
            |             |
            +-------------+
                   |
                   v
              Final Answer

The agent may perform multiple tool calls before producing the final answer.

⸻

4. Example

Suppose we give an agent two tools:

calculate_square()
get_temperature()

The user asks:

What is the square of 12?

The agent may decide:

User
↓
Agent
↓
calculate_square
↓
144
↓
Agent
↓
Final Answer

If the user asks:

What is the temperature in Delhi?

the agent may decide:

User
↓
Agent
↓
get_temperature
↓
Temperature Result
↓
Agent
↓
Final Answer

The important part is that the agent chooses the appropriate tool.

⸻

5. Creating an Agent

File

01_basic_agent.py

We will create:

LLM

- Tool
- Agent

The agent will be able to use a calculator tool.

The flow will be:

User Question
|
v
Agent
|
v
Calculator Tool
|
v
Tool Result
|
v
Agent
|
v
Final Answer

⸻

6. Multiple Tools

File

02_agent_with_multiple_tools.py

We will provide the agent with multiple tools.

For example:

calculate_square()
calculate_cube()

The agent must decide which tool is appropriate.

Flow:

                    User
                      |
                      v
                    Agent
                      |
             +--------+--------+
             |                 |
             v                 v
     calculate_square()   calculate_cube()
             |                 |
             +--------+--------+
                      |
                      v
                  Tool Result
                      |
                      v
                    Agent
                      |
                      v
                 Final Answer

⸻

7. Agent vs Tool

Remember:

Tool
=
A capability

while:

Agent
=
A system that decides how to use capabilities

For example:

Tools:
calculate_square()
calculate_cube()
search_customer()
get_order()

The agent determines which tool is appropriate for the user’s request.

⸻

8. Agent vs Chain

This distinction is extremely important.

Chain

Prompt
↓
LLM
↓
Parser
↓
Output

The path is predetermined.

Agent

Input
↓
Agent
↓
Decision
↓
Tool?
↓
Result
↓
Decision
↓
Final Answer

The path can change depending on the input.

⸻

9. Important Mental Model

Think about an agent as a decision-making loop:

           +----------------+
           |                |
           |     Agent      |
           |                |
           +-------+--------+
                   |
                   v
              Make Decision
                   |
          +--------+--------+
          |                 |
          v                 v
       Finished          Need Tool
          |                 |
          v                 v
       Answer             Tool
                            |
                            v
                       Tool Result
                            |
                            +------→ Agent

The agent keeps going until it determines that it can answer the user.

⸻

10. Files in This Lesson

07-agents/
│
├── README.md
├── 01_basic_agent.py
└── 02_agent_with_multiple_tools.py

01_basic_agent.py

Creates a simple agent with one calculator tool.

02_agent_with_multiple_tools.py

Creates an agent with multiple tools and demonstrates tool selection.

⸻

11. Key Takeaways

You should now understand:

Tool
↓
Provides a capability
LLM
↓
Understands the request
Agent
↓
Uses the LLM + tools
↓
Decides what to do
↓
Loops when necessary

The overall architecture is:

User
↓
Agent
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
Agent
↓
Final Answer

⸻

12. Exercise

Create an agent with these tools:

calculate_square(number)
calculate_cube(number)

Try these questions:

What is the square of 5?

and:

What is the cube of 5?

Then ask:

What is the square of 5 and the cube of 5?

Observe how the agent handles the different requests.

⸻

Next Step

The core LangChain concepts are now covered.

Our next section will be a small LangChain Mini Project that combines the concepts we’ve learned:

Prompt
↓
LLM
↓
Structured Output
↓
Tools
↓
Agent
↓
Final Application

After that, we can start the LangGraph learning repository separately.
