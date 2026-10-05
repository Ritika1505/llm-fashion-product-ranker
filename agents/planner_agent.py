from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2)

def planner_agent(state):

    query = state["query"]

    prompt = f"""
    Find:

    1. Brand
    2. Product Type
    3. Budget

    Query:
    {query}

    Return JSON only.
    """

    response = model.invoke(prompt)

    return {
        "parsed_query": response.content
    }