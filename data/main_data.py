import os
import pandas

import json
from scripts.gtime import get_date, get_day
from scripts.gtime import h, mi
groups = {"дбо-101рпо": 'dbo101.xlsx', 'дбо-102рпо': "dbo102.xlsx", "дбп-101рив": 'dbp101.xlsx'}



def d(group):
    group = groups[group]
    path= os.getcwd()
    excel_data_df = pandas.read_excel(path + f"/data/{group}")
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
    date = get_date()
    _d = dict_lession.get(date)
    if _d == None:
        s = "Сегодня у вас нет пар;)"
        return s
    global mi, h
    mi = str(mi)
    h = str(h)
    if len(mi) != 2:
        mi = '0' + mi
    if len(h) != 2:
        h = '0' + h
    n_time = str(h) + str(mi)
    for _val in _d[1:]:
        time = _val["Время"]
        lession = _val["Курс"]
        classroom = _val["Место проведения"]
        teacher = _val["Преподаватель"]


        if len(time.split(' - ')) == 2:
            _time = time.split(' - ')[1]
            _h = _time.split(':')[0]
            _m = _time.split(':')[1]
            r_time = _h + _m
            if int(n_time) > int(r_time):
                continue
        else:
            _h = time.split(':')[0]
            _m = time.split(':')[1]
            r_time = _h + _m
            if int(r_time) < int(n_time):
                continue

        s += ("Время: " + time + '\n' + "Предмет: " + lession + '\n'
              + "Кабинет: " + '\n' + classroom + '\n' + 'Преподаватель: ' + teacher + '\n\n')
    return s

def get_week_schedule(group) -> str:

    dict_lession = d(group)
    s = ''
    list_of_days_week = []
    day = int(get_date().split('.')[0])
    month = int(get_date().split('.')[1])
    day_of_week = get_day()
    r_day_of_week = day + (7 - day_of_week)
    l_day_of_week = (day + 1) - day_of_week
    for el in dict_lession.keys():
        _day = int(el.split('.')[0])
        _month = int(el.split('.')[1])
        if (_day <= r_day_of_week) and (_day >= l_day_of_week) and (_month == month):
            list_of_days_week.append(el)
    s += '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
    for el in list_of_days_week:
        s += '                           ' + el + '\n'
        for _val in dict_lession[el][1:]:
            time = _val["Время"]
            lesson = _val["Курс"]
            classroom = _val["Место проведения"]
            teacher = _val["Преподаватель"]

            s += ("Время: " + time + '\n' + "Предмет: " + lesson + '\n'
                  + "Кабинет: " + '\n' + classroom + '\n' + 'Преподаватель: ' + teacher + '\n\n')
        s += '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
    return s

# print(get_week_schedule(""))







