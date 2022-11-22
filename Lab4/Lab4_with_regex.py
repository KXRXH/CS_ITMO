"""
Вариант: 12
JSON2XML
"""
import re

TEXT_PATTERN = re.compile(r"(.+)")
FILE_PATTERN = re.compile(".json$")


def json2xml(json_object, padding=" ", space="_"):
    global PADDING
    result_list = []
    json_obj_type = type(json_object)
    if json_obj_type is list:
        """
        Парсинг списка
        """
        for list_element in json_object:
            result_list.append(json2xml(list_element, padding))
        return "\n".join(result_list)
    elif json_obj_type is dict:
        """
        Парсинг тегов
        """
        for tag in json_object.keys():
            xml_tag = re.sub(" ", space, tag)
            result_list.append(TEXT_PATTERN.sub(fr"{padding}<\1>", xml_tag))
            # Вызываем функцию рекурсивно, чтобы учесть данные между тегами
            result_list.append(json2xml(json_object[tag], PADDING + padding))
            result_list.append(TEXT_PATTERN.sub(fr"{padding}</\1>", xml_tag))
        return "\n".join(result_list)
    return padding + json_object


PADDING = "    "
with open('Tests/test2.json', 'r', encoding='utf-8') as json_file:
    data = json_file.read()
    try:
        dic = eval(data)
    except SyntaxError as e:
        print("error: bad json. " + e.msg)
        exit(1)
    xml = open(re.sub(".json$", "_re.xml", json_file.name), 'w', encoding='utf-8')
    xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml.write('<Расписание>\n')
    xml.write(json2xml(dic, PADDING) + "\n")
    xml.write('</Расписание>')
    xml.close()
