import json2xml.json2xml
from json2xml.utils import readfromstring

with open("Tests/test.json", "r", encoding='utf-8') as json_file:
    xml = open(f'{json_file.name.replace(".json", "")}_lib.xml', 'w', encoding='utf-8')
    data = readfromstring(json_file.read())
    xml.write(json2xml.json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml())
    xml.close()
