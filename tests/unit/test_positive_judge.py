from src.core.nodes.judge import positive_judge
from data.mock.input import mock_judgement_input
from src.schemas.models import State, OutputSchema


def test():
    # 使用 State 类初始化，而不是字典
    state = State(input=mock_judgement_input, output=OutputSchema())
    result = positive_judge(state)
    print(f"研判: {result.output}")
    print(f"研判结果: {result.output.classification}")


if __name__ == "__main__":
    test()
