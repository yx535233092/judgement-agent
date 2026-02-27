from src.core.graph import create_app
from src.schemas.models import InputSchema


def run():
    # 1. initial LangGraph Application
    app = create_app()

    # 2. mock data
    sample_input = InputSchema(
        file_name="2026年财务预算草案.docx",
        summary="绝密 ★ 长期。关于2026年财务预算的详细草案。",
        full_txt="这是某单位2026年的内部财务预算，包含未公开的资金拨付细节...",
        organization="XX局财务处",
        ip="10.0.0.1",
        response_person="张三",
        hit_keywords="财务, 预算, 绝密",
    )

    # 3.initail state
    initial_state = {"input": sample_input}

    # 4. execute graph
    print(f"--- 开始处理文件：{sample_input.file_name} ---")
    final_state = app.invoke(initial_state)

    # 5. output final result
    print("*" * 10)
    print("【研判完成】")
    print(f"最终状态:{final_state}")


if __name__ == "__main__":
    run()
