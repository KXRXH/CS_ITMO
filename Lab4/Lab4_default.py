"""
Вариант: 12
JSON2XML
"""
import sys

PADDING = "    "


def fix(some_string: str) -> str:
    """
    Замена спецсимволов
    :param some_string: строка
    :return: измененная строка
    """

    return some_string.replace("&", "&amp;").replace('"', "&quot;") \
        .replace("'", "&apos;").replace("<", "&lt;") \
        .replace(">", "&gt;").replace(r"\\", "")


def fix_tag(tag: str) -> str:
    """
    Замена спецсимволов в тегах
    :param tag: тег
    :return: исправленный тег
    """

    return tag.replace(' ', '_').replace("\\", "") \
        .replace('"', '').replace(";", "_").replace("<", "_lt_") \
        .replace(">", "_gt_").replace("&", "_amp_").replace("'", "_apos_") \
        .replace("=", "_eq_").replace(":", "_colon_").replace("|", "_vl_").replace("\"", "_quot_")


def converter(json_object: str, padding: str = " ") -> str:
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
            result_list.append(padding + f'<{xml_tag}>')
            # Вызываем функцию рекурсивно, чтобы учесть данные между тегами
            result_list.append(converter(json_object[tag], PADDING + padding))
            result_list.append(padding + f"</{xml_tag}>")
        return "\n".join(result_list)
    return padding + fix(json_object)


with open('Tests/test.json', 'r', encoding='utf-8') as json_file:
    data = json_file.read()
    try:
        dic = eval(data)
    except SyntaxError as error:
        print("error: bad json. " + error.msg)
        sys.exit(1)
    with open(f'{json_file.name.replace(".json", "")}.xml', 'w', encoding='utf-8') as xml:
        xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        xml.write('<Расписание>\n')
        xml.write(converter(dic, PADDING) + "\n")
        xml.write('</Расписание>')
        xml.close()
