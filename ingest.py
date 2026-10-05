#Loading Libraries
import pandas as pd
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from pathlib import Path

load_dotenv()

#Loding Data
data_path = Path(__file__).resolve().parent / "data" / "MarketplaceData.xlsx"
df = pd.read_excel(data_path)

documents = []

for _, row in df.iterrows():

    text = f"""
    Marketplace: {row['marketplace']}
    Brand: {row['brand']}
    Product: {row['item_name']}
    Category: {row['category']}
    Price: {row['item_price']}
    Discount: {row['discount']}
    """
#Creating Document Objects
    doc = Document(
        page_content=text,
        metadata={
            "marketplace": row["marketplace"],
            "brand": row["brand"],
            "product": row["item_name"],
            "category": row["category"],
            "price": row["item_price"],
            "discount": row["discount"],
            "link": row["item_link"]})

    documents.append(doc)

print("Documents:", len(documents))

#Creating Embeddings and Vector Store
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",)

vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="vectorstore")

print("Vector Store Created Successfully")