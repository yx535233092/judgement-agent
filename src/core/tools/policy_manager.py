def get_policy_by_scene(scene: str) -> str:
    policy_map = {
        "FIRE_SAFETY": "data/policies/fire_safety.md",
        "TECH": "data/policies/tech.md",
        "GENERAL": "data/policies/general.md",
    }

    file_path = policy_map.get(scene, "data/policies/general.md")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
