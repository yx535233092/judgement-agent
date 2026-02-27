from pydantic_settings import BaseSettings
from pydantic import Field
import os
import yaml


class Settings(BaseSettings):
    # .env变量
    LLM_API_KEY: str = Field(default=None)
    LLM_BASE_URL: str = Field(default=None)

    models: dict = {}
    # pydantic配置
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


def load_settings(config_path: str = "configs/settings.yaml") -> Settings:
    settings = Settings()
    # 加载配置文件
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            yaml_data = yaml.safe_load(f)
            settings.models = yaml_data.get("models", {})
    else:
        raise FileNotFoundError(f"Config file not found: {config_path}")

    return settings


# 单例模式加载配置
config = load_settings()
