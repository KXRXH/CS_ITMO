from pandas import read_json
with open("Tests/test2.json", "r", encoding="utf-8") as json_file:
    try:
        pd_json = read_json(json_file)
    except ValueError as e:
        print("error: bad json.")
        exit(1)
    pd_json.to_csv(f'{json_file.name.replace(".json", "")}.csv', encoding='utf-8')