from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

def rag_agent(state):

    query = state["query"]

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small",)

    db = Chroma(
        persist_directory="vectorstore",
        embedding_function=embedding_model)

    retriever = db.as_retriever(
        search_kwargs={"k": 5})

    results = retriever.invoke(query)

    return {
        "rag_results": results}