"""
Вариант: 16
367468 % 36 = 16
JSON2XML
"""
from enum import Enum


class Types(Enum):
    Other = 0
    String = 1
    Number = 2


PADDING = "    "
with open('test.json', 'r', encoding='utf-8') as json_file:
    data = json_file.read()[1:-1]
    xml = open('out.xml', 'w', encoding='utf-8')
    xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml.write('<root>\n')
    tags = []
    strFlag = False
    typeFlag = Types.Other
    strBuffer = ""
    for n, i in enumerate(data):
        match i:
            case ":":
                if strFlag:
                    strBuffer += i
                    continue
                tag = strBuffer.replace(",", "").replace(":", "")
                tags.append(tag)
                xml.write(PADDING * len(tags) + f"<{tag}>\n")
                strBuffer = ""
            case "}":
                if strFlag:
                    strBuffer += i
                    continue
                xml.write(PADDING * len(tags) + f"</{tags.pop(-1)}>\n")
            case "{" | " ":
                if strFlag:
                    strBuffer += i
            case '"':
                strFlag = not strFlag
            case "," | "\n":
                if data[n-1] == '"':
                    xml.write(PADDING * (len(tags) + 1) + strBuffer)
                    strBuffer = ""
                    xml.write("\n" + PADDING * len(tags) + f"</{tags.pop(-1)}>\n")
                elif i == ",":
                    strBuffer += i
            case _:
                if strFlag:
                    strBuffer += i

    xml.write('</root>')
    xml.close()
