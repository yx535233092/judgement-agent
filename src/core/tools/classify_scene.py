# 场景判别
from src.schemas.state import AgentState


def classify_scene(state: AgentState) -> str:
    file_name = state["input_data"].file_name
    text = state["input_data"].full_txt

    try:
        from src.core.llm import scene_llm

        scene_llm.invoke(text)
    except Exception as e:
        return f"模型调用失败！{e}"
