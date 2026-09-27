03 - Chains and LCEL

In the previous lessons, we learned how to work with chat models, messages, and prompt templates.

In this lesson, we will learn how to connect LangChain components together to create a processing pipeline.

This is called a chain.

We will also learn LCEL (LangChain Expression Language), which allows us to compose LangChain components using the | operator.

⸻

What We Will Learn

By the end of this lesson, you will understand:

- What a LangChain chain is.
- How to connect a prompt template to an LLM.
- What an output parser does.
- What LCEL is.
- How the | operator connects components.
- How to compose multiple operations into a pipeline.

⸻

1. What Is a Chain?

A chain connects multiple operations together.

For example:

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

The output from one component becomes the input to the next component.

⸻

2. LCEL

LCEL stands for:

LangChain Expression Language

LCEL provides a simple way to compose LangChain components.

For example:

Prompt | LLM | Parser

The | operator means:

Output of the component on the left
|
v
Input of the component on the right

So:

Prompt
|
v
LLM
|
v
Parser
|
v
Output

can be represented as:

prompt | llm | parser

⸻

3. Basic Chain

File

01_basic_chain.py

This example creates a simple chain consisting of:

1. A chat prompt template
2. Gemini Flash
3. A string output parser

Flow

User Input
|
v
+------------------+
| Prompt Template |
+--------+---------+
|
v
+------------------+
| Gemini Flash |
+--------+---------+
|
v
+------------------+
| StrOutputParser |
+--------+---------+
|
v
Final String

The complete chain can be represented as:

prompt | llm | parser

⸻

4. Output Parser

A chat model normally returns an AIMessage.

For example:

AIMessage
|
+-- content
+-- metadata
+-- other information

StrOutputParser extracts the generated text from the model response.

The flow becomes:

Gemini
|
v
AIMessage
|
v
StrOutputParser
|
v
String

This makes the output easier to use in the rest of an application.

⸻

5. Chain Composition

File

02_chain_composition.py

A chain can itself be combined with another chain.

For example:

Topic
|
v
Explanation Chain
|
v
Summary Chain
|
v
Final Summary

This allows us to build more complex workflows from smaller reusable components.

⸻

6. Why Chains Matter

Chains are useful because they allow us to separate an application into smaller components.

For example:

Prompt
↓
LLM
↓
Parser

Instead of writing everything as one large function, each part has a clear responsibility.

This becomes especially useful when building:

- AI assistants
- RAG applications
- Content generation systems
- Data extraction pipelines
- AI agents

⸻

7. Important Mental Model

Think of LCEL as a data pipeline:

          DATA
            |
            v
      +-----------+
      | Component |
      +-----+-----+
            |
            | output
            v
      +-----------+
      | Component |
      +-----+-----+
            |
            | output
            v
      +-----------+
      | Component |
      +-----+-----+
            |
            v
          RESULT

Every component receives something and produces something.

The next component consumes that output.

⸻

8. Files in This Lesson

03-chains-and-lcel/
│
├── README.md
├── 01_basic_chain.py
└── 02_chain_composition.py

01_basic_chain.py

Demonstrates a basic LCEL chain:

Prompt → LLM → Parser

02_chain_composition.py

Demonstrates how multiple chains can be composed into a larger workflow.

⸻

9. Key Takeaways

After completing this lesson, you should understand:

Chain
=
Multiple LangChain components connected together

and:

LCEL
Prompt | LLM | Parser

The most important concept is:

Output of A
↓
Input of B
↓
Output of B
↓
Input of C

⸻

10. Exercise

Create a chain that accepts a programming topic and generates a short explanation.

For example:

Topic: React useMemo

The chain should:

Topic
↓
Prompt Template
↓
Gemini
↓
String Output Parser
↓
Explanation

Then change the topic to:

Python decorators

without changing the chain structure.

⸻

Next Lesson

In Lesson 4 - Structured Output, we will move beyond plain text responses.

Instead of asking the model to return arbitrary text, we will define the structure we expect.

The workflow will become:

Input
|
v
Prompt
|
v
Gemini
|
v
Structured Schema
|
v
Python Object

This is an important step toward building reliable AI applications.
