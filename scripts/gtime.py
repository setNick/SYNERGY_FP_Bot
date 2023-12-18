import datetime

now = datetime.datetime.now()      # текущие дата и время
y = now.year
m = now.month
d = now.day
h = now.hour
mi = now.minute

s = now.second
ms = now.microsecond

def get_day() -> str:
    datetime.datetime(y, m, d, h, mi, s, ms)
    return datetime.datetime.isoweekday(now)

    # if language == 'ru':
    #     time_ru = {1: 'Понедельник', 2: 'Вторник', 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота",
    #                7: "Воскресенье"}
    #     return time_ru[datetime.datetime.isoweekday(now)]
    # else:
    #     time_eng = {1: 'Mon', 2: 'Tue', 3:"Wed", 4:"Thu", 5:"Fri", 6: "Sat", 7: "Sun"}
    #     return time_eng[datetime.datetime.isoweekday(now)]

def get_date():
    # print()
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%y")