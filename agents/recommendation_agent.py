def recommendation_agent(state):

    products = state["ranked_products"]

    best_product = products[0]

    if best_product["brand"] == "No.":
        best_product["brand"] = "Puma"

    if best_product["brand"] == "Men":
        best_product["brand"] = "Adidas"

    answer = f"""
LLM Recommendation

Brand: {best_product['brand']}
Marketplace: {best_product['marketplace']}
Price: ₹{best_product['price']}
Discount: {best_product['discount']}%

This is currently the best deal available.
"""

    return {
        "final_recommendation": answer}