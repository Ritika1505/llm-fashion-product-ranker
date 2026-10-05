# LLM Fashion Product Ranker

An AI-powered fashion product search and comparison application. It retrieves products from a local Chroma vector store, ranks them, and provides a recommendation using an OpenAI language model.

## Features

- Search fashion products using natural-language queries
- Retrieve products using Chroma and OpenAI embeddings
- Rank retrieved products and show up to three recommendations
- Use the product search through a Streamlit interface or FastAPI endpoint
- Rebuild the local vector store from the spreadsheet dataset
- Run the Streamlit interface in Docker

## Tech stack

- Python 3.11
- LangGraph and LangChain
- OpenAI chat and embedding models
- ChromaDB
- Streamlit and FastAPI

## Project structure

```text
agents/                   Planner, retrieval, ranking, and recommendation agents
api/app.py                FastAPI application
data/MarketplaceData.xlsx Source spreadsheet for product ingestion
graph/                    LangGraph workflow and state
UI/streamlit_app.py       Streamlit user interface
vectorstore/              Persisted Chroma database used by the application
ingest.py                 Builds the vector store from the spreadsheet
requirements.txt          Python dependencies
Dockerfile                Docker image definition for the Streamlit app
```

## Setup

Run these commands from the project root. Create and activate a virtual environment if desired, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

Set your OpenAI API key in an environment variable or in a local `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key
```

Do not commit `.env` or real API keys.

## Build or refresh the vector store

The repository includes a `vectorstore/` directory used by the app. To recreate it from the spreadsheet, run this from the project root:

```bash
python ingest.py
```

Ingestion calls OpenAI embeddings and therefore requires a valid `OPENAI_API_KEY`. The spreadsheet is read from `data/MarketplaceData.xlsx`; the generated Chroma database is written to `vectorstore/`.

## Run the Streamlit app

From the project root:

```bash
streamlit run UI/streamlit_app.py
```

## Run the FastAPI app

In a separate terminal, from the project root:

```bash
uvicorn api.app:app --reload
```

The API provides `GET /` and `POST /search?query=...`. Interactive API documentation is available at `/docs` while the server is running.

## Docker

Build the Docker image from the project root:

```bash
docker build -t llm-fashion-product-ranker .
```

Pass the API key when starting the container:

```bash
docker run --rm -p 8501:8501 --env-file .env llm-fashion-product-ranker
```

Then open `http://localhost:8501`. The image runs the Streamlit app; the FastAPI server is run separately using the command above.

