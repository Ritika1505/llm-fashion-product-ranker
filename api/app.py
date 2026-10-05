from fastapi import FastAPI
from graph.workflow import graph

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "LLm Fashion Product Ranker API"}

@app.post("/search")
def search_product(query: str):

    state = {
        "query": query}

    result = graph.invoke(state)

    return {
        "top_products":
        result["ranked_products"][:3],

        "recommendation":
        result["final_recommendation"]}