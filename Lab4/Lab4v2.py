"""
Вариант: 16
367468 % 36 = 16
JSON2XML
"""


def json2xml(json_object, padding=" "):
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
            xml_tag = tag.replace(' ', '_')
            result_list.append(padding + f"<{xml_tag}>")
            # Вызываем функцию рекурсивно, чтобы учесть данные между тегами
            result_list.append(json2xml(json_object[tag], PADDING + padding))
            result_list.append(padding + f"</{xml_tag}>")
        return "\n".join(result_list)
    return padding + json_object


PADDING = "    "
with open('test2.json', 'r', encoding='utf-8') as json_file:
    data = json_file.read()
    xml = open(f'{json_file.name.replace(".json", "")}.xml', 'w', encoding='utf-8')
    xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml.write('<root>\n')
    xml.write(json2xml(eval(data), PADDING) + "\n")
    xml.write('</root>')
    xml.close()
