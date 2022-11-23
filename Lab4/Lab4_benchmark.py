def test_1():
    import Lab4_default
    PADDING = " "
    with open('Tests/test2.json', 'r', encoding='utf-8') as json_file:
        data = json_file.read()
        try:
            dic = eval(data)
        except SyntaxError or TypeError as e:
            print("error: bad json. " + e.msg)
            exit(1)
        xml = open(f'{json_file.name.replace(".json", "")}.xml', 'w', encoding='utf-8')
        xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        xml.write('<Расписание>\n')
        xml.write(Lab4_default.converter(dic, PADDING) + "\n")
        xml.write('</Расписание>')
        xml.close()


def test_2():
    import Lab4_with_regex
    PADDING = " "
    with open('Tests/test2.json', 'r', encoding='utf-8') as json_file:
        data = json_file.read()
        try:
            dic = eval(data)
        except SyntaxError or TypeError as e:
            print("error: bad json. " + e.msg)
            exit(1)
        xml = open(Lab4_with_regex.FILE_PATTERN.sub("_re.xml", json_file.name), 'w', encoding='utf-8')
        xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        xml.write('<Расписание>\n')
        xml.write(Lab4_with_regex.converter(dic, PADDING) + "\n")
        xml.write('</Расписание>')
        xml.close()


def test_3():
    import json2xml.json2xml
    from json2xml.utils import readfromstring
    with open("Tests/test.json", "r", encoding='utf-8') as json_file:
        xml = open(f'{json_file.name.replace(".json", "")}_lib.xml', 'w', encoding='utf-8')
        data = readfromstring(json_file.read())
        xml.write(json2xml.json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml())
        xml.close()


if __name__ == '__main__':
    import timeit
    # number of cycles
    n = 100
    print(":::::TUSK #1 BENCHMARK:::::")
    print("Benchmark result: %fs\n" % timeit.timeit("test_1()", number=n, globals=locals()))
    print(":::::TUSK #2 BENCHMARK:::::")
    print("Benchmark result: %fs\n" % timeit.timeit("test_2()", number=n, globals=locals()))
    print(":::::TUSK #3 BENCHMARK:::::")
    print("Benchmark result: %fs" % timeit.timeit("test_3()", number=n, globals=locals()))
