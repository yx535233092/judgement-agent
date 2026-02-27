from src.schemas.models import State, ClassificationEnum


# 正向研判
def positive_judge(state: State) -> State:
    messages = [
        {
            "role": "system",
            "content": """
            你是一个专业的保密研判专家。
            请根据用户提供的文本内容，判断其是否属于涉密文件。
            你的判断应当基于严谨的保密标准。
            
            你必须返回一个合法的 JSON 对象，包含以下字段：
            - trace_id: (int) 用于追踪的唯一id，默认为 0
            - classification: (string) 分类标签，只能是 "CONFIDENTIAL", "SUSPICIOUS", 或 "NORMAL"
            - status: (string) 状态，固定为 "SUCCESS"
            - confidence: (float) 置信度 (0.0-1.0)
            - reasoning: (string) 详细的研判理由
            - evidence: (list of strings) 支撑你判断的文本证据片段
            - policy_reference: (string) 参考的定密依据
      """,
        },
        {
            "role": "user",
            "content": f"""
            待研判文本摘要：
            {state.input.summary}
            
            待研判全文：
            {state.input.full_txt}
        """,
        },
    ]

    try:
        # 结构化输出
        from src.core.llm import structured_llm
        result = structured_llm.invoke(messages)
        
        # 因为 structured_llm.with_structured_output(OutputSchema, method="json_mode") 返回 OutputSchema 实例
        if result:
            state.output = result
            
    except Exception as e:
        print(f"研判过程中出错: {e}")
        state.output.status = "FAILTURE"
    
    return state


# 反向研判
def negative_judge(state: State) -> State:
    pass
