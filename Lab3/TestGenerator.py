ALPHABET = "QWERTYUIOPASDFGHJKLZXCVBNM_+:\}{<>-=?}|\\ ()[]"


def new_test(smile: str) -> (str, int):
    from random import randint
    test_str = ""
    size = randint(10000, 100000)
    for _ in range(size):
        test_str += ALPHABET[randint(0, len(ALPHABET)-1)]
    return test_str, test_str.count(smile)
