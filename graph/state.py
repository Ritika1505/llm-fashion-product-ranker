from typing import TypedDict

class FashionState(TypedDict):

    query: str

    parsed_query: str

    rag_results: list

    ranked_products: list

    final_recommendation: str