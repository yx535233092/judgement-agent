from src.core.graph import create_app
from data.mock.input import mock_confidential_input
from src.schemas.state import AgentState


def run():
    # 1. initial LangGraph Application
    app = create_app()

    # 2.initail state
    state: AgentState = {
        "input_data": mock_confidential_input,
        "is_filtered": False,
        "internal_logs": [],  # TypedDict 需要初始化可选字段或确保逻辑正确
    }

    # 4. execute graph
    print(f"--- 开始处理文件：{state['input_data'].file_name} ---")
    final_state = app.invoke(state)

    # 5. output final result
    print("=" * 20)
    print("【研判完成】")
    print(f"最终状态:{final_state}")


if __name__ == "__main__":
    run()
