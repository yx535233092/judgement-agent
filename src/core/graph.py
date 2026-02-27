from src.schemas.models import State
from langgraph.graph import StateGraph, END
from .nodes.pre_filter import pre_filter


# initial State
def create_app():
    # 1. 初始化图，状态定义
    workflow = StateGraph(State)

    # 2. Set Nodes
    workflow.add_node("pre_filter", pre_filter)

    # 3. Set EntryPoint
    workflow.set_entry_point("pre_filter")

    # 4. Connect Edge
    workflow.add_edge("pre_filter", END)

    # 5. complie
    return workflow.compile()
