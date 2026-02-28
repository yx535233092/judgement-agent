from src.schemas.state import AgentState
from src.core.nodes.judge import negative_judge
from data.mock.input import mock_scene_input


def test():
    state: AgentState = {
        "input_data": mock_scene_input,
        "is_filtered": False,
        "scene": "FIRE_SAFETY",
        "active_policies": "1. **体制机制改革政策部署**: 涉及消防救援体制机制改革等重大事项的方针政策、工作部署.\n2. **涉恐涉暴火灾事故处置**: 与民族分裂、暴力恐怖、极端宗教活动有关的火灾事故和应急救援事件的处置、调查、原因分析等.\n3. **核生化战争灾难应急处置**: 涉及核与辐射、生物、化学事故、战争灾难的应急处置、调查情况等.\n4. **消防工程师考试试题标准**: 注册消防工程师职业资格全国统一考试的试题、试卷（含备用卷）、标准答案、评分标准等.\n5. **消防工程师考试命题安排**: 注册消防工程师职业资格全国统一考试的命题、试卷印制工作安排和人员组成情况.\n6. **重大火灾事故责任认定**: 造成10人以上死亡，50人以上重伤，或者500万元以上直接财产损失的火灾及社会影响度高、有影响的火灾事故调查的责任认定以及对事故责任的处理建议等.\n7. **国际合作交流对策措施**: 消防救援工作国际合作交流的内部考虑、对策措施等.",
        "internal_logs": [],  # TypedDict 需要初始化可选字段或确保逻辑正确
    }
    print(negative_judge(state))


if __name__ == "__main__":
    test()
