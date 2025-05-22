from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
import os
import json

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    

llm = ChatOpenAI(model="gpt-4o", temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY"))
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can I help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
     # Debugging: Print the raw response to understand its structure
    print("Raw Response:", raw_response)

    # Ensure raw_response contains the expected structure
    output = raw_response.get("output")
    if output:
        # Clean up the JSON string before parsing
        output = output.replace("\n", "").strip()
        if output.startswith('{"') and output.endswith('}'):
            parsed_output = json.loads(output)
            structured_response = parser.parse(parsed_output)
            print("\nStructured Response:")
            print(f"Topic: {structured_response.topic}")
            print(f"Summary: {structured_response.summary}")
            print(f"Sources: {', '.join(structured_response.sources)}")
            print(f"Tools Used: {', '.join(structured_response.tools_used)}")
        else:
            print("Invalid JSON format in output")
    else:
        print("No output field found in response:", raw_response)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
    print("Raw output:", output)
except Exception as e:
    print("Error:", str(e))
    print("Raw output:", output)
