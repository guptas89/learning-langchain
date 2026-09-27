05 - Runnables

In the previous lesson, we learned about structured output.

We also used LCEL expressions such as:

prompt | llm | parser

In this lesson, we will understand what is actually being connected by the | operator.

These components are called Runnables.

⸻

What We Will Learn

By the end of this lesson, you will understand:

- What a Runnable is.
- Why LangChain uses Runnables.
- RunnableLambda.
- RunnablePassthrough.
- RunnableParallel.
- How Runnables work with LCEL.
- How data flows between Runnables.

⸻

1. What Is a Runnable?

A Runnable is a component that follows a common interface for processing input and producing output.

Conceptually:

Input
|
v
+-----------+
| Runnable |
+-----+-----+
|
v
Output

A Runnable can represent different kinds of operations.

For example:

Prompt Template
Chat Model
Output Parser
Python Function
Parallel Operations

Many of these components can be connected because they follow the Runnable interface.

⸻

2. Why Runnables Matter

Runnables give LangChain a common way to compose components.

For example:

Prompt
|
v
LLM
|
v
Parser

can be written using LCEL:

prompt | llm | parser

The components can be connected because they behave like Runnables.

⸻

3. RunnableLambda

RunnableLambda allows us to turn a normal Python function into a Runnable.

For example:

Python Function
|
v
RunnableLambda
|
v
Runnable

This allows normal application logic to participate in an LCEL pipeline.

Example

A Python function:

add_prefix("React")

could produce:

"Technology: React"

That function can then be connected to other LangChain components.

⸻

4. RunnablePassthrough

RunnablePassthrough simply passes the input through without changing it.

Input
|
v
RunnablePassthrough
|
v
Same Input

It becomes useful when we want to preserve input while creating a larger pipeline.

⸻

5. RunnableParallel

RunnableParallel allows multiple operations to run on the same input.

For example:

                 Input
                   |
          +--------+--------+
          |                 |
          v                 v
      Operation A       Operation B
          |                 |
          v                 v
       Result A          Result B
          |                 |
          +--------+--------+
                   |
                   v
              Combined

This is useful when different pieces of information need to be generated or processed independently.

⸻

6. Runnable Composition

Runnables can be connected together.

For example:

Input
|
v
Runnable A
|
v
Runnable B
|
v
Runnable C
|
v
Output

Using LCEL:

runnable_a | runnable_b | runnable_c

This is the same composition model we saw in Lesson 3.

⸻

7. Data Flow

One of the most important things to understand is the shape of the data moving through the pipeline.

For example:

"React"
|
v
RunnableLambda
|
v
"Technology: React"
|
v
Prompt
|
v
Chat Model
|
v
AI Response

Every component receives some input and produces some output.

Understanding these input/output shapes makes debugging LCEL pipelines much easier.

⸻

8. RunnableParallel Example

Suppose we have:

Input: React

We might want to create:

{
"definition": "...",
"use_case": "..."
}

We can run two operations using the same input:

                  React
                    |
          +---------+---------+
          |                   |
          v                   v
     Definition           Use Case
          |                   |
          +---------+---------+
                    |
                    v
              Combined Result

This is the basic idea behind RunnableParallel.

⸻

9. Files in This Lesson

05-runnables/
│
├── README.md
├── 01_runnable_basics.py
└── 02_runnable_composition.py

01_runnable_basics.py

Demonstrates:

- RunnableLambda
- RunnablePassthrough

02_runnable_composition.py

Demonstrates:

- Runnable composition
- RunnableParallel
- Combining multiple operations

⸻

10. Key Takeaways

The most important concept is:

Runnable
=
A component that receives input
and produces output.

LCEL then allows us to connect these components:

A | B | C

which means:

A
↓
B
↓
C

The main Runnables introduced in this lesson are:

RunnableLambda
RunnablePassthrough
RunnableParallel

⸻

11. Exercise

Create a RunnableLambda that accepts a programming language and returns:

"Learning: <language>"

For example:

Input:
Python
Output:
Learning: Python

Then connect it to another Runnable that converts the result to uppercase.

The final flow should be:

Python
|
v
RunnableLambda
|
v
"Learning: Python"
|
v
RunnableLambda
|
v
"LEARNING: PYTHON"

⸻

Next Lesson

In Lesson 6 - Tools, we will connect an LLM to external functions.

The basic architecture will become:

User
|
v
LLM
|
| decides whether a tool is needed
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
Final Response

This is an important step toward understanding AI agents.
