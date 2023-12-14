from aiogram import types
kb = [
    [types.KeyboardButton(text="📆Расписание")],
    # [types.KeyboardButton(text="👕Мерч")],
    [types.KeyboardButton(text="ℹ️Информация")],
    ]

keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Что бы вы хотели узнать?"
)

kb1 = [
        [types.KeyboardButton(text="📆Расписание на сегодняшний день")],
        [types.KeyboardButton(text="📆Расписание на неделю")]
    ]

keyboard1 = types.ReplyKeyboardMarkup(
    keyboard=kb1,
    resize_keyboard=True,
    input_field_placeholder="Что бы вы хотели узнать?"
)

# start_kb =[
#     [types.KeyboardButton(text="ДБО-101рпо")],
#     [types.KeyboardButton(text="ДБО-102рпо"),
#     types.KeyboardButton(text="ДБО-161рпо")]
# ]
