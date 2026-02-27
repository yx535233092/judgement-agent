import re


# 正则初筛过滤
def regular_filer(text: str) -> bool:
    reg_exp_pattern = r"(绝密|机密|秘密)\s*★\s*(\d+[年月]|长期|永久|启封前|公开前)"
    result = re.match(reg_exp_pattern, text)
    return bool(result)
