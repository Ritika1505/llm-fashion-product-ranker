from langgraph.graph import StateGraph

from graph.state import FashionState

from agents.planner_agent import planner_agent
from agents.rag_agent import rag_agent
from agents.ranking_agent import ranking_agent
from agents.recommendation_agent import recommendation_agent

builder = StateGraph(FashionState)

builder.add_node(
    "planner",
    planner_agent)

builder.add_node(
    "rag",
    rag_agent)

builder.add_node(
    "ranking",
    ranking_agent)

builder.add_node(
    "recommendation",
    recommendation_agent)

builder.add_edge(
    "planner",
    "rag")

builder.add_edge(
    "rag",
    "ranking")

builder.add_edge(
    "ranking",
    "recommendation")

builder.set_entry_point(
    "planner")

builder.set_finish_point(
    "recommendation")

graph = builder.compile()

print("Graph Created Successfully")