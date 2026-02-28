from jinja2 import Template
from src.core.llm import positive_llm
from src.schemas.structor_output import structor_positive_output
from src.schemas.state import AgentState
import yaml


# 正向研判
def positive_judge(state: AgentState) -> AgentState:
    with open("configs/prompts/positive_judge.yaml", "r", encoding="utf-8") as f:
        prompt_config = yaml.safe_load(f)

    sys_tmpl = Template(prompt_config["system_prompt"])
    user_tmpl = Template(prompt_config["user_prompt"])

    messages = [
        {
            "role": "system",
            "content": sys_tmpl.render(
                scene=state["scene"], active_policies=state["active_policies"]
            ),
        },
        {
            "role": "user",
            "content": user_tmpl.render(
                scene=state["scene"], full_txt=state["input_data"].full_txt
            ),
        },
    ]

    try:
        result: structor_positive_output = positive_llm.invoke(messages)
        verdict = result["verdict"]
        confidence = result["confidence"]
        reasoning = result["reasoning"]
        evidence = result["evidence"]

    except Exception as e:
        print(f"研判过程中出错: {e}")
        state.output.status = "FAILURE"

    return {
        "positive_analysis": {
            "verdict": verdict,
            "confidence": confidence,
            "reasoning": reasoning,
            "evidence": evidence,
        }
    }


# 反向研判
def negative_judge(state: AgentState) -> AgentState:
    with open("configs/prompts/negative_judge.yaml", "r", encoding="utf-8") as f:
        prompt_config = yaml.safe_load(f)

    sys_tmpl = Template(prompt_config["system_prompt"])
    user_tmpl = Template(prompt_config["user_prompt"])

    messages = [
        {
            "role": "system",
            "content": sys_tmpl.render(scene=state["scene"]),
        },
        {
            "role": "user",
            "content": user_tmpl.render(
                scene=state["scene"], full_txt=state["input_data"].full_txt
            ),
        },
    ]

    try:
        result: structor_positive_output = positive_llm.invoke(messages)
        verdict = result["verdict"]
        confidence = result["confidence"]
        reasoning = result["reasoning"]
        evidence = result["evidence"]

    except Exception as e:
        print(f"研判过程中出错: {e}")
        state.output.status = "FAILURE"

    return {
        "negative_analysis": {
            "verdict": verdict,
            "confidence": confidence,
            "reasoning": reasoning,
            "evidence": evidence,
        }
    }
