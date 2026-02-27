from src.core.nodes.pre_filter import pre_filter
from src.schemas.models import (
    State,
    InputSchema,
    OutputSchema,
    ClassificationEnum,
    StatusEnum,
)


def test_pre_filter_confidential():
    """测试识别出涉密标识的情况"""
    input_data = InputSchema(
        file_name="secret_file.docx",
        summary="绝密 ★ 20年",  # 匹配正则
        full_txt="这是非常重要的保密内容...",
        organization="宁波保密局",
        ip="192.168.1.1",
        response_person="王工",
        hit_keywords="",
    )

    output_data = OutputSchema(
        trace_id=1001,
        classification=ClassificationEnum.NORMAL,
        status=StatusEnum.PROGRESS,
        confidence=0.0,
        reasoning="",
        evidence=[],
        policy_reference="",
    )

    state = State(input=input_data, output=output_data)

    # 执行节点
    result_state = pre_filter(state)

    # 断言
    assert result_state.output.classification == ClassificationEnum.CONFIDENTIAL
    assert "涉密文件" in result_state.output.reasoning
    print("✅ 涉密识别测试通过")


def test_pre_filter_normal():
    """测试普通文件不被拦截的情况"""
    input_data = InputSchema(
        file_name="daily_report.txt",
        summary="关于本周工作的日常汇报",
        full_txt="本周完成了代码重构...",
        organization="技术部",
        ip="127.0.0.1",
        response_person="张三",
        hit_keywords="",
    )

    output_data = OutputSchema(
        trace_id=1002,
        classification=ClassificationEnum.NORMAL,
        status=StatusEnum.PROGRESS,
        confidence=1.0,
        reasoning="待研判",
        evidence=[],
        policy_reference="",
    )

    state = State(input=input_data, output=output_data)

    # 执行节点
    result_state = pre_filter(state)

    # 断言分类仍为 NORMAL
    assert result_state.output.classification == ClassificationEnum.NORMAL
    print("✅ 普通文件测试通过")


if __name__ == "__main__":
    test_pre_filter_confidential()
    test_pre_filter_normal()
