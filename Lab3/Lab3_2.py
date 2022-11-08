from re import compile,sub
import configparser

cfg = configparser.ConfigParser()
cfg.read("./TESTS.ini")
TIME_PATTERN = compile(r'(([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])|(([0-1]?[0-9]|2[0-3]):[0-5][0-9])')
for i in range(1, 6):
    with open(f'./TestsT2/test{i}', 'r') as TEST:
        TEST_DATA = TEST.read()
        print(f"Тест {i}:\n\"{TEST_DATA}\"")
        print(f"Ответ:\n\"{sub(TIME_PATTERN, '(TBD)', TEST_DATA)}\"\n")
        # print(f"Ответ: {}\n")