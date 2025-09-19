# OpenAI Agents SDK – General Concepts & Defaults (Latest SDK)
## 1. Overview

The OpenAI Agents SDK is a framework designed to build intelligent agents that leverage `LLMs (Large Language Models)` to solve tasks autonomously.

**Agents combine:**

- LLM reasoning

- Tools `(external functionalities)`

- Instructions `(guidelines or policies)`

- Context `(memory of past actions or interactions)`

This SDK provides default behaviors and configurations to make agents usable out-of-the-box, while still allowing customization for advanced workflows.

---

## 2. Key Concepts
### 2.1 Agent

**Definition:**
An Agent is a programmatic entity that decides, plans, and executes tasks by interacting with LLMs, tools, and instructions.

**Purpose:**
Provides a structured way to integrate LLM reasoning, tool usage, and context management in one object.

**Example Use Cases:**

- Customer support agent answering FAQs

- Personal finance agent tracking income and expenses

- Educational agent providing study guidance

---

### 2.2 Tools

**Definition:**
Tools are external functions or capabilities that an agent can call during execution. LLMs suggest which tool to use, but execution is handled programmatically.

**Features:**

- Accept parameters

- Return structured outputs

- Can be custom functions or external APIs

**Example:**

```python
def weather_tool(city: str) -> str:
    """
    Weather Tool
    
    Description:
        Ye tool city ka current weather provide karta hai (simulated example).
    
    Parameters:
        city (str): City ka naam, jaise "Karachi", "Lahore"
    
    Returns:
        str: City ka weather status
    """
    
    return f"Today {city} Weather is sunny."
```

### 2.3 Instructions

**Definition:**
Instructions are guidelines that define how the agent should behave, make decisions, or respond.

**Examples:**

- “Always answer politely.”

- “Verify data before responding.”

- “Use simple language.”

**Use in SDK:** Instructions can be provided at agent creation, or dynamically modified per run.


### 2.4 Context

**Definition:**
Context is a memory object that tracks:

- Previous user inputs

- Tool calls

- Agent outputs

**Purpose:** Enables multi-turn conversations, retries, and handoffs between agents.

# 3. Default Behaviors in Latest SDK

The latest OpenAI Agents SDK comes with pre-configured default behaviors that allow agents to function immediately. These defaults include:

| Component       | Default Behavior / Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------------------------|
| Model           | gpt-4.1 if not manually specified                                                     |
| Max Turns       | Typically 3–5 retries before failing                                                      |
| Error Handling  | Automatic try/catch for common errors (timeouts, invalid tool responses, unexpected LLM output) |
| Output Parsing  | Automatic if `output_type` is set (e.g., Python class, dataclass, Pydantic model)       |
| Tool Calling    | Automatic detection & execution based on LLM suggestions                                  |
| Context         | Tracks inputs, outputs, and tool calls                                                   |
| Instructions    | Generic polite/helpful behavior if none provided                                         |

---

## 3.1 Default Model

If no model is specified, the SDK uses **gpt-4.1**.  
This ensures the agent can immediately generate responses without requiring manual model selection.

---

## 3.2 Max Turns

Defines how many times the agent can attempt a solution in multi-step reasoning or retries.  
Exceeding max turns raises `MaxTurnsExceeded`.

---

## 3.3 Error Handling

Common errors handled automatically:  
- Model timeouts  
- Invalid or incomplete tool responses  
- LLM output that cannot be parsed  

**Behavior:** Agent either retries or raises an appropriate exception.

---

## 3.4 Output Parsing

If `output_type` is provided, the agent automatically converts LLM output to that type.  

**Supports:**  
- Python class  
- `dataclass`  
- Pydantic models  

```python
from pydantic import BaseModel

class Answer(BaseModel):
    result: str

response = agent.run("What is the capital of Pakistan?", output_type=Answer)
print(response.result)  # 'Islamabad'
```

## 3.5 Tool Calling

Agent can automatically call tools based on LLM suggestions.
If a tool call fails, agent handles error and optionally retries.

```python
tools = [calculator_tool]
response = agent.run("Calculate 5 * 7", tools=tools)
```

## 3.6 Context & Memory

Automatically maintained: no extra coding required.

**Supports:**

- Multi-turn conversation

- Handoffs

- Tool tracking

```python
agent.run("Remember my name is Areeba")
agent.run("What is my name?")  # Uses context
```

## 3.7 Instructions Default

If no instructions provided, agent uses polite and helpful default behavior.
Ensures agent is ready to use without manual instructions.

# 4. Default Execution Flow

```python
User Input
    ↓
Check Instructions (default if none)
    ↓
Update Context
    ↓
Call LLM (default model gpt-4o-mini if unspecified)
    ↓
Detect & Call Tools (if needed)
    ↓
Parse Output (if output_type set)
    ↓
Error Handling (retry or raise exception)
    ↓
Return Result
```

# 6. Summary

- Agent – central entity that executes tasks intelligently

- Tools – optional external functionalities agent can call

- Instructions – define agent behavior, default is polite/helpful

- Context – memory of all interactions, automatically maintained

- Defaults – allow agent to work immediately: model, max turns, error handling, tool calls, output parsing

With these defaults, the agent is ready-to-use while still allowing developers to customize everything for advanced workflows.