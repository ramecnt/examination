import json
import datetime


def load_all():
    """ Функция на вход ничего не принимает и возвращает содержимое файла data1.json в формате json  """
    with open("data/data1.json", "r", encoding="utf-8") as f:
        return json.load(f)


def load_by_day():
    """ Функция на вход ничего не принимает и
     возвращает маршруты электричек по сегодняшняму дню недели в формате json  """
    # Определение номера сегодняшнего дня недели
    day = datetime.date.today().isoweekday()
    result = []
    for i in load_all():
        if day < 6 and (i["days"] == "ежедн." or i["days"] == "раб."):
            result.append(i)
        elif (day == 6 or day == 7) and (i["days"] == "вых" or i["days"] == "ежедн."):
            result.append(i)
    return result


def load_by_number(pk):
    """
    Возвращает все маршруты электрички по ее номеру в формате json

                    Parameters:
                            pk (str): номер электрички
                    Returns:
                            result (json): список всех маршрутов электрчки по заданому номер
    """
    result = []
    # проверка на правильность данных которые ввел пользователь
    try:
        pk = int(pk)
    except (ValueError, TypeError):
        return "<h2>Вы ввели не номер</h2>"
    for i in load_by_day():
        if i["number"] == int(pk):
            result.append(i)
    return result

def load_by_pk(pk):
    for i in range(len(load_all())):
        if i+1 == pk:
            return load_all()[i]

