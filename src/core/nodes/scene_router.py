from src.core.tools.policy_manager import get_policy_by_scene
from src.core.llm import scene_llm
from src.schemas.state import AgentState
import yaml
from jinja2 import Template
from src.schemas.structor_output import structor_scene_output


def router_node(state: AgentState):
    # 加载提示词
    with open("configs/prompts/scene_classify.yaml", "r", encoding="utf-8") as f:
        prompt_config = yaml.safe_load(f)

    # 场景列表
    available_scenes = [
        {
            "name": "FIRE_SAFETY",
            "description": "涉及火灾预防、灭火器材、消防工程部署等。",
        },
        {"name": "TECH", "description": "涉及软件代码、芯片架构、前沿技术研发等。"},
        {"name": "GENERAL", "description": "通用办公、行政通知、基础法律等。"},
    ]

    # 提示词渲染
    sys_tmpl = Template(prompt_config["system_prompt"])
    user_tmpl = Template(prompt_config["user_prompt"])

    # 具体输入信息
    messages = [
        {
            "role": "system",
            "content": sys_tmpl.render(available_scenes=available_scenes),
        },
        {
            "role": "user",
            "content": user_tmpl.render(
                file_name=state["input_data"].file_name,
                text=state["input_data"].full_txt,
            ),
        },
    ]

    try:
        result: structor_scene_output = scene_llm.invoke(messages)

        scene = result["scene_key"]
        active_policies = get_policy_by_scene(scene)

    except Exception as e:
        scene = "GENERAL"

    return {
        "scene": scene,
        "active_policies": active_policies,
        "internal_logs": [f"场景识别原因：{result['reason']}"],
    }
