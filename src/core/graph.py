from src.schemas.state import AgentState
from langgraph.graph import StateGraph, END
from .nodes.pre_filter import pre_filter
from .nodes.scene_router import router_node


# initial State
def create_app():
    # 1. 初始化图，状态定义
    workflow = StateGraph(AgentState)

    # 2. Set Nodes
    workflow.add_node("pre_filter", pre_filter)
    workflow.add_node("scene_router", router_node)

    # 3. Set EntryPoint
    workflow.set_entry_point("pre_filter")

    # 4. Connect Edge
    workflow.add_conditional_edges(
        "pre_filter",
        lambda state: "scene_router" if not state["is_filtered"] else END,
        {"scene_router": "scene_router", END: END},
    )

    # 5. complie
    return workflow.compile()
