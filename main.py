import os

from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    Runner,
    set_tracing_disabled
)

load_dotenv()

GEMINI_MODEL= os.getenv("GEMINI_API_KEY")
BASE_URL= "https://generativelanguage.googleapis.com/v1beta/openai/"

set_tracing_disabled(True)

client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_MODEL,
    base_url= BASE_URL
)

model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

# Creating the agent with initial instructions
agent: Agent = Agent(
    name="Math Tutor",
    instructions="You help with math problems. Explain your reasoning step by step and provide examples.",
    model=model
)

# Running the agent
result: Runner = Runner.run_sync(agent, "What is 5 + 3?")
print("Result 1: ", result.final_output)

# Updating instructions at runtime
agent.instructions = "Use simple and clear language. And if addition appears, give the subtraction result instead."

# Running the agent again with new instructions
result: Runner = Runner.run_sync(agent, "What is 5 + 3?")
print("Result 2: ", result.final_output)

