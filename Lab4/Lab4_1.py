"""
Вариант: 16
367468 % 36 = 16
JSON2XML
"""
PADDING = "    "
with open('test.json', 'r', encoding='utf-8') as json_file:
    data = json_file.read()[1:-1]
    xml = open('out.xml', 'w', encoding='utf-8')
    xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml.write('<root>\n')
    tags = []
    strFlag = False
    tagBuff = ""
    in_tag = False
    for n, i in enumerate(data):
        print(tagBuff, tags, in_tag, strFlag)
        if tagBuff == "Конец":
            ...
        match i:
            case ":":
                if strFlag:
                    tagBuff += i
                    continue
                tag = tagBuff.replace(",", "").replace(":", "")
                tags.append(tag)
                xml.write(PADDING * len(tags) + f"<{tag}>\n")
                tagBuff = ""
                if not strFlag:
                    in_tag = True
            case "}":
                if not strFlag:
                    in_tag = False
                    xml.write(PADDING * len(tags) + f"</{tags.pop(-1)}>\n")
            case "{" | " ":
                ...
            case '"':
                strFlag = not strFlag
            case "," | "\n":
                if data[n-1] == '"':
                    xml.write(PADDING * (len(tags) + 1) + tagBuff)
                    tagBuff = ""
                    xml.write("\n" + PADDING * len(tags) + f"</{tags.pop(-1)}>\n")
                elif i == ",":
                    tagBuff += i
            case _:
                if strFlag:
                    tagBuff += i

    xml.write('</root>')
    xml.close()
