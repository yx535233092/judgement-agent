from src.core.tools.regular_filter import regular_filer


def test():
    test_res1 = regular_filer("测试文本")
    test_res2 = regular_filer("绝密★3年")
    test_res3 = regular_filer("绝密★长期")
    print(test_res1, test_res2, test_res3)


if __name__ == "__main__":
    test()
