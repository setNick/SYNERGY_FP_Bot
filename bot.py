import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import F

from data.main_data import get_day_schedule, get_week_schedule, d
from button import keyboard, keyboard1

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
GROUP = ''

CREATORS = "{<} Студенты Фокультета программирования {<}\n\nЯзыкин Артем \nИлья Конищук \nТретьяков Андрей"

"""ВТОРАЯ ВЕРСИЯ"""

# Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)

logging.basicConfig(level=logging.INFO, filename='data/logs/my_logging.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Разработчики: \n{<} Студенты фокультета программирования {<}\n\nЯзыкин Артем \nИлья Конищук \nТретьяков Андрей")
    await message.answer("Привет, я бот-помощник от факультета программирования, расскажите, из какой вы группы?\n"
                         "Формат: ДБО-101рпо")


# Получение id пользователя
# @dp.message(Command("info"))
# async def cmd_info(message: types.Message):
#     idd = message.from_user.id
#     # print(idd)
#     await message.answer(f'Ваш id - {idd}')

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=message.chat.id, emoji=DiceEmoji.DICE)


@dp.message(F.text.lower() == "ℹ️информация")
async def answer_schedule(message: types.Message):
    await message.answer(
        "Разработчики: \n{<} Студенты фокультета программирования {<}\n\nЯзыкин Артем \nИлья Конищук \nТретьяков Андрей")
    await message.answer("Доступные команды:\nПерезапустить бота: /start", reply_markup=keyboard1)


@dp.message(F.text.lower() == "дбо-101рпо")
async def answer_schedule(message: types.Message):
    global GROUP
    GROUP = "дбо-101рпо"
    logging.info(f'[id: {message.from_user.id}|username: {message.from_user.username}|'
                 f'firs_name: {message.from_user.first_name}|last_name: {message.from_user.last_name}]')
    await message.answer("Что бы вы хотели бы узнать?", reply_markup=keyboard)


@dp.message(F.text.lower() == "дбо-161рпо")
async def answer_schedule(message: types.Message):
    global GROUP
    GROUP = "дбо-101рпо"
    logging.info(f'[id: {message.from_user.id}|username: {message.from_user.username}|'
                 f'firs_name: {message.from_user.first_name}|last_name: {message.from_user.last_name}]')
    await message.answer("Что бы вы хотели бы узнать?", reply_markup=keyboard)


@dp.message(F.text.lower() == "дбп-101рив")
async def answer_schedule(message: types.Message):
    global GROUP
    GROUP = "дбп-101рив"
    logging.info(f'[id: {message.from_user.id}|username: {message.from_user.username}|'
                 f'firs_name: {message.from_user.first_name}|last_name: {message.from_user.last_name}]')
    await message.answer("Что бы вы хотели бы узнать?", reply_markup=keyboard)


@dp.message(F.text.lower() == "дбо-102рпо")
async def answer_schedule(message: types.Message):
    global GROUP
    GROUP = "дбо-102рпо"
    logging.info(f'[id: {message.from_user.id}|username: {message.from_user.username}|'
                 f'firs_name: {message.from_user.first_name}|last_name: {message.from_user.last_name}]')
    # print(GROUP)
    await message.answer("Что бы вы хотели бы узнать?", reply_markup=keyboard)


@dp.message(F.text.lower() == "📆расписание")
async def answer_schedule(message: types.Message):
    if GROUP == '':
        await message.answer("Сначала выберите группу", reply_markup=keyboard)
    else:
        await message.answer("На какой день вы хотели бы узнать расписание: ", reply_markup=keyboard1)


@dp.message(F.text.lower() == "📆расписание на сегодняшний день")
async def answer_day_schedule(message: types.Message):
    if GROUP == '':
        await  message.answer("Сначала выберите группу", reply_markup=keyboard)
    else:
        s = get_day_schedule(GROUP)
        if s == '':
            await message.answer("Сегодняшние пары уже закончились")
        else:
            await message.answer("Вот ваше расписание:", reply_markup=keyboard)
            await message.answer(s)


@dp.message(F.text.lower() == "📆расписание на неделю")
async def answer_day_schedule(message: types.Message):
    if GROUP == '':
        await  message.answer("Сначала выберите группу", reply_markup=keyboard)
    else:
        if get_week_schedule(GROUP) == '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n':
            await message.answer("На этой неделе у вас нет пар;))")
        else:
            await message.answer("Вот ваше расписание:", reply_markup=keyboard)
            await message.answer(get_week_schedule(GROUP))


@dp.message()
async def echo(message: types.Message):
    await message.answer(text='Такой группы не существует, либо она будет добавлена в следующих обновлениях;)')


# Запуск процесса поллинга новых апдейтов
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
