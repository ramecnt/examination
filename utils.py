import json
import datetime

def load_all():
    with open("data/data1.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_by_day():
    day = datetime.date.today().isoweekday()
    result = []
    for i in load_all():
        if day < 6 and (i["days"] == "ежедн." or i["days"] == "раб."):
            result.append(i)
        elif (day == 6 or day == 7) and (i["days"] == "вых" or i["days"] == "ежедн."):
            result.append(i)
    return result

def load_by_pk(pk):
    for i in range(len(load_all())):
        if i+1 == pk:
            print(load_all()[i+1])
