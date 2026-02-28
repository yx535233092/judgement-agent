from src.core.nodes.scene_router import router_node
from data.mock.input import mock_scene_input
from src.schemas.state import AgentState


def test():
    state: AgentState = {
        "input_data": mock_scene_input,
        "is_filtered": False,
        "internal_logs": [],  # TypedDict 需要初始化可选字段或确保逻辑正确
    }
    print(router_node(state))


if __name__ == "__main__":
    test()
