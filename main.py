from typing import TypedDict, List
from langgraph.graph import StateGraph
import math


class AgentState(TypedDict):
    values: List[int]
    name: str
    operation: str
    message: str


def process_state(state: AgentState) -> AgentState:
    result = 0
    if state["operation"] == "-":
        result = state["values"][0] - sum(state["values"][1:])
    elif state["operation"] == "+":
        result = sum(state["values"])
    elif state["operation"] == "*":
        result = math.prod(state["values"])
    elif state["operation"] == "/":
        result = state["values"][0] / math.prod(state["values"][1:])
    state["message"] = f"Hi, {state['name']}, your answer is {result}"
    return state


graph = StateGraph(AgentState)
graph.add_node("processor", process_state)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

result = app.invoke({"values": [1, 2, 3], "name": "Jonah", "operation": "-"})

print("Result: ", result["message"])

# Result: Hi, Jonah, your answer is -4