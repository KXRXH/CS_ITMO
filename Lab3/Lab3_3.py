from re import compile, findall
import configparser

from TestGenerator import TestGenerator

cfg = configparser.ConfigParser()
generator = TestGenerator()
cfg.read("./TESTS.ini")
NAME_PATTERN = compile(r'(([A-Z]|[А-Я])\.)\1')


def test(test_data, group_pattern):
    global NAME_PATTERN
    c = 0
    for row in test_data:
        print(row)
    print("Ответ:")
    for row in test_data:
        if len(findall(group_pattern, row)) and len(findall(NAME_PATTERN, row)):
            continue
        print(row)
    print()


for i in range(1, 6):
    with open(f'./TestsT3/test{i}', 'r', encoding='utf-8') as TEST:
        TEST_DATA = [i.replace("\n", "") for i in TEST]
        GROUP_PATTERN = compile(rf'{cfg["TUSK3"][f"TEST{i}"]}$')
        print(f"Тест {i}:")
        test(TEST_DATA, GROUP_PATTERN)

print("АВТО-ТЕСТЫ")
for i in range(1, 6):
    data, group = generator.studs_test()
    print(f"AUTO-TEST {i}")
    test(data, group)
