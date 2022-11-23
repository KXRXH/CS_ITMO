from collections import Counter
from random import randint
from re import Pattern, compile


class TestGenerator:
    def __init__(self):
        self.__smile_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM_+:}{<>-=?}|\\ ()|[]"
        self.__studs_alphabet = "ИАКМЛВНТ"
        self.__studs_surname_set = ["Котов", "Панов", "Семенов", "Ковалев", "Смирнов", "Поздняков", "Белов",
                                    "Владимиров", "Пахомов", "Петухов", "Филимонов", "Беликов", "Богданов", "Корнилов",
                                    "Губанов", "Колесников", "Филатов", "Рожков", "Григорьев", "Куликов"]

    def smile_test(self, smile: str) -> (str, int):
        test_str = ""
        size = randint(10000, 100000)
        for _ in range(size):
            test_str += self.__smile_alphabet[randint(0, 45)]
        return test_str, test_str.count(smile)

    def studs_test(self) -> ([str], Pattern[str]):
        size = randint(5, 20)
        out = []
        all_groups = []
        for _ in range(size):
            group = f"P{randint(0, 10):04d}"
            surname = self.__studs_surname_set[randint(0, 9)]
            first_name = self.__studs_alphabet[randint(0, 7)]
            second_name = self.__studs_alphabet[randint(0, 7)]
            out.append(f"{surname} {first_name}.{second_name}. {group}")
            all_groups.append(group)
        return out, compile(rf'{Counter(all_groups).most_common(1)}$')
