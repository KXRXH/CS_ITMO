import sys
import timeit

import json2xml.json2xml
from json2xml.utils import readfromstring

import Lab4_default
import Lab4_with_regex


def test_1():
    padding = " "
    with open('Tests/test.json', 'r', encoding='utf-8') as json_file:
        data = json_file.read()
        try:
            dic = eval(data)
        except (SyntaxError, TypeError) as error:
            print("error: bad json. " + error.msg)
            sys.exit(1)
        with open(f'{json_file.name.replace(".json", "")}.xml', 'w', encoding='utf-8') as xml:
            xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            xml.write('<Расписание>\n')
            xml.write(Lab4_default.converter(dic, padding) + "\n")
            xml.write('</Расписание>')
            xml.close()


def test_2():
    padding = " "
    with open('Tests/test.json', 'r', encoding='utf-8') as json_file:
        data = json_file.read()
        try:
            dic = eval(data)
        except (SyntaxError, TypeError) as error:
            print("error: bad json. " + error.msg)
            sys.exit(1)
        with open(Lab4_with_regex.FILE_PATTERN.sub("_re.xml", json_file.name), 'w', encoding='utf-8') as xml:
            xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            xml.write('<Расписание>\n')
            xml.write(Lab4_with_regex.converter(dic, padding) + "\n")
            xml.write('</Расписание>')
            xml.close()


def test_3():
    with open("Tests/test.json", "r", encoding='utf-8') as json_file:
        with open(f'{json_file.name.replace(".json", "")}_lib.xml', 'w', encoding='utf-8') as xml:
            data = readfromstring(json_file.read())
            xml.write(json2xml.json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml())
            xml.close()


if __name__ == '__main__':
    # number of cycles
    N = 100
    print(":::::TUSK #1 BENCHMARK:::::")
    print(f"Benchmark result: {timeit.timeit('test_1()', number=N, globals=locals())}\n")
    print(":::::TUSK #2 BENCHMARK:::::")
    print(f"Benchmark result: {timeit.timeit('test_2()', number=N, globals=locals())}\n")
    print(":::::TUSK #3 BENCHMARK:::::")
    print(f"Benchmark result: {timeit.timeit('test_3()', number=N, globals=locals())}\n")
