from src.core.tools.file_parse import FileParser

file_parser = FileParser()
test1 = file_parser.common_parse("测试文本")
test2 = file_parser.common_parse(123)

print(test1, type(test1))
print(test2, type(test2))
