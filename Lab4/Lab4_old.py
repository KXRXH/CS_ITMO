"""
Вариант: 16
367468 % 36 = 16
JSON2XML
"""


PADDING = "    "
with open('Tests/test2.json', 'r', encoding='utf-8') as json_file:
    data = json_file.read()[1:-1]
    xml = open(f'{json_file.name.replace(".json", "")}.xml', 'w', encoding='utf-8')
    xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml.write('<root>\n')
    tags = []
    strFlag = False
    strBuffer = ""
    for n, i in enumerate(data):
        match i:
            case ":":
                if strFlag:
                    strBuffer += i
                    continue
                tag = strBuffer.replace(",", "").replace(":", "").replace(" ", "_")
                tags.append(tag)
                xml.write(PADDING * len(tags) + f"<{tag}>\n")
                strBuffer = ""
            case "}":
                if strFlag:
                    strBuffer += i
                    continue
                elif data[n-1] == '"':
                    xml.write(PADDING * (len(tags) + 1) + strBuffer)
                    strBuffer = ""
                    xml.write("\n" + PADDING * len(tags) + f"</{tags.pop(-1)}>\n")
                xml.write(PADDING * len(tags) + f"</{tags.pop(-1)}>\n")
            case "{" | " ":
                if strFlag:
                    strBuffer += i
            case '"':
                if data[n-1] == "\\":
                    strBuffer += i
                    continue
                strFlag = not strFlag
            case "," | "\n":
                if data[n-1] == '"':
                    xml.write(PADDING * (len(tags) + 1) + strBuffer)
                    strBuffer = ""
                    xml.write("\n" + PADDING * len(tags) + f"</{tags.pop(-1)}>\n")
                elif strFlag and i == ",":
                    strBuffer += i
            case _:
                if strFlag:
                    strBuffer += i
    xml.write('</root>')
    xml.close()
