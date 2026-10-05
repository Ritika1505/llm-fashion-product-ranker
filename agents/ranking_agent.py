def ranking_agent(state):

    products = []

    for doc in state["rag_results"]:

        products.append(doc.metadata)

    products.sort(
        key=lambda x: x["discount"],
        reverse=True)

    return {
        "ranked_products": products}