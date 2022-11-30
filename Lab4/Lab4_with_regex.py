"""
Вариант: 12
JSON2XML
"""
import re
import sys

TEXT_PATTERN = re.compile(r"(.+)")
FILE_PATTERN = re.compile(".json$")
PADDING = "    "


def fix(some_str: str) -> str:
    some_str = re.sub("&", "&amp;", some_str)
    some_str = re.sub('"', "&quot;", some_str)
    some_str = re.sub("'", "&apos;", some_str)
    some_str = re.sub("<", "&lt;", some_str)
    some_str = re.sub(">", "&gt;", some_str)
    some_str = re.sub(r"\\", "", some_str)
    return some_str


def fix_tag(tag: str) -> str:
    tag = re.sub(" ", "_", tag)
    tag = re.sub(r'\\', "", tag)
    tag = re.sub(";", "_", tag)
    tag = re.sub("<", "_lt_", tag)
    tag = re.sub("\"", "_quot_", tag)
    tag = re.sub(":", "_colon_", tag)
    tag = re.sub(">", "_gt_", tag)
    tag = re.sub("'", "_apos_", tag)
    tag = re.sub("\"", "__", tag)
    tag = re.sub("=", "_eq_", tag)
    tag = re.sub("&", "_amp_", tag)
    tag = re.sub(r"\|", "_vl_", tag)
    return tag


def converter(json_object, padding=" "):
    result_list = []
    json_obj_type = type(json_object)
    if json_obj_type is list:
        # Парсинг списка
        for list_element in json_object:
            result_list.append(converter(list_element, padding))
        return "\n".join(result_list)
    if json_obj_type is dict:
        # Парсинг тегов
        for tag in json_object.keys():
            xml_tag = fix_tag(tag)
            result_list.append(TEXT_PATTERN.sub(fr"{padding}<\1>", xml_tag))
            # Вызываем функцию рекурсивно, чтобы учесть данные между тегами
            result_list.append(converter(json_object[tag], PADDING + padding))
            result_list.append(TEXT_PATTERN.sub(fr"{padding}</\1>", xml_tag))
        return "\n".join(result_list)
    return padding + fix(json_object)


with open('Tests/test.json', 'r', encoding='utf-8') as json_file:
    data = json_file.read()
    try:
        dic = eval(data)
    except (SyntaxError, TypeError) as error:
        print("error: bad json. " + error.msg)
        sys.exit(1)
    with open(re.sub(".json$", "_re.xml", json_file.name), 'w', encoding='utf-8') as xml:
        xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        xml.write('<Расписание>\n')
        xml.write(converter(dic, PADDING) + "\n")
        xml.write('</Расписание>')
        xml.close()
