import streamlit as st

from graph.workflow import graph

st.title("🛍️ LLm Fashion Product Ranker")

st.write("Search products and get recommendations.")

query = st.text_input(
    "Enter your product query")

if st.button("Search"):

    if query:
        with st.spinner("Searching products..."):
            state = {
                "query": query}

            result = graph.invoke(state)

        st.success("Search Completed")

        st.subheader("Top 3 Products")

        products = result["ranked_products"]

        for i, product in enumerate(products[:3], start=1):
            st.write(f"Product {i}")
            st.write(
                f"Brand: {product['brand']}")
            st.write(
                f"Marketplace: {product['marketplace']}"
                )
            st.write(
                f"Price: ₹{product['price']}")
            st.write(
                f"Discount: {product['discount']}%")
            st.write("----------------------")

        st.subheader("LLM Recommendation")
        st.write(
            result["final_recommendation"])

    else:
        st.warning(
            "Please enter a query")