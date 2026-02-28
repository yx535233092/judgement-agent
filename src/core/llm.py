from langchain_openai import ChatOpenAI
from src.utils.config_loader import config
from src.schemas.structor_output import structor_scene_output

# 通用大模型
primary_llm = ChatOpenAI(
    api_key=config.LLM_API_KEY,
    model=config.models.get("llm_model"),
    base_url=config.models.get("model_base_url"),
    temperature=config.models.get("temperature"),
)

# 结构化输出llm
scene_llm = primary_llm.with_structured_output(
    structor_scene_output, method="json_mode"
)
