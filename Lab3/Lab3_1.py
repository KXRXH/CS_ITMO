"""
██╗░░░░░░█████╗░██████╗░░█████╗░    ███╗░░██╗░█████╗░███╗░░░███╗███████╗██████╗░    ██████╗░
██║░░░░░██╔══██╗██╔══██╗██╔══██╗    ████╗░██║██╔══██╗████╗░████║██╔════╝██╔══██╗    ╚════██╗
██║░░░░░███████║██████╦╝███████║    ██╔██╗██║██║░░██║██╔████╔██║█████╗░░██████╔╝    ░█████╔╝
██║░░░░░██╔══██║██╔══██╗██╔══██║    ██║╚████║██║░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗    ░╚═══██╗
███████╗██║░░██║██████╦╝██║░░██║    ██║░╚███║╚█████╔╝██║░╚═╝░██║███████╗██║░░██║    ██████╔╝
╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝    ╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝    ╚═════╝░
──────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████────██████████████────██████████████────██████──██████────██████████████────██████████████─
─██░░░░░░░░░░██────██░░░░░░░░░░██────██░░░░░░░░░░██────██░░██──██░░██────██░░░░░░░░░░██────██░░░░░░░░░░██─
─██████████░░██────██░░██████████────██████████░░██────██░░██──██░░██────██░░██████████────██░░██████░░██─
─────────██░░██────██░░██────────────────────██░░██────██░░██──██░░██────██░░██────────────██░░██──██░░██─
─██████████░░██────██░░██████████────────────██░░██────██░░██████░░██────██░░██████████────██░░██████░░██─
─██░░░░░░░░░░██────██░░░░░░░░░░██────────────██░░██────██░░░░░░░░░░██────██░░░░░░░░░░██────██░░░░░░░░░░██─
─██████████░░██────██░░██████░░██────────────██░░██────██████████░░██────██░░██████░░██────██░░██████░░██─
─────────██░░██────██░░██──██░░██────────────██░░██────────────██░░██────██░░██──██░░██────██░░██──██░░██─
─██████████░░██────██░░██████░░██────────────██░░██────────────██░░██────██░░██████░░██────██░░██████░░██─
─██░░░░░░░░░░██────██░░░░░░░░░░██────────────██░░██────────────██░░██────██░░░░░░░░░░██────██░░░░░░░░░░██─
─██████████████────██████████████────────────██████────────────██████────██████████████────██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
import configparser
import re
from re import compile, Pattern

from TestGenerator import TestGenerator

"""
 4: =
 0: -
 3: |
"""
cfg = configparser.ConfigParser()
generator = TestGenerator()
cfg.read('TESTS.ini')
SMILE = input()
# SMILE = "=-|"
SMILE_PATTERN: Pattern[str] = compile(re.escape(SMILE))
for i in range(1, 6):
    with open(f'./TestsT1/test{i}', 'r', encoding='utf-8') as TEST:
        TEST_DATA = TEST.read()
        print(f"TEST {i}\nТестовая строка: \"{TEST_DATA}\"")
        print(f"Верный ответ: {cfg['TUSK1'][f'TEST{i}']}")
        print(f"Ответ полученный через RegExp: {len(SMILE_PATTERN.findall(TEST_DATA))}\n")

print("USER-TEST")
n = int(input("Введите количество тестов: "))
for i in range(n):
    test_str = input(f"тест #{i + 1}: ")
    print(f"Ответ: {len(SMILE_PATTERN.findall(test_str))}\n")
