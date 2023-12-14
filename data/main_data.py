import os
import pandas

import json
from scripts.gtime import get_date, get_day

groups = {"дбо-101рпо": 'd101.xlsx', 'дбо-102рпо': "d102.xlsx", "дбо-161рпо": "d161.xlsx"}



def d(group):
    # for el in os.listdir():
    #     if groups[group] != el:
    #         continue
    group = groups[group]
    path= os.getcwd()
    excel_data_df = pandas.read_excel(path + f"/data/{group}")
    # excel_data_df = pandas.read_excel(el)
    json_str = excel_data_df.to_json(orient='records', force_ascii=False)
    student_details = json.loads(json_str)
    c = 0
    dict_lession = {}
    kur = []
    for el in student_details:
        if len(el["Время"].split(',')) != 1 and c == 0:
            name = el["Время"].split(',')[0].strip()
            c = 1
            kur.append(el)
            continue

        if len(el["Время"].split(',')) != 1:
            dict_lession[name] = kur
            kur = []
            name = el["Время"].split(',')[0].strip()
        kur.append(el)
    return dict_lession



def get_day_schedule(group) -> str:
    dict_lession = d(group)
    s = ''
    _d = dict_lession.get(get_date())
    if _d == None:
        s = "Сегодня у вас нет пар;)"
        return s



    for _val in _d[1:]:
        time = _val["Время"]
        lession = _val["Курс"]
        classroom = _val["Место проведения"]
        Teacher = _val["Преподаватель"]

        s += ("Время: " + time + '\n' + "Предмет: " + lession + '\n'
              + "Кабинет: " + '\n' + classroom + '\n' + 'Преподаватель: ' + Teacher + '\n\n')
    return s

def get_week_schedule(group) -> str:

    dict_lession = d(group)
    s = ''
    list_of_days_week = []
    date = int(get_date().split('.')[0])
    mounth = int(get_date().split('.')[1])
    day_of_week = get_day()
    r_day_of_week = date + (7 - day_of_week)
    l_day_of_week = (date + 1) - day_of_week
    for el in dict_lession.keys():
        day = int(el.split('.')[0])
        _mounth = int(el.split('.')[1])
        if day <= r_day_of_week and day >= l_day_of_week and _mounth == mounth:
            list_of_days_week.append(el)
    s += '~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    for el in list_of_days_week:
        s +=  '                           ' + el + '\n'
        for _val in dict_lession[el][1:]:
            time = _val["Время"]
            lession = _val["Курс"]
            classroom = _val["Место проведения"]
            Teacher = _val["Преподаватель"]

            s += ("Время: " + time + '\n' + "Предмет: " + lession + '\n'
                  + "Кабинет: " + '\n' + classroom + '\n' + 'Преподаватель: ' + Teacher + '\n\n')
        s += '~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    return s

# print(get_week_schedule(""))



# print(get_day_schedule("дбо-101рпо"))




