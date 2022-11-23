import re


# ^(00|\+)(\d{1,2})\((\d{3,6})\)(\d{3})-(\d{2})(-\d{2})?$


def check_number(_number):
    if _number.count("(") and len(re.sub(r"[ |\-|\)]", "", _number.split("(")[1])) == 10 and re.match(
            r"^(00|\+)(\d{1,2})\((\d{3,6})\)(\d{3})-(\d{2})(-\d{2})?$",
            _number):
        return f"{_number} is valid"
    return f"{_number} is invalid"


tests = [
    "+8(222)444-33-22",
    "0012(7655)233-12",
    "001(765)233-12-55",
    "001(7651)233-12-52",
    "-013(76531)233-12",
    "+013(76531)233-12",
    "+13(76531)233-12"
]
number = input()
print(check_number(number))
for i in tests:
    print(check_number(i))
