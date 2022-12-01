from re import compile, sub

TIME_PATTERN1 = compile(r'(([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])')
TIME_PATTERN2 = compile(r'(([0-1][0-9]|2[0-3]):[0-5][0-9])')
for i in range(1, 6):
    with open(f'./TestsT2/test{i}', 'r', encoding='utf-8') as TEST:
        TEST_DATA = TEST.read()
        print(f"Тест {i}:\n\"{TEST_DATA}\"")
        print(f"Ответ:\n\"{sub(TIME_PATTERN2, '(TBD)', sub(TIME_PATTERN1, '(TBD)', TEST_DATA))}\"\n")

print("USER-TEST")
n = int(input("Введите количество тестов: "))
for i in range(n):
    test_str = input(f"тест #{i + 1}: ")
    print(f"Ответ:\n\"{sub(TIME_PATTERN2, '(TBD)', sub(TIME_PATTERN1, '(TBD)', test_str))}\"\n")
