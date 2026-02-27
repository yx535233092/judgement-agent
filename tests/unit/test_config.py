from src.utils.config_loader import config


# 配置加载器单元测试
def test_config():
    print("测试config_loader")
    print("=" * 10)
    print("⭐️加载config——setting")
    print(config.models)
    print("=" * 10)
    print("⭐️加载env")
    print(config.LLM_API_KEY)
    pass


if __name__ == "__main__":
    test_config()
